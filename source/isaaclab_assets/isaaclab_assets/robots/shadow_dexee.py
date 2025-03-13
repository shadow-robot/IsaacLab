# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the dexee hand from Shadow Robot.

The following configurations are available:

* :obj:`SHADOW_DEXEE_HAND_CFG`: Shadow Hand with implicit actuator model.

Reference:

* https://www.shadowrobot.com/dexterous-hand-series/

"""


import isaaclab.sim as sim_utils
from isaaclab.actuators.actuator_cfg import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
# from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

##
# Configuration
##

SHADOW_DEXEE_HAND_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/workspace/isaaclab/source/isaaclab_assets/data/Robots/shadow_dexee/shadow_dexee.usd",
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=True,
            retain_accelerations=True,
            max_depenetration_velocity=1000.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.0005,
            fix_root_link=True,
        ),
        
        # collision_props=sim_utils.CollisionPropertiesCfg(contact_offset=0.005, rest_offset=0.0),
        joint_drive_props=sim_utils.JointDrivePropertiesCfg(drive_type="force"),
        # fixed_tendons_props=sim_utils.FixedTendonPropertiesCfg(limit_stiffness=30.0, damping=0.1),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        # rot=(0.0, 0.0, -0.7071, 0.7071),
        joint_pos={".*": 0.0},
    ),
    actuators={
        "fingers": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            effort_limit={
                "F(0|1|2)_J0": 1.5,
                "F(0|1|2)_J1": 1.2,
                "F(0|1|2)_J2": 0.7,
                "F(0|1|2)_J3": 0.35,
            },
            stiffness={
                "F(0|1|2)_J0": 2.8,
                "F(0|1|2)_J1": 2.5,
                "F(0|1|2)_J2": 1.1,
                "F(0|1|2)_J3": 0.6,
            },
            damping={
                "F(0|1|2)_J0": 0.03,
                "F(0|1|2)_J1": 0.02,
                "F(0|1|2)_J2": 0.01,
                "F(0|1|2)_J3": 0.008,
            },
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)
"""Configuration of Shadow Dexee robot."""
