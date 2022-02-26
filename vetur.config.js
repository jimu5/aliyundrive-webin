// vetur.config.js
/** @type {import('vls').VeturConfig} */
module.exports = {
    // **optional** default: `[{ root: './' }]`
    // support monorepos
    projects: [
      './frontend', // Shorthand for specifying only the project root location
      {
        // **required**
        // Where is your project?
        // It is relative to `vetur.config.js`.
        root: './frontend'
      }
    ]
};