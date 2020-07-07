'''
This is the main file for training or testing the model.
'''
import os
from argparse import ArgumentParser
from model import cycleGAN
from test import test


# parse the argument
def get_args():
    parser = ArgumentParser(description='cycleGAN PyTorch')
    parser.add_argument('--epochs', type=int, default=200)
    parser.add_argument('--decay_epoch', type=int, default=100)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--lr', type=float, default=0.0002)
    parser.add_argument('--load_height', type=int, default=158)
    parser.add_argument('--load_width', type=int, default=158)
    parser.add_argument('--gpu_ids', type=str, default='0')
    parser.add_argument('--crop_height', type=int, default=128)
    parser.add_argument('--crop_width', type=int, default=128)
    parser.add_argument('--lamda', type=int, default=10)
    parser.add_argument('--idt_coef', type=float, default=0.5)
    parser.add_argument('--training', type=bool, default=False)
    parser.add_argument('--testing', type=bool, default=False)
    parser.add_argument('--results_dir', type=str, default='CycleGAN/results')
    parser.add_argument('--dataset_dir', type=str, default='CycleGAN/datasets/horse2zebra')
    parser.add_argument('--checkpoint_dir', type=str, default='CycleGAN')
    parser.add_argument('--norm', type=str, default='instance', help='instance normalization or batch normalization')
    parser.add_argument('--no_dropout', action='store_true', help='no dropout for the generator')
    parser.add_argument('--ngf', type=int, default=64, help='# of gen filters in first conv layer')
    parser.add_argument('--ndf', type=int, default=64, help='# of discrim filters in first conv layer')
    args = parser.parse_args()
    return args


def main():
  args = get_args()

  str_ids = args.gpu_ids.split(',')
  args.gpu_ids = []
  for str_id in str_ids:
    id = int(str_id)
    if id >= 0:
      args.gpu_ids.append(id)

  print(not args.no_dropout)

  if args.training:
      print("Training")
      model = cycleGAN(args)
      model.train(args)
  if args.testing:
      print("Testing")
      test(args)


if __name__ == '__main__':
    main()