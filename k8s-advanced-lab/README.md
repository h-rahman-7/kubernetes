Get the secret password for the argo-cd login:

`kubectl get secret argocd-initial-admin-secret -n argo-cd -o jsonpath='{.data.password}' | base64 --decode`