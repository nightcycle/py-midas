source env/Scripts/Activate
# stubgen src/midas -o src
py -m build
twine upload dist/midas-data-util-0.2.4.tar.gz -u nightcycle -p yHEc3E7sXx4DCP --verbose