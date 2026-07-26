/**
 * Smoke-load the Express app without listening (alias setup mirrors server.js).
 */
require('module-alias/register');
const path = require('path');
const moduleAlias = require('module-alias');

const srcDir = path.join(__dirname, '..', 'src');

moduleAlias.addAliases({
  '@app': path.join(srcDir, 'app'),
  '@lib': path.join(srcDir, 'lib'),
  '@config': path.join(srcDir, 'config'),
  '@middlewares': path.join(srcDir, 'middlewares'),
  '@logs': path.join(__dirname, '..', 'logs'),
  '@websockets': path.join(srcDir, 'websockets'),
  '@modules': path.join(srcDir, 'modules'),
  '@prisma/client': path.join(srcDir, 'prisma', 'client.js'),
});

moduleAlias.addAlias(
  '@prisma/client/runtime',
  path.join(__dirname, '..', 'node_modules', '@prisma', 'client', 'runtime'),
);

require('@lib/aliases').registerAllModuleAliases();

const createApp = require('@app/index');
const app = typeof createApp === 'function' ? createApp() : createApp;
console.log('APP_LOAD_OK', Boolean(app));
