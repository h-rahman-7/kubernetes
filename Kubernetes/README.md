# Kubernetes - k8s 

- Is the leading container orchestration tool
- Designed as a loosely coupled collection of components centered around deploying, maintaining and scaling workloads
- Vendor-neutral
	- Runs on all cloud providers
- Backed by huge community

**What do K8s do?**
- Service discovery and load balancing
- Storage Orchestration
	- Local or Cloud based
- Automated rollouts and rollbacks
- Self-healing
- Secret and configuration management
- Use the same API across on-prem and cloud
**What K8s cannot do**
- Does not deploy source code
- Does not build your application
- Does not provide application-level services
	- Message buses ,databases, caches etc

**K8s Architecture Image**

![alt text](./images/k8sArchitecture.png)

**Composed of**
- Master Node also known as control plane
	- Runs Kubernetes services and controllers
- Worker Nodes
	- Runs the containers that you deploy 

**Example**
- Container runs in a pod
	- Pod runs in a node
		- All nodes form a cluster

![alt text](./images/clusterToPod.png)

## Running Kubernetes Locally

**Local K8s**
- Requires Virtualisation
	- Docker Desktop
	- MicoK8s
	- Minikube
- Runs over Docker Desktop
	- Kind (Kubernetes in Docker)
- Limited to 1 Node
	- Docker Desktop
- Multiple Nodes
	- MicroK8s
	- Minikube
	- Kind
- Windows
	- Docker Desktop is currently only way to run both Linux and windows containers
		- Runs on Hyper-V or WSL 2
	- If Hyper-V is enabled, you can't run another hypervisor at the same time
	- You can install Minikube on Hyper-V or Virtual Box

**Kubernetes Local** - Using CMD or PowerShell

-  This command lets you check if Kubernetes is running: `kubectl cluster-info dump

**Kubernetes CLI**
- K8s API:

![alt text](./images/k8sAPI.png)

- **kubectl** - The main command for K8s
	- Communicates with the api server
	- Configuration stored locally under:
		- ${HOME}/.kube/config
		- C:\Users\{USER}\.kube\config
- **K8s Context**
	- A context is a group of access parameters to a K8s cluster
	- Containers a Kubernetes cluster, a user and a namespace
	- The current context is the cluster that is currently the default for kubectl
		- All kubectl commands run against that cluster

![alt text](./images/kubectl-cheatsheet.png)

- Kube tools
	- kubectl - Useful for fast context usage, install using: `choco install kubectx-ps` if you have 'Choco' installed
- Rename a context: `kubectl config rename-context [oldname] [newname]`

**Declarative vs Imperative**
- Imperative:
	- Using kubectl commands, issue a series of commands to create resources
	- Great for learning, testing and troubleshooting
	- It's like code
- Declarative:
	- Using kubectl and YAML manifests defining the resources you need
	- Reproducible and repeatable
	- can be saved in source control
	- Its like data that can be parsed and modified

**Imperative**:

![alt text](./images/Imperative.png)

**Declarative**:

![alt text](./images/Declarative.png)

## **YAML**
 - Root level required properties
	 - apiVersion
		 - Api version of the object
	- kind
		- type of object
	- metadata.name
		- unique name for the object
	- metadata.namespace
		- scoped environment name (will default to current)
	- spec
		- object specifications or desired state
- Create an object using YAML
	  kubectl create -f [YAML file]
  
![alt text](./images/PodDefinition.png)

**Note:**
- We do NOT need to type all the YAML manually, we can get the syntax from kubernetes.io/docs and search and copy
- We can create using manifests (templates) in VS Code, in new YAML file, hitting ctrl+space and select the template you need
- Kubernetes CLI to generate manifests: `--dry-run=cleient -o yaml`

## Deploying an Imperative and Declarative container

- For **Imperative**:
	- `kubectl create deployment mynginx1 --image=nginx` 
	- we can check if its created using: `kubectl get  deploy`
- For **Declarative**
	- `kubectl create -f deploy-example.yaml` - Must have the 'deploy-example.yaml' file exist and must contain some data
- **Useful commands**
	- `kubectl get  deploy` - Listing all the running deployments
	- `kubectl delete deploy example-deployment-name ` - after running the first command, you can delete using the 'name' 

## Namespaces
- Allow to group resources
	- Example: Dev,Test,Prod
- K8s create a default workspace
- Objects in one namespace can access objects in a different one
	- Example: objectname.**prod**.scv.cluster.local
- Deleting a namespace will delete all its child objects

- Define a namespace
- Specify the namespace when defining objects

![alt text](./images/pod-namespace.png)

- You can limit resources using the resource quota object

![alt text](./images/resource-quota.png)

**Kubectl - Namespace sheet commands**

![alt text](./images/Namespace-cheatsheet.png)


# Kubernetes Storage

- **Why Persistent Storage?**
  - Pods are **ephemeral** – created and deleted often, so not ideal for storing data!
  - Persistent storage provides **data reliability** beyond the pod lifecycle.
  - Essential for **stateful applications** like:
    - Databases
    - Message queues
    - Apps that need to remember past interactions

- **Persistent Volumes (PV)**
  - Acts as **dedicated storage** in Kubernetes (like a shared hard drive).
  - **Created by admins** and available for applications to use.
  - Think of it as **pre-configured storage** ready to go when needed.

- **Persistent Volume Claim (PVC)**
  - PVC is how an app requests storage – **“I need space”**.
  - When a PVC matches an available PV, it gets **bound** to that volume.
  - Similar to asking IT for shared storage; once approved, you can use it freely.


# ConfigMaps

- **Purpose**: Store non-confidential data needed by applications in Kubernetes.
- **Configuration Management**: Provides a way to manage and supply configuration settings to pods without embedding values directly in application code.
- **Flexibility**: Allows **dynamic configuration changes** without needing to rebuild the application.
- **Usage**:
  - Used for items like environment variables, config files, command-line arguments, etc.
  - Ideal for things like API URLs, app modes (development, production), and other non-sensitive settings.
- **Consistency**: Ensures that **pods receive correct configurations** every time they start, making deployments more reliable.

Creating a Config map:

- $ kctl create configmap my-config --from-literal=APP_COLOUR=blue --from-literal=APP_MODE=production

## Secrets

- Store sensitive data securely in Kubernetes by encoding it as Base64.
- Create a secret with the command:
  ```
  kubectl create secret generic my-secret --from-literal=username=myuser --from-literal=password=mypassword
  ```
To retrieve and view secrets in YAML format:

`kubectl get secrets -o yaml`

The output will include encoded values like:
```
data:
  password: bXlwYXNzd29yZA==
  username: bXl1c2Vy
```
Decode a secret (e.g., password) with:

`echo "bXlwYXNzd29yZA==" | base64 -d` <br>
This returns the original plaintext values.

# Kubernetes Networking

Pod Networking: All pods can communicate with each other and with nodes without Network Address Translation (NAT).

Cluster-IP Consistency: The IP a pod sees for itself is the same IP that others use to reach it.

For example, create two pods, apache and nginx:

```
kubectl run apache --image=httpd
kubectl run nginx --image=nginx
```
Verify they’re running:

`kubectl get pods`

```
NAME    READY   STATUS    RESTARTS   AGE
apache  1/1     Running   0          10s
nginx   1/1     Running   0          20s
```
Get pod IP addresses:


`kubectl get pods -o wide`

```
Copy code
NAME    READY   STATUS    RESTARTS   AGE   IP          NODE
apache  1/1     Running   0          20s   10.244.0.9  minikube
nginx   1/1     Running   0          30s   10.244.0.8  minikube
```
Access nginx pod terminal:
```
kubectl exec nginx -it -- sh
```
Inside nginx, use curl to reach the apache pod:

`curl 10.244.0.9`

Expected output:

`<html><body><h1>It works!</h1></body></html>` 

This confirms inter-pod communication without explicit network configuration.


## Service Discovery and DNS

Service Discovery: Kubernetes Services abstract and manage access to pods.

DNS: Enables automatic name resolution for services, facilitating intra-cluster connectivity.

Key Concepts:
Service Types: ClusterIP, NodePort, LoadBalancer, etc.
DNS Lab: Test DNS with a network troubleshooting image:

`kubectl run tmp-shell --rm -i --tty --image=moabukar/netshoot`

# Network Policies

Network policies are sets of rules that govern communication between pods, defining which pods can interact with each other and with external resources. Without these policies, all pods can communicate freely—this isn’t ideal in production, where tighter controls are necessary.

For instance, network policies can restrict frontend pods to only communicate with backend pods, while backend pods connect solely with a database. This ensures structured and secure interactions between services.

### Key Concepts
- **Pod Communication Control**: Defines how groups of pods communicate with each other and external network endpoints.
- **Ingress**: Controls incoming traffic to pods.
- **Egress**: Controls outgoing traffic from pods.

### Ingress Controller
- Manages external access to services within the cluster, typically over HTTP/HTTPS.
- Routes external requests to the appropriate service based on predefined rules.

### Egress Controller
- Controls outbound traffic from the pods to external services.
- Often used to enforce network security policies and restrict external access.

# Types of Services
## 1. ClusterIP
- Default Service Type in Kubernetes.
- Exposes the Service only within the cluster, making it inaccessible from outside.
- Ideal for internal communication between different components of the application.
- Uses a cluster-internal IP that other Pods can access.

```
apiVersion: v1
kind: Service
metadata:
  name: my-clusterip-service
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: my-app
```
## 2. NodePort

- Exposes the Service on a static port (between 30000-32767) on each Node in the cluster.
- NodePort: the port on each Node that allows external access.
- Port: the port on the Service for internal communication within the cluster.
- TargetPort: the actual port on the Pod.
- Good for basic external access, but it exposes every node and is generally not used in production.
```
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30007
  selector:
    app: my-app
```

## 3. LoadBalancer
- Creates an external load balancer that directs traffic to the Service's Pods.
- Ideal for production, especially on cloud providers (AWS, GCP), where it automatically provisions load balancing infrastructure.
-Uses NodePort and ClusterIP internally, providing simplicity for exposing services externally.
- Note: This can be costly as it depends on the cloud provider's load balancing features.

```
apiVersion: v1
kind: Service
metadata:
  name: my-loadbalancer-service
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: my-app
```

## 4. ExternalName
- Maps a Service to an external DNS name (e.g., `example.com`), without creating a new endpoint.
- Adds a DNS CNAME record to allow access to external services by name within the cluster.
- Useful for services outside the cluster that need internal access by name.

```
apiVersion: v1
kind: Service
metadata:
  name: my-externalname-service
spec:
  type: ExternalName
  externalName: example.com
```
## Ports in Kubernetes Services
### NodePort, Port, and TargetPort Explained
- Port: The internal cluster port used by other services in the cluster to access this Service.
- TargetPort: The specific port on the Pod that the Service points to.
- NodePort: Exposes the Service on a fixed port across each node, allowing external access (used with `NodePort` or `LoadBalancer` services).


# Scheduling

Kubernetes Scheduling is responsible for assigning Pods to Nodes in a cluster. 
The scheduler considers resource availability, constraints, and other factors to ensure Pods are efficiently distributed across the Nodes.

### 1. Basic Scheduling Concepts: <br>
- Scheduler: The core component that decides where each Pod should run.
- Node Selection: The scheduler selects an appropriate Node based on resource requests, Node capacity, and constraints defined for each Pod.
- Binding: Once a Node is chosen, the Pod is bound to that Node for deployment.

```
apiVersion: v1
kind: Pod
metadata:
  name: my-scheduled-pod
spec:
  nodeName: node01
  containers:
    - name: app-container
      image: nginx
```

### 2. Resource Requests and Limits
- Requests: Minimum resources (CPU, memory) a Pod needs to function. Ensures the Pod has enough resources allocated on a Node.
- Limits: Maximum resources a Pod can consume. Prevents Pods from overusing resources and affecting other workloads.
Helps the scheduler determine if a Node has sufficient resources to support a Pod.

```
apiVersion: v1
kind: Pod
metadata:
  name: my-resource-pod
spec:
  containers:
    - name: app-container
      image: nginx
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

### 3. Affinity and Anti-Affinity <br>
- Affinity: Specifies that a Pod should run near other specified Pods, often for performance or proximity needs.
- Anti-Affinity: Specifies that a Pod should avoid certain Nodes or Pods, often to increase redundancy or prevent resource conflicts.
Defined using Node or Pod labels to guide the scheduler’s placement decisions.

```
apiVersion: v1
kind: Pod
metadata:
  name: my-affinity-pod
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              app: my-app
          topologyKey: "kubernetes.io/hostname"
  containers:
    - name: app-container
      image: nginx
```

### 4. Taints and Tolerations
- Taints: Applied to Nodes to repel certain Pods, typically to reserve Nodes for specific tasks.
- Tolerations: Applied to Pods to allow them to tolerate certain Node taints, granting access to those Nodes.
Useful for workloads that require isolation or specialised Node resources.

```
apiVersion: v1
kind: Pod
metadata:
  name: my-toleration-pod
spec:
  tolerations:
    - key: "example-key"
      operator: "Exists"
      effect: "NoSchedule"
  containers:
    - name: app-container
      image: nginx
```

### 5. Node Selectors and Node Affinity
- Node Selectors: Basic method of specifying which Nodes a Pod should run on based on labels.
- Node Affinity: More advanced than Node Selectors, allowing expressions and conditions for scheduling decisions.

```
apiVersion: v1
kind: Pod
metadata:
  name: my-node-affinity-pod
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: "kubernetes.io/e2e-az-name"
                operator: In
                values:
                  - e2e-az1
                  - e2e-az2
  containers:
    - name: app-container
      image: nginx
```

# Selectors

To create and label pods, we write under `metadata`:

```
apiVersion: v1
kind: Pod
metadata:
	name: web-app
	labels:
		app: App1
		function: Front-endpoint
```
You can have as many different labels as you want

To select the pod once its created using a specific label we can use `--selector` for example:

`kubectl get pods --selector app=App1` if the label is only checking for `App1` anywhere, you can also use `kubectl get pods --selector=App1`

To get a specific pod for example: "Identify the POD which is part of the prod environment, the finance BU and of frontend tier?":

We can use: `k get all --selector env=prod,bu,tier=frontend`

In `Replica Sets` we use `Selectors` and `matchLabels` to specify which pod we want with the corresponding name:

```
spec:
	replicas: 3
	selector: 
		matchLabels:
			app: App1
	template:
		metadata:
			labels:
				app: App1
```