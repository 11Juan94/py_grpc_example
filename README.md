# NGINX Ingress Controller example for GRPC

This example was tested on localhost with docker-desktop (Windows) and kubernetes.
On linux extra configuration may be needed.

# Installation

Create TSL secret for kubernetes with localhost certificates.
```
kubectl create secret tls grpc-secret --key server.pem --cert server.crt
```
Example files are on folder **resources**. (are valid until 2022)

Apply the kubernetes configuration files wich are on folder **k8s**.
Start with ingress controller for 
```
kubectl apply -f deploy.yaml
kubectl apply -f deployment.yaml
kubectl apply -f ingress.yaml
```

# Test

Run the **greeter_client.py**.

## Missing tests
Missing testing multiple nodes and only 1 ingress controller and see if choose loadbalancing across nodes.
(Linkerd daemonset only do load balancing inside on node)
