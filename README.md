# Internal Approval Request Generator
This is a simple program to help you generate approval request for [Internal Approval System](https://github.com/iamdejan/internal_approval_system) project.

## Getting Started

### Prerequisites
- Python 3.7
- PyCrypto 2.6.1

### What to Do
You can edit the data from `generate_data.py`, since that file will generate the data that will be signed later. However, for now, I expect your data to be in **JSON format** (not JSON string).

### Run The Program
Just run this command in terminal:
`sh run.sh`

## FAQ
1) **Question**: What algorithm do you use for this?
**Answer**: For the hashing, I use SHA512. For public and private keys, I use RSA 2048.
2) **Question**: After  I get the results (public key, signature, and data), what should I do?
**Answer**: you can run the server for Internal Approval System. After that, you can use either Postman / cURL to send the POST request to [Approval Request endpoint](https://github.com/iamdejan/internal_approval_system/blob/master/system/urls.py#L26). You can refer to sample request [here](https://github.com/iamdejan/internal_approval_system/blob/master/system/views/project.py#L13).

## Authors
- [Giovanni Dejan](https://github.com/iamdejan)