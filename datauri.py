import sys
import mimetypes
import argparse
import os
import base64

def generate_datauri(mime, content):
    b64_contents = base64.b64encode(content)
    b64_contents = b64_contents.decode('ascii').replace('\n','')
    return "data:{};base64,{}".format(mime, b64_contents)

def generate_datauri_from_file(infile):
    mime, _ = mimetypes.guess_type(infile, strict=False)
    content = None
    try:
        with open(infile, 'r') as f:
            content = f.read()
        content = content.encode('utf-8')
    except:
        with open(infile, 'rb') as f:
            content = f.read()
    return generate_datauri(mime, content)

def main():
    mimetypes.init()
    parser = argparse.ArgumentParser(description='convert a file into a Data URI (https://en.wikipedia.org/wiki/Data_URI_scheme)')
    parser.add_argument('infile')
    args = parser.parse_args()
    sys.stdout.write(generate_datauri_from_file(args.infile))

if __name__ == '__main__':
    main()
