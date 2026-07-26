/**
 * Curated demo seed orchestration (platform packs only).
 *
 * Usage:
 *   node scripts/seed-demo-data.js
 */

const fs = require('fs');
const path = require('path');
const {
  createSeedContext,
  DEFAULT_RANDOM_SEED,
  deterministicUuid,
  prisma,
} = require('./seeders/seed-runtime');
const env = require('@config/env');
const { seedOrgPack } = require('./seeders/seed-org-pack');
const { seedAccessPack } = require('./seeders/seed-access-pack');
const { seedSubscriptionsPack } = require('./seeders/seed-subscriptions-pack');
const { assertDemoTaskAllowed } = require('./demo-safety');

const getDeterministicDate = (sequence = 0, minuteOffset = 0, randomSeed = DEFAULT_RANDOM_SEED) => {
  const seedOffsetMs = (Math.abs(Number(randomSeed) || DEFAULT_RANDOM_SEED) % 100000) * 1000;
  return new Date(Date.UTC(2026, 1, 15, 9, 0, 0) + seedOffsetMs + (sequence + minuteOffset) * 60000);
};

const resolveNumericEnv = (value, fallback) => {
  const parsed = Number.parseInt(String(value), 10);
  return Number.isFinite(parsed) ? parsed : fallback;
};

const tryRequireSeeder = (relativePath) => {
  const absolutePath = path.join(__dirname, relativePath);
  if (!fs.existsSync(absolutePath)) {
    return null;
  }
  // eslint-disable-next-line import/no-dynamic-require, global-require
  return require(absolutePath);
};

const seedDemoData = async ({
  targetCount = 0,
  randomSeed = DEFAULT_RANDOM_SEED,
} = {}) => {
  const safety = assertDemoTaskAllowed('demo seed');
  if (!safety.allowed) {
    console.warn('Skipping seed: NODE_ENV=production');
    return { skipped: true, reason: safety.reason };
  }

  const ctx = createSeedContext({
    randomSeed,
    recordCount: targetCount,
  });

  console.log(`Seeding curated FCHIP demo data with random seed ${ctx.randomSeed}...`);

  const orgPack = await seedOrgPack(ctx);
  const accessPack = await seedAccessPack(ctx, orgPack);
  const subscriptionsPack = await seedSubscriptionsPack(ctx, orgPack);

  // HIS clinical / operations packs were removed; skip if files are absent.
  const skippedPacks = [];
  const optionalPacks = [
    { name: 'clinical_catalog', file: './seeders/seed-clinical-catalog-pack.js', exportName: 'seedClinicalCatalogPack' },
    { name: 'clinical', file: './seeders/seed-clinical-pack.js', exportName: 'seedClinicalPack' },
    { name: 'operations', file: './seeders/seed-operations-pack.js', exportName: 'seedOperationsPack' },
    { name: 'communications', file: './seeders/seed-communications-pack.js', exportName: 'seedCommunicationsPack' },
    { name: 'biomedical', file: './seeders/seed-biomedical-pack.js', exportName: 'seedBiomedicalPack' },
    { name: 'mortuary', file: './seeders/seed-mortuary-pack.js', exportName: 'seedMortuaryPack' },
    { name: 'compliance', file: './seeders/seed-compliance-pack.js', exportName: 'seedCompliancePack' },
    { name: 'governance', file: './seeders/seed-governance-pack.js', exportName: 'seedGovernancePack' },
    { name: 'filler', file: './seeders/seed-filler-pack.js', exportName: 'seedFillerPack' },
  ];

  for (const pack of optionalPacks) {
    const mod = tryRequireSeeder(pack.file);
    if (!mod || typeof mod[pack.exportName] !== 'function') {
      skippedPacks.push(pack.name);
    }
  }

  if (skippedPacks.length > 0) {
    console.log(`Skipping removed HIS seed packs: ${skippedPacks.join(', ')}`);
  }

  console.log('Platform demo data seeded successfully.');

  return {
    skipped: false,
    summary: {
      tenants: Object.keys(orgPack.tenants).length,
      users: Object.keys(accessPack.users).length,
      subscriptions: Object.keys(subscriptionsPack.subscriptions).length,
      skipped_packs: skippedPacks,
    },
  };
};

const main = async () => {
  try {
    await seedDemoData({
      targetCount: 0,
      randomSeed: resolveNumericEnv(env.SEED_RANDOM_SEED, DEFAULT_RANDOM_SEED),
    });
  } catch (error) {
    console.error('Failed to seed demo data:', error);
    process.exitCode = 1;
  } finally {
    await prisma.$disconnect();
  }
};

if (require.main === module) {
  main();
}

module.exports = {
  seedDemoData,
  deterministicUuid,
  getDeterministicDate,
};
