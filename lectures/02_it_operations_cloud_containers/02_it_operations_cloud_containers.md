E-mail: Kamen.Kanchev@UniCreditGroup.BG 


UniCredit - Internal Use Only 

1 


**----- Start of picture text -----**<br>
Agenda<br>**----- End of picture text -----**<br>


## _**Cloud Computing**_ 


**----- Start of picture text -----**<br>
2<br>**----- End of picture text -----**<br>


## _**Server Virtualization**_ 


**----- Start of picture text -----**<br>
3<br>Hyper-V<br>Containers<br>4<br>**----- End of picture text -----**<br>


**----- Start of picture text -----**<br>
5<br>5<br>**----- End of picture text -----**<br>


_**Containers Orchestration**_ 

UniCredit - Internal Use Only 

## • **What is Cloud computing?** 

Cloud computing is a paradigm of computing model for enabling convenient, on-demand access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. 

This cloud model promotes availability and is composed three main service models, and 3 deployment models 

- **Primary cloud deployment models** 

   - Public Cloud 

   - Private Cloud 

   - Hybrid Cloud 

Win. The Right Way. Together. 


**3** 

UniCredit - Internal Use Only 

Win. The Right Way. Together. 

**4** 

UniCredit - Internal Use Only 

- A Cloud Service provider is a company that offers components of cloud infrastructure as 

- computing typically, a service (IaaS), software as a service (SaaS) or platform as a service (PaaS) 

- Cloud service use their own providers 

- Data Center and compute recourse to host cloud computing-based infrastructure for customers. Cloud services typically are priced using payas-you-go models 


Win. The Right Way. Together. 

**5** 

UniCredit - Internal Use Only 


- ➢ Typically build and used within the organization 

- ➢ Compute, Storage, and Network equipment are owned by the Organization 

- ➢ Hosted into the Organization Data Center 

- ➢ Internally managed 

**UniCredit Bulbank relay mainly on its own Private Cloud** 


Win. The Right Way. Together. 

**6** 

UniCredit - Internal Use Only 

- ➢ Main technology used in the Cloud Computing is Server Virtualization 

- ➢ Server Virtualization allow creating more logical Server, called Virtual Machines, within one physical Server 

- ➢ **Hypervisor** is the software layer that allow the virtualization 


**----- Start of picture text -----**<br>
App App App<br>Operating System<br>Hardware<br>**----- End of picture text -----**<br>


## **Traditional Stack** 


**----- Start of picture text -----**<br>
App App App<br>OS OS OS<br>Hypervisor<br>Hardware<br>**----- End of picture text -----**<br>


## **Virtualized Stack** 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 

## **Old model** 

- ➢ Many diverse physical servers in Data Center 

- ➢ One server -> One OS -> One ore multiple applications 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 


**----- Start of picture text -----**<br>
Hypervisor<br>**----- End of picture text -----**<br>


## **New model** 

- ➢ Small number of physical servers in Data Center 

- ➢ One server -> Hypervisor -> Different OS -> One application per virtual server 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 

- ➢ Type 1 hypervisor: hypervisors run directly on the system hardware – A “bare metal” embedded hypervisor 

- ➢ Type 2 hypervisor: hypervisors run on a host operating system that provides virtualization services, such as I/O device support and memory management 


Win. The Right Way. Together. 


UniCredit - Internal Use Only 

- ➢ Used mainly for development and test purposes 

- ➢ Can be installed on very laptop and Desktop machine 

- ➢ Most popular Type 2 Hypervisors 

   - VMware Workstation/Player – Windows and Linux PCs 

   - Oracle VM VirtualBox - Windows and Linux PCs 

   - VMware Fusion – Mac 

   - QEMU -Mac 


**----- Start of picture text -----**<br>
Win.<br>The Right Way.<br>Together.<br>**----- End of picture text -----**<br>


UniCredit - Internal Use Only 

- ➢ Used in the Enterprise 

- ➢ Require specific Hardware 

- ➢ Provide features to ensure High Availability 

- ➢ Most popular Type 1Hypervisors 

   - VMware ESXi 

   - Microsoft Hyper V 

   - Citrix Xen servers 

   - Red Hat OpenStack 


## **UniCredit Bulbank relay mainly on Hyper-V for Server Virtualisation** 

Win. The Right Way. Together. 


UniCredit - Internal Use Only 


Win. The Right Way. Together. 


UniCredit - Internal Use Only 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 

- **Each Virtual Machine  consists** 

- ➢ **Virtual Machine hard disk Files** 

- ➢ **Virtual Machine Configuration file** 


Win. The Right Way. Together. 


**15** 

UniCredit - Internal Use Only 

Live migration 

- Faster and simultaneous migration 

- No Down Time 


**----- Start of picture text -----**<br>
M od fiedStorage handle movedemory L i ve migration setup pages transferred<br>VM Modified memory pagesConfiguratioMemory co n ten da t a VM<br>IP connection<br>SMB network storage<br>MEMORY<br>**----- End of picture text -----**<br>


Win. The Right Way. Together. 

UniCredit - Internal Use Only 


Win. The Right Way. Together. 

# Let’s have a break 

Win. The Right Way. Together. 


UniCredit Bulbank 

UniCredit - Internal Use Only 

➢ A way to package an application with all necessary dependencies and configuration ➢ Can be easily shared and moved around ➢ Makes development and deployment process  more efficient 


Win. The Right Way. Together. 

**19** 

UniCredit - Internal Use Only 

**Lightweight OS-virtualization Application packaging for portable, reusable software** 


Win. The Right Way. Together. 


20 

UniCredit - Internal Use Only 


➢ Servers – OS Kernel and app layer 

- ➢ Hypervisor – HyperV, VMWare 

- ➢ Container Engine – Docker, Krio ➢ Hypervisor like HyperV virtualize the kernel and app layer 

- ➢ Container Engine like Docker virtualize the app layer 

- ➢ Differences: 

   - ➢ The size 

   - ➢ Bootup time 

➢ Compatibility 


Win. The Right Way. Together. 

**21** 

UniCredit - Internal Use Only 

- ➢ Container Repository – storage for containers 

- ➢ Private Repositories 

- ➢ Public Repositories – Docker Hub 


Win. The Right Way. Together. 

**22** 

UniCredit - Internal Use Only 

## ➢ **Each software app will have its have own lybery and dependencies** 

➢ Some apps needs some specific libraries versions some other apps needs a different versions  of the same library 

- ➢ Installation process is different on each environment 

- ➢ Many steps where something could go wrong 

Win. The Right Way. Together. 


**23** 

UniCredit - Internal Use Only 


➢ **Each software app will have its own libraries and dependencies** ➢ Packaged with all needed dependencies and configuration ➢ One command to install the app 


Win. The Right Way. Together. 

**24** 

UniCredit - Internal Use Only 


Win. The Right Way. Together. 


**25** 

UniCredit - Internal Use Only 


- ➢ **Layers of images** 

- ➢ Mostly Linux based because small size – Alpine Linux 

- ➢ App image on top – tomcat 

- ➢ The order of images is described in Docker File 


Win. The Right Way. Together. 

**26** 

UniCredit - Internal Use Only 


**----- Start of picture text -----**<br>
It was not Scalable<br>**----- End of picture text -----**<br>


Containers could communicate with each other Containers had to be deployed appropriately Containers had to be managed carefully Auto scaling was not possible Distributing traffic was still challenging 


Win. The Right Way. Together. 

27 

UniCredit - Internal Use Only 

- ➢ Kubernetes  is an open-source container orchestration system for automating container deployment, scaling, and management. 

- ➢ Originally designed by Google, the project is now maintained by the Cloud Native Computing Foundation. 

- ➢ It is a platform designed to completely manage the life cycle of containerized  applications and services using methods that provide predictability, scalability, and high  availability. 

Win. The Right Way. Together. 


**28** 

UniCredit - Internal Use Only 


The features of Kubernetes, are as follows: 

- **Automated Scheduling:** Kubernetes provides advanced scheduler to launch container on cluster nodes based on their resource 

- requirements and other constraints, while not sacrificing availability. 

- **Self Healing Capabilities:** Kubernetes allows to replaces and reschedules containers when nodes die. It also kills containers that don’t 

- respond to user-defined health check and doesn’t advertise them to clients until they are ready to serve. 

- **Automated rollouts & rollback:** Kubernetes rolls out changes to the application or its configuration while monitoring application health 

- to ensure it doesn’t kill all your instances at the same time. If something goes wrong, with Kubernetes you can rollback the change. 

- **Horizontal Scaling & Load Balancing:** Kubernetes can scale up and scale down the application as per the requirements with a simple 

- command, using a UI, or automatically based on CPU usage. Win. 

Win. The Right Way. Together. 

UniCredit - Internal Use Only 


Win. The Right Way. Together. 


30 

UniCredit - Internal Use Only 

AKubernetes cluster is a set of physical or virtual machines and other infrastructure resources that are needed to run your containerized applications. Each machine in a Kubernetes cluster is called a **node** . 

There are two types of node in each Kubernetes cluster: **Master node(s):** hosts the Kubernetes control plane components and manages the cluster **Worker node(s)** :runs your containerized applications 


**----- Start of picture text -----**<br>
worker worker<br>Master<br>Win.<br>The Right Way.<br>Together.<br>**----- End of picture text -----**<br>


UniCredit - Internal Use Only 

## Kubernetes Master 

- Master is responsible for managing the complete cluster. 

- You can access master node via the CLI, GUI, orAPI 

- Themaster watches over the nodes in the cluster and is responsible for the actual orchestration of containers on the worker nodes 

- For achieving fault tolerance, there can be more than one master node in the cluster. 

- It is the access point from which administrators and other users interact with the cluster to manage the scheduling and deployment of containers. 

- It has four components: ETCD,Scheduler,Controller andAPI Server 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 

## Kubernetes Master 

## ETCD 

- ETCD is a distributed reliable key-value store used by Kubernetes to store all data used to manage the cluster. 

- When you have multiple nodes and multiple masters in your cluster, etcd stores all that information on all the nodes in the cluster in a distributed manner. 

- ETCD is responsible for implementing locks within the cluster to ensure thereareno conflicts between the Masters 

## Scheduler 


- The scheduler is responsible for distributing work or containers across multiple nodes. 

- . 

- It looks for newly created containers and assigns them to Nodes 

Win. The Right Way. Together. 


UniCredit - Internal Use Only 

## Kubernetes Master 

## API server manager 

- Masters communicate with the rest of the cluster through the kube-apiserver, the main access point to the control plane. 

- It validates and executes user’s REST commands 

- kube-apiserver also makes sure that configurations in etcd match with configurations of containers deployed in the cluster. 


## Controller manager 

- The controllers arethe brain behind orchestration. 

- They are responsible for noticing and responding when nodes, containers or endpoints goes down. Thecontrollers makes decisions to bring up new containers in such cases. 

- The kube-controller-manager runs control loops that manage the state of the cluster by checking if Win. the required deployments, replicas, and nodes are running in the cluster The Right Way. 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 

## Kubernetes Master 

## Kubectl 

- kubectl is the command line utility using which we can interact with k8s cluster 

- UsesAPIs providedbyAPI server to interact. 

- Also known as the kubecommand line tool or kubectl or kubecontrol. 

- Used to deploy and manage applications on a Kubernetes 


- kubectl run nginx used to deploy an application on the cluster. 

- kubectl cluster-info used to view information about the cluster and the 

- kubectl get nodes used to list all the nodes part of the cluster. 

Win. The Right Way. Together. 


UniCredit - Internal Use Only 

## Kubernetes Worker 

## Kubelet 

- Worker nodes have the kubelet agent that is responsible for interacting with the master to provide health information of the worker node 

- Tocarry out actions requested by themaster on the worker nodes. 

## Kubeproxy 


- The kube-proxy is responsible for ensuring network traffic is routed properly to internal and external services as required and is based on the rules definedby network policies in kube-controller-manager and other custom controllers. 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 

## **Kubernetes Concepts - Namespaces** 

Namespaces are Kubernetes objects which partition a single Kubernetes cluster into multiple virtual clusters 

- Kubernetes clusters can managelargenumbers of unrelated workloads concurrently and organizationsoften choose to deploy projects createdby separateteamsto shared clusters. 

- With multiple deployments in a single cluster, thereare high chancesof deleting deployments belong to deffprohjects. 

- So namespacesallow you to group objects togetherso you can filter andcontrolthemas a unit/group. 

- Namespacesprovide a scope for names. Names of resources need to beunique within a namespace, but not across namespaces. 

- So each Kubernetes namespaceprovides the scope for Kubernetes Names itcontains;which means that using the combinationof an objectnameand a Namespace,each objectgets a unique identity across the cluster 


Win. The Right Way. Together. 

UniCredit - Internal Use Only 

## **Kubernetes Concepts - Pods** 

- Basic scheduling unit in Kubernetes. Pods areoften ephemeral 

- Kubernetes doesn’t run containers directly; instead it wraps one or more containers into a higher-level structure calleda pod 

- It is also the smallest deployableunit that can be created, schedule, and managed on a Kubernetes cluster. Each pod is assigned a unique IP address within the cluster. 

- 

- Pods can hold multiple containers as well, but you should limit yourself when possible. Because pods are scaled up and down as a unit, all containers in a pod must scale together, regardless of their individual needs. This leads to wasted resources. 


**----- Start of picture text -----**<br>
containers<br>**----- End of picture text -----**<br>


**----- Start of picture text -----**<br>
Win.<br>The Right Way.<br>Together.<br>**----- End of picture text -----**<br>


## **Kubernetes Concepts** 


Pod Networking 


UniCredit - Internal Use Only 

## **Kubernetes Concepts - Deployment** 

- ADeployment provides declarative updates for Pods 

- You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. 

- Deployment is the recommended way to deploy a pod 

- By default Kubernetes performs deployments in rolling update strategy. 

- Key features of deployment: 

   - ✓ Easily deploy a Pod 

   - ✓ Rolling updates pods 

   - ✓ Rollback to previous deployment versions 

   - ✓ Scale deployment 

   - ✓ Pause and resume deployment 


Win. The Right Way. Together. 


UniCredit - Internal Use Only 

## **Kubernetes Concepts - Services** 

- Services logically connect pods across the cluster to enable networking between them 

- Thelifetime of an individual pod cannot be relied upon; everything from their IP addresses to 

   - their very existence are prone to change. 

- Kubernetes doesn’t treat its pods as unique, long-running instances; if a pod encounters an issue and dies, it’s Kubernetes’jobto replace it so that the application doesn’t experience any downtime 

- Services makes sure that even after a pod(back-end) dies because of a failure, the newly created pods will be reached by its dependency pods(front-end) via services. In this case, front-end applications always find the backend applications via a simple service(using service name or IP address) irrespective of their location in the cluster 

- Services point to pods directly using labels. Services do not point to deployments or ReplicaSets. So, all pods with the same label gets attached to same service 

- 3 types: ClusterIP, NodePort and LoadBalancer 

Win. The Right Way. Together. 


UniCredit - Internal Use Only 

## **Kubernetes Concepts - Services** 


Pods’lifecycle are erratic; they comeand go by Kubernetes’will. 

**Not healthy? Killed. Not in theright place?Cloned, andkilled.** So how can you send a request to your application if you can’t know for sure whereit lives? Theanswerlies in **services** . 

Services are tied to the pods using pod labels and provides a stable end point for the users to reachthe application. 


When requesting your application,you don’t care about its location or about which pod answers the request. Win. 

The Right Way. Together. 

UniCredit - Internal Use Only 

## **Kubernetes Concepts - Volumes** 

- By default, container data is stored inside own its file system 

- Containers are ephemeral in nature. When they are destroyed, the data inside them gets deleted 

- Also when running multiple containers in a Pod it is often necessary to share files between those Containers 

- In order to persist data beyond the lifecycle of pod, Kubernetes provide volumes 

- Avolume can be thought of as a directory which is accessible to the containers in a pod 

- • The medium backing a volume and its contents are determined by the volume type 

## Types of Kubernetes Volumes 

- There are different types of volumes you can use in a Kubernetes pod: ❑ Node-local memory (emptyDir and hostPath) 

## Pod 


**----- Start of picture text -----**<br>
containers<br>**----- End of picture text -----**<br>


- ❑ Cloud volumes (e.g., awsElasticBlockStore, gcePersistentDisk, and azureDiskVolume) 

- ❑ File-sharing volumes, such as Network File System (NFS) ❑ Distributed-file systems (e.g., CephFS and GlusterFS) 

Win. The Right Way. Together. 

- ❑ Special volume types such as PersistentVolumeClaim, secret, configmap and gitRepo 


UniCredit - Internal Use Only 


Win. The Right Way. Together. 

**44** 

UniCredit - Internal Use Only 


Win. The Right Way. Together. 

**45** 

UniCredit - Internal Use Only 


Win. The Right Way. Together. 

**46** 

UniCredit - Internal Use Only 


Win. The Right Way. Together. 


**47** 

UniCredit - Internal Use Only 


Win. The Right Way. Together. 

**48** 

UniCredit - Internal Use Only 

Win. The Right Way. Together. 

**49** 

# **Thank You!!!** 

Win. The Right Way. Together. 


UniCredit Bulbank 

