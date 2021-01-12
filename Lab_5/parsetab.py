
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSEnonassoc=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNnonassoc<>LTEGTEEQNEQnonassoc:left+-DOTADDDOTSUBleft*/DOTMULDOTDIVrightUMINUSleft\'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GTE ID IF INTNUM LTE MULASSIGN NEQ ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructionsinstructions : instructions instructioninstructions : instruction : \'{\' instructions \'}\'instruction : IF \'(\' condition \')\' instruction %prec IFXinstruction : IF \'(\' condition \')\' instruction ELSE instructioninstruction : FOR variable \'=\' range instructioninstruction : WHILE \'(\' condition \')\' instructioncondition : expression EQ expression\n                 | expression NEQ expression\n                 | expression LTE expression\n                 | expression GTE expression\n                 | expression \'<\' expression\n                 | expression \'>\' expressionvariable : IDrange : expression \':\' expressioninstruction : statement \';\'statement : BREAKstatement : CONTINUEstatement : RETURNstatement : RETURN expressionstatement : PRINT expression_liststatement : lvalue \'=\' expression\n                 | lvalue ADDASSIGN expression\n                 | lvalue SUBASSIGN expression\n                 | lvalue MULASSIGN expression\n                 | lvalue DIVASSIGN expressionlvalue : variablelvalue : variable \'[\' expression_list \']\'expression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expression\n                  | expression DOTADD expression\n                  | expression DOTSUB expression\n                  | expression DOTMUL expression\n                  | expression DOTDIV expressionexpression : \'-\' expression %prec UMINUSexpression : expression "\'" expression : \'(\' expression \')\'expression : lvalueexpression : rangeexpression : INTNUMexpression : FLOATNUMexpression : STRINGexpression_list : expression_list \',\' expressionexpression_list : expressionexpression_list : expression : \'[\' expression_list \']\'expression : EYE \'(\' expression \')\'expression : EYE \'(\' expression \',\' expression \')\'expression : ZEROS \'(\' expression \')\'expression : ZEROS \'(\' expression \',\' expression \')\'expression : ONES \'(\' expression \')\'expression : ONES \'(\' expression \',\' expression \')\''
    
_lr_action_items = {'{':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,4,-2,-3,-28,-15,4,-17,-41,-42,-43,-44,-45,-4,-39,-38,4,4,-29,4,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,4,-6,-51,-53,-55,]),'IF':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,5,-2,-3,-28,-15,5,-17,-41,-42,-43,-44,-45,-4,-39,-38,5,5,-29,5,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,5,-6,-51,-53,-55,]),'FOR':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,6,-2,-3,-28,-15,6,-17,-41,-42,-43,-44,-45,-4,-39,-38,6,6,-29,6,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,6,-6,-51,-53,-55,]),'WHILE':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,8,-2,-3,-28,-15,8,-17,-41,-42,-43,-44,-45,-4,-39,-38,8,8,-29,8,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,8,-6,-51,-53,-55,]),'BREAK':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,10,-2,-3,-28,-15,10,-17,-41,-42,-43,-44,-45,-4,-39,-38,10,10,-29,10,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,10,-6,-51,-53,-55,]),'CONTINUE':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,11,-2,-3,-28,-15,11,-17,-41,-42,-43,-44,-45,-4,-39,-38,11,11,-29,11,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,11,-6,-51,-53,-55,]),'RETURN':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,12,-2,-3,-28,-15,12,-17,-41,-42,-43,-44,-45,-4,-39,-38,12,12,-29,12,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,12,-6,-51,-53,-55,]),'PRINT':([0,2,3,4,7,15,16,21,25,26,27,28,29,41,55,57,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,106,108,110,114,115,116,117,],[-3,13,-2,-3,-28,-15,13,-17,-41,-42,-43,-44,-45,-4,-39,-38,13,13,-29,13,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,-52,-54,13,-6,-51,-53,-55,]),'ID':([0,2,3,4,6,7,12,13,15,16,17,19,20,21,23,24,25,26,27,28,29,30,36,37,38,39,40,41,44,47,48,49,50,51,52,53,54,55,56,57,60,61,62,63,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,95,102,103,104,105,106,107,108,109,110,114,115,116,117,],[-3,15,-2,-3,15,-28,15,15,-15,15,15,15,15,-17,15,15,-41,-42,-43,-44,-45,15,15,15,15,15,15,-4,15,15,15,15,15,15,15,15,15,-39,15,-38,15,15,15,15,15,15,15,15,15,15,15,15,-29,15,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-5,-7,-8,-50,15,-52,15,-54,15,15,-6,-51,-53,-55,]),'$end':([0,1,2,3,21,41,95,102,103,114,],[-3,0,-1,-2,-17,-4,-5,-7,-8,-6,]),'}':([3,4,16,21,41,95,102,103,114,],[-2,-3,41,-17,-4,-5,-7,-8,-6,]),'(':([5,8,12,13,17,19,20,23,24,30,31,32,33,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[17,20,24,24,24,24,24,24,24,24,60,61,62,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'=':([7,14,15,18,78,],[-28,36,-15,44,-29,]),'ADDASSIGN':([7,14,15,78,],[-28,37,-15,-29,]),'SUBASSIGN':([7,14,15,78,],[-28,38,-15,-29,]),'MULASSIGN':([7,14,15,78,],[-28,39,-15,-29,]),'DIVASSIGN':([7,14,15,78,],[-28,40,-15,-29,]),'+':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,47,-41,-42,-43,-44,-45,47,47,-39,-38,47,47,47,47,47,47,-42,47,-29,-30,-31,-32,-33,-34,-35,-36,-37,47,-40,-49,47,47,47,47,47,47,47,47,47,47,-50,-52,-54,47,47,47,-51,-53,-55,]),'-':([7,12,13,15,17,19,20,22,23,24,25,26,27,28,29,30,35,36,37,38,39,40,43,44,47,48,49,50,51,52,53,54,55,56,57,58,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,105,106,107,108,109,111,112,113,115,116,117,],[-28,23,23,-15,23,23,23,48,23,23,-41,-42,-43,-44,-45,23,48,23,23,23,23,23,48,23,23,23,23,23,23,23,23,23,-39,23,-38,48,23,23,23,23,48,48,48,48,48,23,23,23,23,23,23,-42,48,-29,-30,-31,-32,-33,-34,-35,-36,-37,48,-40,-49,48,48,48,48,48,48,48,48,48,48,-50,23,-52,23,-54,23,48,48,48,-51,-53,-55,]),'*':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,49,-41,-42,-43,-44,-45,49,49,-39,-38,49,49,49,49,49,49,-42,49,-29,49,49,-32,-33,49,49,-36,-37,49,-40,-49,49,49,49,49,49,49,49,49,49,49,-50,-52,-54,49,49,49,-51,-53,-55,]),'/':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,50,-41,-42,-43,-44,-45,50,50,-39,-38,50,50,50,50,50,50,-42,50,-29,50,50,-32,-33,50,50,-36,-37,50,-40,-49,50,50,50,50,50,50,50,50,50,50,-50,-52,-54,50,50,50,-51,-53,-55,]),'DOTADD':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,51,-41,-42,-43,-44,-45,51,51,-39,-38,51,51,51,51,51,51,-42,51,-29,-30,-31,-32,-33,-34,-35,-36,-37,51,-40,-49,51,51,51,51,51,51,51,51,51,51,-50,-52,-54,51,51,51,-51,-53,-55,]),'DOTSUB':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,52,-41,-42,-43,-44,-45,52,52,-39,-38,52,52,52,52,52,52,-42,52,-29,-30,-31,-32,-33,-34,-35,-36,-37,52,-40,-49,52,52,52,52,52,52,52,52,52,52,-50,-52,-54,52,52,52,-51,-53,-55,]),'DOTMUL':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,53,-41,-42,-43,-44,-45,53,53,-39,-38,53,53,53,53,53,53,-42,53,-29,53,53,-32,-33,53,53,-36,-37,53,-40,-49,53,53,53,53,53,53,53,53,53,53,-50,-52,-54,53,53,53,-51,-53,-55,]),'DOTDIV':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,54,-41,-42,-43,-44,-45,54,54,-39,-38,54,54,54,54,54,54,-42,54,-29,54,54,-32,-33,54,54,-36,-37,54,-40,-49,54,54,54,54,54,54,54,54,54,54,-50,-52,-54,54,54,54,-51,-53,-55,]),"'":([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,55,-41,-42,-43,-44,-45,55,55,-39,55,55,55,55,55,55,55,-42,55,-29,55,55,55,55,55,55,55,55,55,-40,-49,55,55,55,55,55,55,55,55,55,55,-50,-52,-54,55,55,55,-51,-53,-55,]),':':([7,15,22,25,26,27,28,29,35,43,55,57,58,64,65,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,56,-41,-42,-43,-44,-45,56,56,-39,-38,56,56,56,56,56,56,-42,56,-29,-30,-31,-32,-33,-34,-35,-36,-37,None,-40,-49,56,56,56,56,56,56,56,56,56,56,-50,-52,-54,56,56,56,-51,-53,-55,]),';':([7,9,10,11,12,13,15,22,25,26,27,28,29,34,35,55,57,64,65,66,67,68,78,80,81,82,83,84,85,86,87,88,89,90,94,104,106,108,115,116,117,],[-28,21,-18,-19,-20,-48,-15,-21,-41,-42,-43,-44,-45,-22,-47,-39,-38,-23,-24,-25,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-46,-50,-52,-54,-51,-53,-55,]),',':([7,13,15,19,25,26,27,28,29,30,34,35,45,55,57,59,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,108,115,116,117,],[-28,-48,-15,-48,-41,-42,-43,-44,-45,-48,63,-47,63,-39,-38,63,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,105,107,109,-46,-50,-52,-54,-51,-53,-55,]),'EQ':([7,15,25,26,27,28,29,43,55,57,78,80,81,82,83,84,85,86,87,88,89,90,104,106,108,115,116,117,],[-28,-15,-41,-42,-43,-44,-45,70,-39,-38,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-50,-52,-54,-51,-53,-55,]),'NEQ':([7,15,25,26,27,28,29,43,55,57,78,80,81,82,83,84,85,86,87,88,89,90,104,106,108,115,116,117,],[-28,-15,-41,-42,-43,-44,-45,71,-39,-38,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-50,-52,-54,-51,-53,-55,]),'LTE':([7,15,25,26,27,28,29,43,55,57,78,80,81,82,83,84,85,86,87,88,89,90,104,106,108,115,116,117,],[-28,-15,-41,-42,-43,-44,-45,72,-39,-38,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-50,-52,-54,-51,-53,-55,]),'GTE':([7,15,25,26,27,28,29,43,55,57,78,80,81,82,83,84,85,86,87,88,89,90,104,106,108,115,116,117,],[-28,-15,-41,-42,-43,-44,-45,73,-39,-38,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-50,-52,-54,-51,-53,-55,]),'<':([7,15,25,26,27,28,29,43,55,57,78,80,81,82,83,84,85,86,87,88,89,90,104,106,108,115,116,117,],[-28,-15,-41,-42,-43,-44,-45,74,-39,-38,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-50,-52,-54,-51,-53,-55,]),'>':([7,15,25,26,27,28,29,43,55,57,78,80,81,82,83,84,85,86,87,88,89,90,104,106,108,115,116,117,],[-28,-15,-41,-42,-43,-44,-45,75,-39,-38,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-50,-52,-54,-51,-53,-55,]),']':([7,15,19,25,26,27,28,29,30,35,45,55,57,59,78,80,81,82,83,84,85,86,87,88,89,90,94,104,106,108,115,116,117,],[-28,-15,-48,-41,-42,-43,-44,-45,-48,-47,78,-39,-38,90,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,-46,-50,-52,-54,-51,-53,-55,]),')':([7,15,25,26,27,28,29,42,46,55,57,58,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,97,98,99,100,101,104,106,108,111,112,113,115,116,117,],[-28,-15,-41,-42,-43,-44,-45,69,79,-39,-38,89,-29,-30,-31,-32,-33,-34,-35,-36,-37,-16,-40,-49,104,106,108,-9,-10,-11,-12,-13,-14,-50,-52,-54,115,116,117,-51,-53,-55,]),'[':([7,12,13,15,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[19,30,30,-15,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'INTNUM':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'FLOATNUM':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'STRING':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'EYE':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'ZEROS':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'ONES':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'ELSE':([21,41,95,102,103,114,],[-17,-4,110,-7,-8,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions':([0,4,],[2,16,]),'instruction':([2,16,69,76,79,110,],[3,3,95,102,103,114,]),'variable':([2,6,12,13,16,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,69,70,71,72,73,74,75,76,79,105,107,109,110,],[7,18,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'statement':([2,16,69,76,79,110,],[9,9,9,9,9,9,]),'lvalue':([2,12,13,16,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,69,70,71,72,73,74,75,76,79,105,107,109,110,],[14,25,25,14,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,14,25,25,25,25,25,25,14,14,25,25,25,14,]),'expression':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[22,35,43,35,43,57,58,35,64,65,66,67,68,77,80,81,82,83,84,85,86,87,88,91,92,93,94,96,97,98,99,100,101,111,112,113,]),'range':([12,13,17,19,20,23,24,30,36,37,38,39,40,44,47,48,49,50,51,52,53,54,56,60,61,62,63,70,71,72,73,74,75,105,107,109,],[26,26,26,26,26,26,26,26,26,26,26,26,26,76,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'expression_list':([13,19,30,],[34,45,59,]),'condition':([17,20,],[42,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','Mparser.py',29),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Mparser.py',33),
  ('instructions -> <empty>','instructions',0,'p_instructions_empty','Mparser.py',37),
  ('instruction -> { instructions }','instruction',3,'p_instruction_block','Mparser.py',41),
  ('instruction -> IF ( condition ) instruction','instruction',5,'p_instruction_if','Mparser.py',49),
  ('instruction -> IF ( condition ) instruction ELSE instruction','instruction',7,'p_instruction_if_else','Mparser.py',53),
  ('instruction -> FOR variable = range instruction','instruction',5,'p_instruction_for','Mparser.py',57),
  ('instruction -> WHILE ( condition ) instruction','instruction',5,'p_instruction_while','Mparser.py',61),
  ('condition -> expression EQ expression','condition',3,'p_condition','Mparser.py',65),
  ('condition -> expression NEQ expression','condition',3,'p_condition','Mparser.py',66),
  ('condition -> expression LTE expression','condition',3,'p_condition','Mparser.py',67),
  ('condition -> expression GTE expression','condition',3,'p_condition','Mparser.py',68),
  ('condition -> expression < expression','condition',3,'p_condition','Mparser.py',69),
  ('condition -> expression > expression','condition',3,'p_condition','Mparser.py',70),
  ('variable -> ID','variable',1,'p_variable','Mparser.py',74),
  ('range -> expression : expression','range',3,'p_range','Mparser.py',78),
  ('instruction -> statement ;','instruction',2,'p_instruction_statement','Mparser.py',82),
  ('statement -> BREAK','statement',1,'p_statement_break','Mparser.py',86),
  ('statement -> CONTINUE','statement',1,'p_statement_continue','Mparser.py',90),
  ('statement -> RETURN','statement',1,'p_statement_return','Mparser.py',94),
  ('statement -> RETURN expression','statement',2,'p_statement_return_expression','Mparser.py',98),
  ('statement -> PRINT expression_list','statement',2,'p_statement_print','Mparser.py',102),
  ('statement -> lvalue = expression','statement',3,'p_statement_assignment','Mparser.py',106),
  ('statement -> lvalue ADDASSIGN expression','statement',3,'p_statement_assignment','Mparser.py',107),
  ('statement -> lvalue SUBASSIGN expression','statement',3,'p_statement_assignment','Mparser.py',108),
  ('statement -> lvalue MULASSIGN expression','statement',3,'p_statement_assignment','Mparser.py',109),
  ('statement -> lvalue DIVASSIGN expression','statement',3,'p_statement_assignment','Mparser.py',110),
  ('lvalue -> variable','lvalue',1,'p_lvalue_variable','Mparser.py',114),
  ('lvalue -> variable [ expression_list ]','lvalue',4,'p_lvalue_reference','Mparser.py',118),
  ('expression -> expression + expression','expression',3,'p_expression_binary','Mparser.py',122),
  ('expression -> expression - expression','expression',3,'p_expression_binary','Mparser.py',123),
  ('expression -> expression * expression','expression',3,'p_expression_binary','Mparser.py',124),
  ('expression -> expression / expression','expression',3,'p_expression_binary','Mparser.py',125),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_binary','Mparser.py',126),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_binary','Mparser.py',127),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_binary','Mparser.py',128),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression_binary','Mparser.py',129),
  ('expression -> - expression','expression',2,'p_expression_uminus','Mparser.py',133),
  ("expression -> expression '",'expression',2,'p_expression_transpose','Mparser.py',137),
  ('expression -> ( expression )','expression',3,'p_expression_group','Mparser.py',141),
  ('expression -> lvalue','expression',1,'p_expression_lvalue','Mparser.py',145),
  ('expression -> range','expression',1,'p_expression_range','Mparser.py',149),
  ('expression -> INTNUM','expression',1,'p_expression_intnum','Mparser.py',153),
  ('expression -> FLOATNUM','expression',1,'p_expression_floatnum','Mparser.py',157),
  ('expression -> STRING','expression',1,'p_expression_string','Mparser.py',161),
  ('expression_list -> expression_list , expression','expression_list',3,'p_expression_list','Mparser.py',165),
  ('expression_list -> expression','expression_list',1,'p_expression_list_single','Mparser.py',169),
  ('expression_list -> <empty>','expression_list',0,'p_expression_list_empty','Mparser.py',173),
  ('expression -> [ expression_list ]','expression',3,'p_vector','Mparser.py',177),
  ('expression -> EYE ( expression )','expression',4,'p_eye_1','Mparser.py',193),
  ('expression -> EYE ( expression , expression )','expression',6,'p_eye_2','Mparser.py',197),
  ('expression -> ZEROS ( expression )','expression',4,'p_zeros_1','Mparser.py',201),
  ('expression -> ZEROS ( expression , expression )','expression',6,'p_zeros_2','Mparser.py',205),
  ('expression -> ONES ( expression )','expression',4,'p_ones_1','Mparser.py',209),
  ('expression -> ONES ( expression , expression )','expression',6,'p_ones_2','Mparser.py',213),
]
