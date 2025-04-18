import argparse


def args_parser():
    parser = argparse.ArgumentParser()

    # Data
    parser.add_argument('--noniid_type', type=str, default='dirichlet',
                        help="iid or dirichlet")
    parser.add_argument('--iid', type=int, default=0,  
                        help='set 1 for iid')
    parser.add_argument('--batchsize', type=int, default=128, 
                        help="batchsize")
    parser.add_argument('--validate_batchsize', type=int, default=128, 
                        help="batchsize")
    parser.add_argument('--dirichlet_alpha', type=float, default=0.5, 
                    help="dirichlet_alpha")
    parser.add_argument('--dirichlet_alpha2', type=float, default=False, 
                    help="dirichlet_alpha2")
    parser.add_argument('--longtail_proxyset', type=str, default='none',
                    help="longtail_proxyset")
    parser.add_argument('--longtail_clients', type=str, default='none', 
                    help="longtail_clients")

    # System
    parser.add_argument('--device', type=str, default='0',
                        help="device: {cuda, cpu}")
    

    


    
    parser.add_argument('--node_num', type=int, default=20, # 200
                        help="Number of nodes")
    parser.add_argument('--T', type=int, default=300,  # 100 
                        help="Number of communication rounds")
    parser.add_argument('--E', type=int, default=1, # 3
                        help="Number of local epochs: E")
    parser.add_argument('--dataset', type=str, default='cifar100',
                        help="Type of algorithms:{mnist, cifar10,cifar100, fmnist}") 
    parser.add_argument('--select_ratio', type=float, default=1,
                    help="the ratio of client selection in each round")
    parser.add_argument('--local_model', type=str, default='ResNet20',
                        help='Type of local model: {CNN, ResNet20, AlexNet,LeNet5}')
    parser.add_argument('--random_seed', type=int, default=10,
                        help="random seed for the whole experiment")
    parser.add_argument('--exp_name', type=str, default='FirstTable',
                        help="experiment name")
    


    # Server function
    parser.add_argument('--server_method', type=str, default='fedawa', 
                        help="fedavg, fedawa")
    parser.add_argument('--server_valid_ratio', type=float, default=0.02, 
                    help="the ratio of validate set (proxy dataset) in the central server")
    parser.add_argument('--server_epochs', type=int, default=1,
                        help="optimizer epochs on server")
    parser.add_argument('--server_optimizer', type=str, default='adam',
                        help="type of server optimizer, adam or sgd")
    parser.add_argument('--gamma', type=float, default=1.0,
                        help="vector_scale")
    parser.add_argument('--reg_distance', type=str, default='cos',
                        help="cos or euc")

                        
    # Client function
    parser.add_argument('--client_method', type=str, default='local_train',
                        help="local_train, fedprox")
    parser.add_argument('--optimizer', type=str, default='sgd',
                        help="optimizer: {sgd, adam}")
    parser.add_argument('--client_valid_ratio', type=float, default=0.3,
                    help="the ratio of validate set in the clients")  
    parser.add_argument('--lr', type=float, default=0.08,
                        help='clients loca learning rate')
    parser.add_argument('--local_wd_rate', type=float, default=5e-4,
                        help='clients local wd rate')
    parser.add_argument('--momentum', type=float, default=0.9,
                        help='clients SGD momentum')
    parser.add_argument('--mu', type=float, default=0.001,
                        help="clients proximal term mu for FedProx")

    args = parser.parse_args()

    return args
