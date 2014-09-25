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
          './vendor/bower/jquery/dist/jquery.min.js',
          './vendor/bower/underscore/underscore-min.js',
          './emission_events/static/scripts/{,*/}*.js'
        ],
        dest: './emission_events/static/js/app.js',
      },
    },

    sass: {
      dist: {
        files: {
          './emission_events/static/css/app.css': './emission_events/static/scss/app.scss'
        }
      }
    },

    jshint: {
      options: {
        jshintrc: '.jshintrc',
        reporter: require('jshint-stylish')
      },
      all: [
        'emission_events/static/scripts/{,*/}*.js'
      ]
    },

    watch: {
      sass: {
        files: ['emission_events/static/scss/**/*.scss'],
        tasks: ['sass']
      },
      js: {
        files: ['emission_events/static/scripts/{,*/}*.js'],
        tasks: ['jshint', 'concat']
      },
    }
  });

  grunt.registerTask('dev', [
    'watch'
  ]);

};
