import argparse
from ast import arg
import util.host

def cli():
    parser = argparse.ArgumentParser(description='ai-teller is a program to tell you your future')
    subparsers = parser.add_subparsers(metavar='subcommand')

    # config command and its arguments
    config_command = subparsers.add_parser('config', help='生成默认配置文件')
    config_command.set_defaults(handle=handle_config)

    # server command and its arguments
    server_command = subparsers.add_parser("server", help="启动服务器")
    server_command.add_argument('-p', '--port', type=int, default=9870, required=True, help='端口')
    server_command.set_defaults(handle=handle_server)

    migrate_command= subparsers.add_parser("migrate",help="迁移数据")
    migrate_command.add_argument('-src', '--source', type= str,default='ikk', required= True, help ='数据源')
    migrate_command.add_argument('-dst', '--destination', type= str, default= 'fgh', required= True, help = '目的端')
    migrate_command.set_defaults(handle = handle_migrate)

    args = parser.parse_args()
    if hasattr(args, 'handle'):
        args.handle(args)
    else:
        parser.print_help()

def handle_migrate(args):
    print('migrate data come source to destination')

def handle_config(args):
    print('config will generate a default config file')

def handle_server(args):
    print('server will start a server')
    ip = util.host.get_host_ip()
    print('server will listen on ip:', ip)
    print('server will listen on port:', args.port)

if __name__ == '__main__':
    cli()
