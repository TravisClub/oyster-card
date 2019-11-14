#!/usr/bin/env bash

pushd "${0%/*}"
pushd ..

python -m pytest -vv \
--cov=. \
--cov-report=html:reports/coverage \
--cov-report=xml:reports/coverage/coverage.xml \
--cov-config=scripts/.coveragerc \
tests/

popd
popd