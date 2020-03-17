#!/usr/bin/env python3
"""
Created on September 21 2019

@author: Melchior du Lac
@description: Galaxy script to query rpCofactors REST service

"""
import json
import argparse
import requests
import tempfile
import tarfile
import os

def rpCofactorsUpload(inputTar,
        pathway_id,
        compartment_id,
        server_url,
        outputTar):
    # Post request
    data = {'pathway_id': pathway_id, 'compartment_id': compartment_id}
    files = {'inputTar': open(inputTar, 'rb'),
             'data': ('data.json', json.dumps(data))}
    r = requests.post(server_url+'/Query', files=files)
    r.raise_for_status()
    with open(outputTar, 'wb') as ot:
        ot.write(r.content)

##
#
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Python wrapper to add cofactors to generate rpSBML collection')
    parser.add_argument('-input', type=str)
    parser.add_argument('-output', type=str)
    parser.add_argument('-input_format', type=str)
    parser.add_argument('-pathway_id', type=str)
    parser.add_argument('-compartment_id', type=str)
    parser.add_argument('-server_url', type=str)
    params = parser.parse_args()
    if params.input_format=='tar':
        rpCofactorsUpload(params.input,
                          params.pathway_id,
                          params.compartment_id,
                          params.server_url,
                          params.output) 
    elif params.input_format=='sbml':
        #make the tar.xz 
        with tempfile.TemporaryDirectory() as tmpOutputFolder:
            inputTar = tmpOutputFolder+'/tmp_input.tar.xz'
            outputTar = tmpOutputFolder+'/tmp_output.tar.xz'
            print(params.input)
            with tarfile.open(inputTar, mode='w:xz') as tf:
                info = tarfile.TarInfo('single.rpsbml.xml') #need to change the name since galaxy creates .dat files
                info.size = os.path.getsize(params.input)
                #info = tarfile.gettarinfo(fileobj=params.input)
                #info.arcname = 'single.rpsbml.xml'
                tf.addfile(tarinfo=info, fileobj=open(params.input, 'rb'))
                tf.list()
            with tarfile.open('/home/mdulac/Downloads/test_out.tar.xz', mode='w:xz') as tf:
                info = tarfile.TarInfo('single.rpsbml.xml') #need to change the name since galaxy creates .dat files
                info.size = os.path.getsize(params.input)
                #info = tarfile.gettarinfo(fileobj=params.input)
                #info.arcname = 'single.rpsbml.xml'
                tf.addfile(tarinfo=info, fileobj=open(params.input, 'rb'))
            rpCofactorsUpload(inputTar,
                              params.pathway_id,
                              params.compartment_id,
                              params.server_url,
                              outputTar) 
            with tarfile.open(outputTar) as outTar:
                outTar.extractall(tmpOutputFolder)
            out_file = glob.glob(tmpOutputFolder+'/*.rpsbml.xml')
            if len(out_file)>1:
                logging.warning('There are more than one output file...')
            shutil.copy(out_file[0], params.output)
    else:
        logging.error('Cannot identify the input/output format: '+str(params.input_format))
