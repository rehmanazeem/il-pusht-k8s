"""Workaround: LeRobot 0.6.1's migration crashes saving config because JSON lists
(crop_shape, down_dims, optimizer_betas) reach a config that declares tuples."""
from lerobot.processor import migrate_policy_normalization as m

_orig = m.make_policy_config
m.make_policy_config = lambda t, **kw: _orig(
    t, **{k: tuple(v) if isinstance(v, list) else v for k, v in kw.items()}
)

if __name__ == "__main__":
    m.main()
