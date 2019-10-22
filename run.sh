python3 generate_data.py > data.in

openssl genrsa -out private_key.pem 2048
openssl rsa -in private_key.pem -out public_key.pem -pubout
cat public_key.pem
python3 generate_signature.py < data.in
cat data.in
echo ''