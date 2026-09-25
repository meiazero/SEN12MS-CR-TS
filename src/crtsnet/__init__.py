"""CR-TS Net generator as an installable package: `crtsnet.networks_branched.define_G`.

Every other module here is a symlink to the unchanged upstream file in `models/` (the
networks and what they import), so the package holds the network only, without the training
scripts' dependencies, which stay in the `scripts` dependency group.
"""
