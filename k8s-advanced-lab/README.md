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