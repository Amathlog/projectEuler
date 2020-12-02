pushd %~dp0
mkdir Problem%1
pushd Problem%1
type nul > problem.txt
type nul > solution.py
popd
popd
