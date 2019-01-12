#!/bin/sh

setup_git() {
  git config  user.email "travis@travis-ci.org"
  git config  user.name "Travis CI"
  git remote set-url origin https://${GITHUB_TOKEN}@github.com/taciossbr/taciossbr.github.io.git > /dev/null 2>&1
  git pull origin master
  
}

commit_website_files() {
  git checkout -b gh-pages
  git add . *.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-pages https://${GH_TOKEN}@github.com/MVSE-outreach/resources.git > /dev/null 2>&1
  git push --quiet --set-upstream origin-pages gh-pages 
}

setup_git
# commit_website_files
# upload_files
