FROM python

# Application setup...

COPY . /code/ # Copy source coude with all the tests.
WORKDIR /code
CMD py.test --junitxml=/data/test_report.xml \
            --cov-report xml:/data/coverage.xml