# swe1-app

[![Build Status](https://app.travis-ci.com/Sumisha4/swe1-app.svg?branch=main)](https://app.travis-ci.com/Sumisha4/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/Sumisha4/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/Sumisha4/swe1-app?branch=main)

Django polls tutorial (Parts 1-4) deployed to AWS Elastic Beanstalk.

Live site: http://django-env.eba-tfccrzxp.us-east-2.elasticbeanstalk.com/polls/

## Continuous integration

Every push and pull request is built on Travis CI, which:

1. checks formatting with `black --check .`
2. lints with `flake8`
3. runs the test suite under `coverage` and reports to Coveralls
4. deploys to Elastic Beanstalk when the build on `main` passes

## Running locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/polls/ in a browser.
