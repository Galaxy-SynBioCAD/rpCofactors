# rpCofactors 

* rpCofactors Docker Image: [brsynth/rpCofactors-standalone](https://hub.docker.com/r/brsynth/rpcofactors-standalone)

Completes monocomponent reaction output by RetroPath2.0 with the appropriate cofactors. Creates sub-paths when multiple reaction rules are associated with a single reaction. Inout may be a single SBML file or a collection within a tar.xz archive

### Input

Required:
* **-input**: (String) Path to the input file. Can be either a single SBML file or a collection as a tar.xz archive file
* **-input_format**: (String) 

Advanced Options:
* **-pathway_id**: (String) ID of the heterologous pathway in the SBML (default: rp_pathway)
* **-compartment_id**: (String) ID of the SBML compartment where the heterologous pathway will be expressed in (default: MNXC3 (i.e. cytoplasm))

### Output

* **-output**

## Building the docker

To build the docker locally, run the following command in the project directory: 

```
docker build -t brsynth/rpcofactors-standalone:dev .
```

## Running the test

To test untar the test.tar.xz file and run the following command:

```
python run.py -input test/test_rpReader.tar -output test/test_rpCofactors.tar -input_format tar
```

## Dependencies

* Base docker image: [brsynth/rpBase](https://hub.docker.com/r/brsynth/rpbase)
* Cache docker image: [brsynth/rpCache](https://hub.docker.com/r/brsynth/rpcache)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Version 0.1

## Authors

* **Melchior du Lac**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thomas Duigou
* Joan Hérisson

## How to cite rpCofactors?
