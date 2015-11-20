'use strict';

module.exports = function(grunt) {

  // Load grunt tasks automatically
  require('load-grunt-tasks')(grunt);

  // Time how long tasks take
  require('time-grunt')(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    concat: {
      options: {
        separator: ';',
      },
      dist: {
        src: [
          './webapp/vendor/bower/jquery/dist/jquery.min.js',
          './webapp/vendor/bower/underscore/underscore-min.js',
          './webapp/js/{,*/}*.js'
        ],
        dest: './emission_events/static/js/app.js',
      },
    },

    sass: {
      options: {
        loadPath: ['webapp/vendor/bower']
      },
      dist: {
        files: {
          './emission_events/static/css/app.css': './webapp/scss/app.scss'
        }
      }

    },

    jshint: {
      options: {
        jshintrc: '.jshintrc',
        reporter: require('jshint-stylish')
      },
      all: [
        'webapp/js/{,*/}*.js'
      ]
    },

    watch: {
      sass: {
        files: ['webapp/scss/**/*.scss'],
        tasks: ['sass']
      },
      js: {
        files: ['webapp/js/{,*/}*.js'],
        tasks: ['jshint', 'concat']
      },
    }
  });

  grunt.registerTask('dev', [
    'watch'
  ]);
  grunt.registerTask('default', ['watch']);
  grunt.registerTask('build', ['sass', 'concat']);
};
