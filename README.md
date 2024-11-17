# K8s Advanced Project  
_Hello and welcome to K8s advanced labs. In this project we will be discussing how to set up a production grade EKS cluster from start to finish_  

Just like a real world dev environment we will be discussing:
- how to host your app and,
- expose securely to public using industry standards tools
  - includes setting up DNS records and managing certificates for https
- automating set-up efficiently, reliably and securley

By the of this exercise you should grasp how to take an application from internal deployment all the way to being acessible securely over the internet.

The key takeaways for DevOps:
`making sure things are scalable, maintainable and reliable`

This project mirrors what you would encounter in a production environment touching on the tools and processes that happen bts. 

## What tools will we use?
- create clusters using terraform on AWS via EKS
- Helm (K8s package manager)
- NGINX ingress controller (ingress traffic routing management) 
- Let's encrypt (certificate authority)
- cert-manager (to automate certificate mangement)
- external-dns (automate and sync services with your DNS provider, in this case route53)
- add ArgoCD 

























Get the secret password for the argo-cd login:

`kubectl get secret argocd-initial-admin-secret -n argo-cd -o jsonpath='{.data.password}' | base64 --decode`

When kubectl get <resource> doesnt work, the steps to fix it:

`aws eks update-kubeconfig --region us-east-1 --name eks-lab`

or

Add the access policies to the EKS cluster:

`AmazonEKSAdminPolicy` and `AmazonEKSClusterAdminPolicy`

Update the kubeconfig:

`aws eks --region us-east-1 update-kubeconfig --name eks-lab`

Deploy the ingress using:

`kubectl apply -f https://raw.githubusercontent.com/kubernetes/nginx-ingress/main/deploy/static/provider/cloud/deploy.yaml`

If CRD's dont get installed correctly run:

`kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.10.1/cert-manager.crds.yaml`