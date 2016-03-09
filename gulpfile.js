var gulp = require('gulp'),
  fs = require('fs'),
  sass = require('gulp-sass'),
  connect = require('gulp-connect'),
  gutil = require('gulp-util'),
  prompt = require('gulp-prompt'),
  exec = require('child_process').exec,
  GulpSSH = require('gulp-ssh'),
  git = require('gulp-git'),
  minify = require('gulp-minifier'),
  RevAll = require('gulp-rev-all'),
  del = require('del'),
  paths = {
    files: ['./**/*.{html,js}'],
    sass: ['./scss/**/*.scss', './Cats-Galore/**/*.scss']
  };

gulp.task('default', ['dev', 'sass', 'watch']);

gulp.task('dev', function() {
  connect.server({
    port: 8000,
    livereload: true
  });
});

gulp.task('sass', function(cb) {
  gulp.src('./scss/bootstrap/_bootstrap.scss')
    .pipe(sass({
      errLogToConsole: true
    }))
    .pipe(gulp.dest('./css/'))
    .pipe(connect.reload())
    .on('end', cb);
});

gulp.task('files', function() {
  gulp.src(paths.files[0])
    .pipe(connect.reload());
});

gulp.task('watch', function() {
  gulp.watch(paths.sass, ['sass']);
  gulp.watch(paths.files, ['files']);
});

gulp.task('update', function(cb) {
  var name = fs.readFileSync('./logs/name.json', {
    encoding: 'UTF-8'
  });
  exec('git pull origin ' + name, function(err, stdout) {
    exec('git push server ' + name, function(err, stdout) {});
  });
});
