basePath = '../';

files = [
  JASMINE,
  JASMINE_ADAPTER,
  'app/static/lib/angular/angular.js',
  'app/static/lib/angular/angular-*.js',
  'test/lib/angular/angular-mocks.js',
  'app/static/js/**/*.js',
  'test/unit/**/*.js'
];

autoWatch = true;

browsers = ['Chrome'];

junitReporter = {
  outputFile: 'test_out/unit.xml',
  suite: 'unit'
};
