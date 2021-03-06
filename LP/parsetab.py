
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AT CM EQ FROM GT ID LP LT NE OR RP SELECT WHEREsqlstg : SELECT field FROM body\n  field : AT\n           | ID\n           | morefield \n  morefield : ID \n               | ID CM morefield\n  body : ID\n          | ID WHERE wbody\n  wbody : cond\n           | cond op wbody\n  cond : ID comp ID\n          | LP wbody RP\n  op : AND\n        | OR\n  comp : EQ\n          | NE\n          | GT\n          | LT\n  '
    
_lr_action_items = {'SELECT':([0,],[2,]),'$end':([1,9,10,15,16,27,28,29,],[0,-1,-7,-8,-9,-11,-10,-12,]),'AT':([2,],[4,]),'ID':([2,7,8,13,17,18,19,20,21,22,23,24,25,],[5,10,11,14,14,27,-15,-16,-17,-18,14,-13,-14,]),'FROM':([3,4,5,6,11,12,],[7,-2,-3,-4,-5,-6,]),'CM':([5,11,],[8,8,]),'WHERE':([10,],[13,]),'LP':([13,17,23,24,25,],[17,17,17,-13,-14,]),'EQ':([14,],[19,]),'NE':([14,],[20,]),'GT':([14,],[21,]),'LT':([14,],[22,]),'RP':([16,26,27,28,29,],[-9,29,-11,-10,-12,]),'AND':([16,27,29,],[24,-11,-12,]),'OR':([16,27,29,],[25,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sqlstg':([0,],[1,]),'field':([2,],[3,]),'morefield':([2,8,],[6,12,]),'body':([7,],[9,]),'wbody':([13,17,23,],[15,26,28,]),'cond':([13,17,23,],[16,16,16,]),'comp':([14,],[18,]),'op':([16,],[23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sqlstg","S'",1,None,None,None),
  ('sqlstg -> SELECT field FROM body','sqlstg',4,'p_sqlstg','lexyacc.py',63),
  ('field -> AT','field',1,'p_field','lexyacc.py',67),
  ('field -> ID','field',1,'p_field','lexyacc.py',68),
  ('field -> morefield','field',1,'p_field','lexyacc.py',69),
  ('morefield -> ID','morefield',1,'p_morefield','lexyacc.py',73),
  ('morefield -> ID CM morefield','morefield',3,'p_morefield','lexyacc.py',74),
  ('body -> ID','body',1,'p_body','lexyacc.py',78),
  ('body -> ID WHERE wbody','body',3,'p_body','lexyacc.py',79),
  ('wbody -> cond','wbody',1,'p_wbody','lexyacc.py',83),
  ('wbody -> cond op wbody','wbody',3,'p_wbody','lexyacc.py',84),
  ('cond -> ID comp ID','cond',3,'p_cond','lexyacc.py',88),
  ('cond -> LP wbody RP','cond',3,'p_cond','lexyacc.py',89),
  ('op -> AND','op',1,'p_op','lexyacc.py',93),
  ('op -> OR','op',1,'p_op','lexyacc.py',94),
  ('comp -> EQ','comp',1,'p_comp','lexyacc.py',98),
  ('comp -> NE','comp',1,'p_comp','lexyacc.py',99),
  ('comp -> GT','comp',1,'p_comp','lexyacc.py',100),
  ('comp -> LT','comp',1,'p_comp','lexyacc.py',101),
]
