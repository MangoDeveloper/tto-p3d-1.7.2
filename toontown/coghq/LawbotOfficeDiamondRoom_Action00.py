# 2013.08.22 22:19:09 Pacific Daylight Time
# Embedded file name: toontown.coghq.LawbotOfficeDiamondRoom_Action00
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone13a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 10005: {'type': 'attribModifier',
         'name': 'stomperDamage',
         'comment': '',
         'parentEntId': 0,
         'attribName': 'damage',
         'recursive': 1,
         'typeName': 'stomper',
         'value': '10'},
 10009: {'type': 'attribModifier',
         'name': 'spotlightDamage',
         'comment': '',
         'parentEntId': 0,
         'attribName': 'damPow',
         'recursive': 1,
         'typeName': 'securityCamera',
         'value': '10'},
 10032: {'type': 'attribModifier',
         'name': 'radius',
         'comment': '',
         'parentEntId': 10059,
         'attribName': 'radius',
         'recursive': 1,
         'typeName': 'securityCamera',
         'value': '7'},
 10036: {'type': 'attribModifier',
         'name': 'accel',
         'comment': '',
         'parentEntId': 10059,
         'attribName': 'accel',
         'recursive': 1,
         'typeName': 'securityCamera',
         'value': '2'},
 10066: {'type': 'attribModifier',
         'name': 'maxVel',
         'comment': '',
         'parentEntId': 10059,
         'attribName': 'maxVel',
         'recursive': 1,
         'typeName': 'securityCamera',
         'value': '10'},
 10000: {'type': 'nodepath',
         'name': 'front',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-80, -1.5, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10001: {'type': 'nodepath',
         'name': 'left',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 40, 0.05),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10002: {'type': 'nodepath',
         'name': 'right',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, -40, 0.05),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10003: {'type': 'nodepath',
         'name': 'back',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(80, 0, 0.05),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1)},
 10007: {'type': 'nodepath',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10006,
         'pos': Point3(0, -10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10008: {'type': 'nodepath',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10006,
         'pos': Point3(0, 10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10011: {'type': 'nodepath',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10010,
         'pos': Point3(0, 10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10012: {'type': 'nodepath',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10010,
         'pos': Point3(0, -10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10017: {'type': 'nodepath',
         'name': 'stompers',
         'comment': '',
         'parentEntId': 10000,
         'pos': Point3(0, -6, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10019: {'type': 'nodepath',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10018,
         'pos': Point3(0, 10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10020: {'type': 'nodepath',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10018,
         'pos': Point3(0, -10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10021: {'type': 'nodepath',
         'name': 'leftFront',
         'comment': '',
         'parentEntId': 10001,
         'pos': Point3(-29.5779, 0, 0),
         'hpr': Point3(27, 0, 0),
         'scale': Vec3(1, 1, 1)},
 10026: {'type': 'nodepath',
         'name': 'projectors',
         'comment': '',
         'parentEntId': 10021,
         'pos': Point3(-15, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10027: {'type': 'nodepath',
         'name': 'left',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(0, 8, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10028: {'type': 'nodepath',
         'name': 'middle',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(0, -15, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10029: {'type': 'nodepath',
         'name': 'right',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(0, -28, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10031: {'type': 'nodepath',
         'name': 'nodepaths',
         'comment': '',
         'parentEntId': 10057,
         'pos': Point3(0, -2, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10033: {'type': 'nodepath',
         'name': 'backLeft',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(0, 20, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10034: {'type': 'nodepath',
         'name': 'backCenter',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1)},
 10035: {'type': 'nodepath',
         'name': 'backRight',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(0, -20, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10037: {'type': 'nodepath',
         'name': 'rightFront',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(-20.7505, 15.0698, 0),
         'hpr': Point3(333, 0, 0),
         'scale': Vec3(1, 1, 1)},
 10038: {'type': 'nodepath',
         'name': 'projectors',
         'comment': '',
         'parentEntId': 10037,
         'pos': Point3(-15, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10043: {'type': 'nodepath',
         'name': 'left',
         'comment': '',
         'parentEntId': 10038,
         'pos': Point3(0, 8, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10044: {'type': 'nodepath',
         'name': 'middle',
         'comment': '',
         'parentEntId': 10038,
         'pos': Point3(0, -15, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10045: {'type': 'nodepath',
         'name': 'frontLeft',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(-15, 20, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10046: {'type': 'nodepath',
         'name': 'frontCenter',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(-15, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10047: {'type': 'nodepath',
         'name': 'frontRight',
         'comment': '',
         'parentEntId': 10031,
         'pos': Point3(-15, -20, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10048: {'type': 'nodepath',
         'name': 'right',
         'comment': '',
         'parentEntId': 10038,
         'pos': Point3(0, -28, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10049: {'type': 'nodepath',
         'name': 'rightBack',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(20, 4, 0),
         'hpr': Point3(21, 0, 0),
         'scale': 1},
 10050: {'type': 'nodepath',
         'name': 'leftBack',
         'comment': '',
         'parentEntId': 10001,
         'pos': Point3(20, -7, 0),
         'hpr': Point3(334, 0, 0),
         'scale': 1},
 10057: {'type': 'nodepath',
         'name': 'discoFloor',
         'comment': '',
         'parentEntId': 10003,
         'pos': Point3(36.354, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1)},
 10059: {'type': 'nodepath',
         'name': 'cameras',
         'comment': '',
         'parentEntId': 10057,
         'pos': Point3(-7, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10006: {'type': 'securityCamera',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10000,
         'pos': Point3(15, 15, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'accel': 5.0,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 15.0,
         'modelPath': 0,
         'projector': Point3(6, 6, 25),
         'radius': 5,
         'switchId': 0,
         'trackTarget1': 10007,
         'trackTarget2': 10008,
         'trackTarget3': 0},
 10010: {'type': 'securityCamera',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10000,
         'pos': Point3(15, -15, 0),
         'hpr': Point3(180, 0, 0),
         'scale': 1,
         'accel': 5.0,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 15.0,
         'modelPath': 0,
         'projector': Point3(6, 6, 25),
         'radius': 5,
         'switchId': 0,
         'trackTarget1': 10011,
         'trackTarget2': 10012,
         'trackTarget3': 0},
 10018: {'type': 'securityCamera',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10000,
         'pos': Point3(15, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'accel': 1,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 5,
         'modelPath': 0,
         'projector': Point3(6, 6, 25),
         'radius': 5,
         'switchId': 0,
         'trackTarget1': 10019,
         'trackTarget2': 10020,
         'trackTarget3': 0},
 10024: {'type': 'securityCamera',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'accel': 1,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 5,
         'modelPath': 0,
         'projector': Point3(6, 6, 25),
         'radius': 5,
         'switchId': 0,
         'trackTarget1': 10027,
         'trackTarget2': 10028,
         'trackTarget3': 0},
 10025: {'type': 'securityCamera',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10026,
         'pos': Point3(0, -20, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'accel': 1,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 5,
         'modelPath': 0,
         'projector': Point3(6, 6, 25),
         'radius': 5,
         'switchId': 0,
         'trackTarget1': 10028,
         'trackTarget2': 10029,
         'trackTarget3': 0},
 10041: {'type': 'securityCamera',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10038,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'accel': 1,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 5,
         'modelPath': 0,
         'projector': Point3(6, 6, 25),
         'radius': 5,
         'switchId': 0,
         'trackTarget1': 10043,
         'trackTarget2': 10044,
         'trackTarget3': 0},
 10042: {'type': 'securityCamera',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10038,
         'pos': Point3(0, -20, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'accel': 1,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 5,
         'modelPath': 0,
         'projector': Point3(6, 6, 25),
         'radius': 5,
         'switchId': 0,
         'trackTarget1': 10044,
         'trackTarget2': 10048,
         'trackTarget3': 0},
 10060: {'type': 'securityCamera',
         'name': 'backRow',
         'comment': '',
         'parentEntId': 10059,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'accel': 2,
         'damPow': 10,
         'hideModel': 0,
         'maxVel': 10,
         'modelPath': 0,
         'projector': Point3(0, 0, 25),
         'radius': 7,
         'switchId': 0,
         'trackTarget1': 10033,
         'trackTarget2': 10034,
         'trackTarget3': 0},
 10062: {'type': 'securityCamera',
         'name': 'frontRow',
         'comment': '',
         'parentEntId': 10059,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'accel': 2,
         'damPow': 10,
         'hideModel': 1,
         'maxVel': 10,
         'modelPath': 0,
         'projector': Point3(0, 0, 25),
         'radius': 7,
         'switchId': 0,
         'trackTarget1': 10045,
         'trackTarget2': 10046,
         'trackTarget3': 0},
 10063: {'type': 'securityCamera',
         'name': 'backRow2',
         'comment': '',
         'parentEntId': 10059,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'accel': 2,
         'damPow': 10,
         'hideModel': 1,
         'maxVel': 10,
         'modelPath': 0,
         'projector': Point3(0, 0, 25),
         'radius': 7,
         'switchId': 0,
         'trackTarget1': 0,
         'trackTarget2': 10034,
         'trackTarget3': 10035},
 10065: {'type': 'securityCamera',
         'name': 'frontRow2',
         'comment': '',
         'parentEntId': 10059,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'accel': 2,
         'damPow': 10,
         'hideModel': 1,
         'maxVel': 10,
         'modelPath': 0,
         'projector': Point3(0, 0, 25),
         'radius': 7,
         'switchId': 0,
         'trackTarget1': 0,
         'trackTarget2': 10046,
         'trackTarget3': 10047},
 10004: {'type': 'stomper',
         'name': '3',
         'comment': '',
         'parentEntId': 10017,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 2.0,
         'phaseShift': 0.25,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10013: {'type': 'stomper',
         'name': '2',
         'comment': '',
         'parentEntId': 10017,
         'pos': Point3(0, 12.5, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 2.0,
         'phaseShift': 0.5,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10014: {'type': 'stomper',
         'name': '1',
         'comment': '',
         'parentEntId': 10017,
         'pos': Point3(0, 25, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 2.0,
         'phaseShift': 0.0,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10015: {'type': 'stomper',
         'name': 'copy of 4 (2)',
         'comment': '',
         'parentEntId': 10049,
         'pos': Point3(0, -10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10016: {'type': 'stomper',
         'name': '4',
         'comment': '',
         'parentEntId': 10017,
         'pos': Point3(0, -12.5, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 2.0,
         'phaseShift': 0.75,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10022: {'type': 'stomper',
         'name': 'copy of 3',
         'comment': '',
         'parentEntId': 10021,
         'pos': Point3(0, 0, 0),
         'hpr': Point3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(10, 6, 10),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.0,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10023: {'type': 'stomper',
         'name': 'copy of 3 (2)',
         'comment': '',
         'parentEntId': 10021,
         'pos': Point3(0, -20, 0),
         'hpr': Point3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(10, 6, 10),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.4,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10030: {'type': 'stomper',
         'name': 'copy of 4 (3)',
         'comment': '',
         'parentEntId': 10049,
         'pos': Point3(10, 10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10039: {'type': 'stomper',
         'name': 'copy of 3',
         'comment': '',
         'parentEntId': 10037,
         'pos': Point3(0, 0, 0),
         'hpr': Point3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(10, 6, 10),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.0,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10040: {'type': 'stomper',
         'name': 'copy of 3 (2)',
         'comment': '',
         'parentEntId': 10037,
         'pos': Point3(0, -20, 0),
         'hpr': Point3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(10, 6, 10),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.4,
         'range': 6,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10051: {'type': 'stomper',
         'name': 'copy of 4 (4)',
         'comment': '',
         'parentEntId': 10049,
         'pos': Point3(20, -5, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10052: {'type': 'stomper',
         'name': 'copy of 4 (5)',
         'comment': '',
         'parentEntId': 10049,
         'pos': Point3(35, 10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10053: {'type': 'stomper',
         'name': 'copy of 4',
         'comment': '',
         'parentEntId': 10050,
         'pos': Point3(0, -10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1,
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10054: {'type': 'stomper',
         'name': 'copy of 4 (2)',
         'comment': '',
         'parentEntId': 10050,
         'pos': Point3(10, 10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10055: {'type': 'stomper',
         'name': 'copy of 4 (3)',
         'comment': '',
         'parentEntId': 10050,
         'pos': Point3(20, -5, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10056: {'type': 'stomper',
         'name': 'copy of 4 (4)',
         'comment': '',
         'parentEntId': 10050,
         'pos': Point3(35, 10, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': Vec3(1, 1, 1),
         'animateShadow': 1,
         'cogStyle': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 5),
         'modelPath': 0,
         'motion': 3,
         'period': 4.0,
         'phaseShift': 0.75,
         'range': 30.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 0,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 0,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\coghq\LawbotOfficeDiamondRoom_Action00.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:19:09 Pacific Daylight Time
