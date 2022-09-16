def fea_analysis(l, w, t, f):
    """FEA solution for plate subject to a central load"""
    res = l + w - t*f
    return res


import argparse
parser = argparse.ArgumentParser()

# Cast input to float, with a default value; maps to FORCE
parser.add_argument('-F', '--FORCE', type=float, required=True)

# Cast input to float, with a default value; maps to WIDTH
parser.add_argument('-W', '--WIDTH', type=float, default=1.0)

# Cast input to float, with a default value; maps to LENGTH
parser.add_argument('-L', '--LENGTH', type=float, default=5.0)

# Cast input to float, with a default value; maps to THICKNESS
parser.add_argument('-T', '--THICKNESS', type=float, default=0.01)

args = parser.parse_args()
stress_value = fea_analysis(args.LENGTH, args.WIDTH, args.THICKNESS, args.FORCE)
print(stress_value)