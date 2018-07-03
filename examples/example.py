#!/usr/bin/env python

import sys
import importlib
import math

Unit = object()
World = object()

class IdrisError(Exception):
  pass

def _idris_error(msg):
  raise IdrisError(msg)

def _idris_pymodule(name):
  return importlib.import_module(name)

def _idris_call(f, args):
  return f(*list(args))

def _idris_foreach(it, st, f):
  for x in it:
    # Apply st, x, world
    st = APPLY0(APPLY0(APPLY0(f, st), x), World)
  return st

def _idris_try(f, fail, succ):
  try:
    result = APPLY0(f, World)  # apply to world
    return APPLY0(succ, result)
  except Exception as e:
    return APPLY0(fail, e)

def _idris_raise(e):
  raise e

def _idris_marshal_PIO(action):
  return lambda: APPLY0(action, World)  # delayed apply-to-world

def _idris_get_global(name):
  return globals()[name]

class _ConsIter(object):
  def __init__(self, node):
    self.node = node

  def __next__(self):
    if self.node.isNil:
      raise StopIteration
    else:
      result = self.node.head
      self.node = self.node.tail
      return result

class ConsList(object):
  def __init__(self, isNil=True, head=None, tail=None):
    self.isNil = isNil
    self.head  = head
    self.tail  = tail

  def __nonzero__(self):
    return not self.isNil

  def __len__(self):
    cnt = 0
    while not self.isNil:
      self = self.tail
      cnt += 1
    return cnt

  def cons(self, x):
    return ConsList(isNil=False, head=x, tail=self)

  def __iter__(self):
    return _ConsIter(self)

# Python.Functions.$.
def _idris_Python_46_Functions_46__36__46_(arg0, arg1, arg2, arg3, arg4, arg5, in6):
  while True:
    in7 = _idris_call(arg3, _idris_Python_46_Functions_46_strip(None, arg2, arg5))
    return in7

# Prelude.Bool.&&
def _idris_Prelude_46_Bool_46__38__38_(arg0, arg1):
  while True:
    if not arg0:  # Prelude.Bool.False
      return arg0
    else:  # Prelude.Bool.True
      return EVAL0(arg1)
    return _idris_error("unreachable due to case in tail position")

# Prelude.Basics..
def _idris_Prelude_46_Basics_46__46_(arg0, arg1, arg2, arg3, arg4, x5):
  while True:
    return APPLY0(arg3, APPLY0(arg4, x5))

# Python.Fields./.
def _idris_Python_46_Fields_46__47__46_(arg0, arg1, arg2, arg3, arg4):
  while True:
    return getattr(arg2, arg3)

# Python.Fields./:
def _idris_Python_46_Fields_46__47__58_(arg0, arg1, arg2, arg3, arg4, in5):
  while True:
    in6 = APPLY0(arg2, in5)
    return _idris_Python_46_Fields_46__47__46_(None, None, in6, arg3, None)

# Prelude.Monad.>>=
def _idris_Prelude_46_Monad_46__62__62__61_(arg0, arg1, arg2, arg3):
  while True:
    return APPLY0(APPLY0(arg1, arg2), arg3)

# Force
def _idris_Force(arg0, arg1, arg2):
  while True:
    return EVAL0(arg2)

# assert_unreachable
def _idris_assert_95_unreachable():
  while True:
    return None

# call__IO
def _idris_call_95__95_IO(arg0, arg1, arg2):
  while True:
    return APPLY0(arg2, None)

# Python.Exceptions.catch
def _idris_Python_46_Exceptions_46_catch(arg0, arg1, arg2, in3):
  while True:
    in4 = APPLY0(arg1, in3)
    if in4[0] == 1:  # Python.Exceptions.Except
      in5, in6 = in4[1:]
      return APPLY0(APPLY0(APPLY0(arg2, in5), in6), in3)
    else:  # Python.Exceptions.OK
      in7 = in4[1]
      return in7
    return _idris_error("unreachable due to case in tail position")

# Python.Prim.collect
def _idris_Python_46_Prim_46_collect(arg0, arg1, arg2, arg3, in4):
  while True:
    in8 = _idris_Python_46_Prim_46_foreach(
      None,
      None,
      None,
      arg2,
      ConsList(),
      (65704,),  # {U_Python.Prim.{collect_0}_3}
      None,
      in4
    )
    return _idris_Prelude_46_List_46_reverseOnto(None, ConsList(), in8)

# Python.Prim.foreach
def _idris_Python_46_Prim_46_foreach(arg0, arg1, arg2, arg3, arg4, arg5, arg6, in7):
  while True:
    in8 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (0,),  # Python.Telescope.Return
      _idris_Python_46_Fields_46__47__46_(None, None, arg3, u'__iter__', None),
      None,
      Unit,
      in7
    )
    in9 = _idris_foreach(arg3, arg4, arg5)
    return in9

# Python.Lib.Threading.forkPIO
def _idris_Python_46_Lib_46_Threading_46_forkPIO(arg0, arg1, in2):
  while True:
    in3 = _idris_Python_46_Fields_46__47__58_(
      None,
      None,
      (65688, None, u'queue'),  # {U_Python.importModule_1}
      u'Queue',
      None,
      in2
    )
    in6 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (1, (1,), (65682,)),  # Python.Telescope.Bind, Python.Telescope.Forall, {U_Python.Lib.Threading.{forkPIO_2}_1}
      in3,
      None,
      (0, (0,), (0, 1, Unit)),  # Builtins.MkDPair, Data.Erased.Erase, Builtins.MkDPair
      in2
    )
    in7 = _idris_Python_46_Fields_46__47__58_(
      None,
      None,
      (65688, None, u'threading'),  # {U_Python.importModule_1}
      u'Thread',
      None,
      in2
    )
    in10 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (1, (0,), (65683,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_4}_1}
      in7,
      None,
      (
        0,  # Builtins.MkDPair
        None,
        (0, _idris_Python_46_marshalPIO(None, (65680, None, arg1, in6)), Unit)  # Builtins.MkDPair, {U_Python.Lib.Threading.forkPIO, worker_1}
      ),
      in2
    )
    in11 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (0,),  # Python.Telescope.Return
      _idris_Python_46_Fields_46__47__46_(None, None, in10, u'start', None),
      None,
      Unit,
      in2
    )
    return in6

# Prelude.Maybe.fromMaybe
def _idris_Prelude_46_Maybe_46_fromMaybe(arg0, arg1, arg2):
  while True:
    if arg2 is not None:  # Prelude.Maybe.Just
      in3 = arg2
      return in3
    else:  # Prelude.Maybe.Nothing
      return EVAL0(arg1)
    return _idris_error("unreachable due to case in tail position")

# Python.Exceptions.fromString
def _idris_Python_46_Exceptions_46_fromString(arg0):
  while True:
    return {
      u'ArithmeticError': (3,),  # Python.Exceptions.ArithmeticError
      u'AssertionError': (7,),  # Python.Exceptions.AssertionError
      u'AttributeError': (8,),  # Python.Exceptions.AttributeError
      u'BufferError': (2,),  # Python.Exceptions.BufferError
      u'EOFError': (15,),  # Python.Exceptions.EOFError
      u'EnvironmentError': (9,),  # Python.Exceptions.EnvironmentError
      u'FileNotFoundError': (12,),  # Python.Exceptions.FileNotFoundError
      u'FloatingPointError': (4,),  # Python.Exceptions.FloatingPointError
      u'IOError': (10,),  # Python.Exceptions.IOError
      u'ImportError': (16,),  # Python.Exceptions.ImportError
      u'IndentationError': (27,),  # Python.Exceptions.IndentationError
      u'IndexError': (18,),  # Python.Exceptions.IndexError
      u'KeyError': (19,),  # Python.Exceptions.KeyError
      u'LookupError': (17,),  # Python.Exceptions.LookupError
      u'MemoryError': (20,),  # Python.Exceptions.MemoryError
      u'NameError': (21,),  # Python.Exceptions.NameError
      u'NotImplementedError': (25,),  # Python.Exceptions.NotImplementedError
      u'OSError': (11,),  # Python.Exceptions.OSError
      u'OverflowError': (5,),  # Python.Exceptions.OverflowError
      u'ReferenceError': (23,),  # Python.Exceptions.ReferenceError
      u'RuntimeError': (24,),  # Python.Exceptions.RuntimeError
      u'StandardError': (1,),  # Python.Exceptions.StandardError
      u'StopIteration': (0,),  # Python.Exceptions.StopIteration
      u'SyntaxError': (26,),  # Python.Exceptions.SyntaxError
      u'SystemError': (29,),  # Python.Exceptions.SystemError
      u'TabError': (28,),  # Python.Exceptions.TabError
      u'TypeError': (30,),  # Python.Exceptions.TypeError
      u'UnboundLocalError': (22,),  # Python.Exceptions.UnboundLocalError
      u'UnicodeDecodeError': (33,),  # Python.Exceptions.UnicodeDecodeError
      u'UnicodeEncodeError': (34,),  # Python.Exceptions.UnicodeEncodeError
      u'UnicodeError': (32,),  # Python.Exceptions.UnicodeError
      u'UnicodeTranslateError': (35,),  # Python.Exceptions.UnicodeTranslateError
      u'VMSError': (14,),  # Python.Exceptions.VMSError
      u'ValueError': (31,),  # Python.Exceptions.ValueError
      u'WindowsError': (13,),  # Python.Exceptions.WindowsError
      u'ZeroDivisionError': (6,)  # Python.Exceptions.ZeroDivisionError
    }.get(arg0, (36,))  # Python.Exceptions.Other

# idris_crash
def _idris_idris_95_crash():
  while True:
    return None

# Prelude.Bool.ifThenElse
def _idris_Prelude_46_Bool_46_ifThenElse(arg0, arg1, arg2, arg3):
  while True:
    if not arg1:  # Prelude.Bool.False
      return EVAL0(arg3)
    else:  # Prelude.Bool.True
      return EVAL0(arg2)
    return _idris_error("unreachable due to case in tail position")

# Python.importModule
def _idris_Python_46_importModule(arg0, arg1, w2):
  while True:
    return _idris_pymodule(arg1)

# Prelude.Interfaces.intToBool
def _idris_Prelude_46_Interfaces_46_intToBool(arg0):
  while True:
    if arg0 == 0:
      return False
    else:
      return True
    return _idris_error("unreachable due to case in tail position")

# io_bind
def _idris_io_95_bind(arg0, arg1, arg2, arg3, k4, w5):
  while True:
    return APPLY0(APPLY0(k4, APPLY0(arg3, w5)), w5)

# io_pure
def _idris_io_95_pure(arg0, arg1, arg2, w3):
  while True:
    return arg2

# Python.Prim.iterate
def _idris_Python_46_Prim_46_iterate(arg0, arg1, arg2, arg3, arg4, arg5, arg6, in7):
  while True:
    in8 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (0,),  # Python.Telescope.Return
      _idris_Python_46_Fields_46__47__46_(None, None, arg3, u'__iter__', None),
      None,
      Unit,
      in7
    )
    return _idris_Python_46_Prim_46_iterate_58_iter_58_0(
      None, None, None, None, None, None, None, None, in8, arg4, arg5,
      in7
    )

# Main.main
def _idris_Main_46_main(in0):
  while True:
    in1 = _idris_Python_46_importModule(None, u'requests', in0)
    in2 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (0,),  # Python.Telescope.Return
      _idris_Python_46_Fields_46__47__46_(None, None, in1, u'Session', None),
      None,
      Unit,
      in0
    )
    in4 = _idris_Python_46_Fields_46__47__58_(
      None,
      None,
      (
        65679,  # {U_Python.Functions.$._1}
        None,
        None,
        (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}
        _idris_Python_46_Fields_46__47__46_(None, None, in2, u'get', None),
        None,
        (0, u'http://idris-lang.org', Unit)  # Builtins.MkDPair
      ),
      u'text',
      None,
      in0
    )
    in5 = _idris_Python_46_importModule(None, u'bs4', in0)
    in8 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (1, (0,), (65683,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_4}_1}
      _idris_Python_46_Fields_46__47__46_(None, None, in5, u'BeautifulSoup', None),
      None,
      (0, in4, (0, u'html.parser', Unit)),  # Builtins.MkDPair, Builtins.MkDPair
      in0
    )
    in10 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}
      _idris_Python_46_Fields_46__47__46_(None, None, in8, u'select', None),
      None,
      (0, u'div.entry-content li', Unit),  # Builtins.MkDPair
      in0
    )
    in11 = sys.stdout.write(u'Idris has got the following exciting features:\u000a')
    in12 = Unit
    in24 = _idris_Python_46_Prim_46_iterate(None, None, None, in10, 0, (65702,), None, in0)  # {U_Main.{main_10}_3}
    in25 = sys.stdout.write(((u'Total number of features: ' + _idris_Prelude_46_Show_46_primNumShow(None, (65690,), (0,), in24)) + u'\u000a'))  # {U_prim__toStrInt_1}, Prelude.Show.Open
    in26 = Unit
    in27 = sys.stdout.write(u'\u000a')
    in28 = Unit
    in29 = (65694, in2)  # {U_Main.{main_12}_2}
    in38 = _idris_Python_46_Lib_46_Threading_46_forkPIO(None, APPLY0(in29, u'A'), in0)
    in39 = _idris_Python_46_Lib_46_Threading_46_forkPIO(None, APPLY0(in29, u'B'), in0)
    in40 = APPLY0(_idris_Python_46_Lib_46_Threading_46_wait(None, in38), in0)
    in41 = APPLY0(_idris_Python_46_Lib_46_Threading_46_wait(None, in39), in0)
    in42 = sys.stdout.write(((u'thread A says ' + _idris_Prelude_46_Show_46_primNumShow(None, (65689,), (0,), in40)) + u'\u000a'))  # {U_prim__toStrBigInt_1}, Prelude.Show.Open
    in43 = Unit
    in44 = sys.stdout.write(((u'thread B says ' + _idris_Prelude_46_Show_46_primNumShow(None, (65689,), (0,), in41)) + u'\u000a'))  # {U_prim__toStrBigInt_1}, Prelude.Show.Open
    in45 = Unit
    in46 = sys.stdout.write(u'\u000a')
    in47 = Unit
    in48 = _idris_Python_46_importModule(None, u'os', in0)
    in49 = sys.stdout.write(u'And now, let\'s fail!\u000a')
    in50 = Unit
    in61 = _idris_Python_46_Exceptions_46_catch(
      None,
      (65675, None, (65664, in48)),  # {U_Python.Exceptions.try_1}, {U_Main.{main_14}_1}
      (65696,),  # {U_Main.{main_17}_2}
      in0
    )
    in63 = _idris_Python_46_Exceptions_46_try(
      None,
      (
        65679,  # {U_Python.Functions.$._1}
        None,
        None,
        (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}
        _idris_Python_46_Fields_46__47__46_(None, None, in48, u'mkdir', None),
        None,
        (0, u'/root/hello', Unit)  # Builtins.MkDPair
      ),
      in0
    )
    if in63[0] == 1:  # Python.Exceptions.Except
      in64, in65 = in63[1:]
      if in64[0] == 12:  # Python.Exceptions.FileNotFoundError
        in66 = sys.stdout.write(((u'  -> (2) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(in65)) + u'\u000a'))
        return Unit
      elif in64[0] == 11:  # Python.Exceptions.OSError
        in67 = sys.stdout.write(((u'  -> (2) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(in65)) + u'\u000a'))
        return Unit
      else:
        return _idris_Python_46_Exceptions_46_raise(None, in65, in0)
      return _idris_error("unreachable due to case in tail position")
    else:  # Python.Exceptions.OK
      in68 = in63[1]
      in69 = sys.stdout.write(u'Your root could probably use some security lessons!\u000a')
      return Unit
    return _idris_error("unreachable due to case in tail position")

# Python.marshalPIO
def _idris_Python_46_marshalPIO(arg0, arg1):
  while True:
    return _idris_marshal_PIO(arg1)

# mkForeignPrim
def _idris_mkForeignPrim():
  while True:
    return None

# Python.Prim.next
def _idris_Python_46_Prim_46_next(arg0, arg1, in2):
  while True:
    in3 = _idris_Python_46_Exceptions_46_try(
      None,
      (
        65679,  # {U_Python.Functions.$._1}
        None,
        None,
        (0,),  # Python.Telescope.Return
        _idris_Python_46_Fields_46__47__46_(None, None, arg1, u'__next__', None),
        None,
        Unit
      ),
      in2
    )
    if in3[0] == 1:  # Python.Exceptions.Except
      in4, in5 = in3[1:]
      if in4[0] == 0:  # Python.Exceptions.StopIteration
        return None
      else:
        return _idris_Python_46_Exceptions_46_raise(None, in5, in2)
      return _idris_error("unreachable due to case in tail position")
    else:  # Python.Exceptions.OK
      in6 = in3[1]
      return in6
    return _idris_error("unreachable due to case in tail position")

# Prelude.Bool.not
def _idris_Prelude_46_Bool_46_not(arg0):
  while True:
    if not arg0:  # Prelude.Bool.False
      return True
    else:  # Prelude.Bool.True
      return False
    return _idris_error("unreachable due to case in tail position")

# Prelude.Show.precCon
def _idris_Prelude_46_Show_46_precCon(arg0):
  while True:
    if arg0[0] == 6:  # Prelude.Show.App
      return 6
    elif arg0[0] == 3:  # Prelude.Show.Backtick
      return 3
    elif arg0[0] == 2:  # Prelude.Show.Dollar
      return 2
    elif arg0[0] == 1:  # Prelude.Show.Eq
      return 1
    elif arg0[0] == 0:  # Prelude.Show.Open
      return 0
    elif arg0[0] == 5:  # Prelude.Show.PrefixMinus
      return 5
    else:  # Prelude.Show.User
      return 4
    return _idris_error("unreachable due to case in tail position")

# Prelude.Show.primNumShow
def _idris_Prelude_46_Show_46_primNumShow(arg0, arg1, arg2, arg3):
  while True:
    in4 = APPLY0(arg1, arg3)
    if arg2[0] == 6:  # Prelude.Show.App
      aux4 = 6
    elif arg2[0] == 3:  # Prelude.Show.Backtick
      aux4 = 3
    elif arg2[0] == 2:  # Prelude.Show.Dollar
      aux4 = 2
    elif arg2[0] == 1:  # Prelude.Show.Eq
      aux4 = 1
    elif arg2[0] == 0:  # Prelude.Show.Open
      aux4 = 0
    elif arg2[0] == 5:  # Prelude.Show.PrefixMinus
      aux4 = 5
    else:  # Prelude.Show.User
      aux4 = 4
    aux3 = _idris_Prelude_46_Interfaces_46_Prelude_46_Interfaces_46__64_Prelude_46_Interfaces_46_Ord_36_Integer_58__33_compare_58_0(
      aux4, 5
    )
    if aux3[0] == 2:  # Prelude.Interfaces.GT
      aux5 = True
    else:
      if arg2[0] == 6:  # Prelude.Show.App
        aux7 = 6
      elif arg2[0] == 3:  # Prelude.Show.Backtick
        aux7 = 3
      elif arg2[0] == 2:  # Prelude.Show.Dollar
        aux7 = 2
      elif arg2[0] == 1:  # Prelude.Show.Eq
        aux7 = 1
      elif arg2[0] == 0:  # Prelude.Show.Open
        aux7 = 0
      elif arg2[0] == 5:  # Prelude.Show.PrefixMinus
        aux7 = 5
      else:  # Prelude.Show.User
        aux7 = 4
      aux6 = (aux7 == 5)
      if aux6 == 0:
        aux8 = False
      else:
        aux8 = True
      aux5 = aux8
    aux2 = aux5
    if not aux2:  # Prelude.Bool.False
      aux9 = False
    else:  # Prelude.Bool.True
      aux11 = (in4 == u'')
      if aux11 == 0:
        aux12 = True
      else:
        aux12 = False
      aux10 = _idris_Decidable_46_Equality_46_Decidable_46_Equality_46__64_Decidable_46_Equality_46_DecEq_36_Bool_58__33_decEq_58_0(
        aux12, True
      )
      if aux10[0] == 1:  # Prelude.Basics.No
        aux13 = False
      else:  # Prelude.Basics.Yes
        aux14 = (in4[0] == u'-')
        if aux14 == 0:
          aux15 = False
        else:
          aux15 = True
        aux13 = aux15
      aux9 = aux13
    aux1 = aux9
    if not aux1:  # Prelude.Bool.False
      return in4
    else:  # Prelude.Bool.True
      return (u'(' + (in4 + u')'))
    return _idris_error("unreachable due to case in tail position")

# prim__addInt
def _idris_prim_95__95_addInt(arg0, arg1):
  while True:
    return (arg0 + arg1)

# prim__asPtr
def _idris_prim_95__95_asPtr(arg0):
  while True:
    return _idris_error("unimplemented external: prim__asPtr")

# prim__concat
def _idris_prim_95__95_concat(arg0, arg1):
  while True:
    return (arg0 + arg1)

# prim__eqBigInt
def _idris_prim_95__95_eqBigInt(arg0, arg1):
  while True:
    return (arg0 == arg1)

# prim__eqChar
def _idris_prim_95__95_eqChar(arg0, arg1):
  while True:
    return (arg0 == arg1)

# prim__eqManagedPtr
def _idris_prim_95__95_eqManagedPtr(arg0, arg1):
  while True:
    return _idris_error("unimplemented external: prim__eqManagedPtr")

# prim__eqPtr
def _idris_prim_95__95_eqPtr(arg0, arg1):
  while True:
    return _idris_error("unimplemented external: prim__eqPtr")

# prim__eqString
def _idris_prim_95__95_eqString(arg0, arg1):
  while True:
    return (arg0 == arg1)

# prim__null
def _idris_prim_95__95_null():
  while True:
    return None

# prim__peek16
def _idris_prim_95__95_peek16(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__peek16")

# prim__peek32
def _idris_prim_95__95_peek32(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__peek32")

# prim__peek64
def _idris_prim_95__95_peek64(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__peek64")

# prim__peek8
def _idris_prim_95__95_peek8(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__peek8")

# prim__peekDouble
def _idris_prim_95__95_peekDouble(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__peekDouble")

# prim__peekPtr
def _idris_prim_95__95_peekPtr(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__peekPtr")

# prim__peekSingle
def _idris_prim_95__95_peekSingle(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__peekSingle")

# prim__poke16
def _idris_prim_95__95_poke16(arg0, arg1, arg2, arg3):
  while True:
    return _idris_error("unimplemented external: prim__poke16")

# prim__poke32
def _idris_prim_95__95_poke32(arg0, arg1, arg2, arg3):
  while True:
    return _idris_error("unimplemented external: prim__poke32")

# prim__poke64
def _idris_prim_95__95_poke64(arg0, arg1, arg2, arg3):
  while True:
    return _idris_error("unimplemented external: prim__poke64")

# prim__poke8
def _idris_prim_95__95_poke8(arg0, arg1, arg2, arg3):
  while True:
    return _idris_error("unimplemented external: prim__poke8")

# prim__pokeDouble
def _idris_prim_95__95_pokeDouble(arg0, arg1, arg2, arg3):
  while True:
    return _idris_error("unimplemented external: prim__pokeDouble")

# prim__pokePtr
def _idris_prim_95__95_pokePtr(arg0, arg1, arg2, arg3):
  while True:
    return _idris_error("unimplemented external: prim__pokePtr")

# prim__pokeSingle
def _idris_prim_95__95_pokeSingle(arg0, arg1, arg2, arg3):
  while True:
    return _idris_error("unimplemented external: prim__pokeSingle")

# prim__ptrOffset
def _idris_prim_95__95_ptrOffset(arg0, arg1):
  while True:
    return _idris_error("unimplemented external: prim__ptrOffset")

# prim__readChars
def _idris_prim_95__95_readChars(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__readChars")

# prim__readFile
def _idris_prim_95__95_readFile(arg0, arg1):
  while True:
    return _idris_error("unimplemented external: prim__readFile")

# prim__registerPtr
def _idris_prim_95__95_registerPtr(arg0, arg1):
  while True:
    return _idris_error("unimplemented external: prim__registerPtr")

# prim__sizeofPtr
def _idris_prim_95__95_sizeofPtr():
  while True:
    return _idris_error("unimplemented external: prim__sizeofPtr")

# prim__sltBigInt
def _idris_prim_95__95_sltBigInt(arg0, arg1):
  while True:
    return (arg0 < arg1)

# prim__stderr
def _idris_prim_95__95_stderr():
  while True:
    return _idris_error("unimplemented external: prim__stderr")

# prim__stdin
def _idris_prim_95__95_stdin():
  while True:
    return _idris_error("unimplemented external: prim__stdin")

# prim__stdout
def _idris_prim_95__95_stdout():
  while True:
    return _idris_error("unimplemented external: prim__stdout")

# prim__strHead
def _idris_prim_95__95_strHead(arg0):
  while True:
    return arg0[0]

# prim__toStrBigInt
def _idris_prim_95__95_toStrBigInt(arg0):
  while True:
    return str(arg0)

# prim__toStrInt
def _idris_prim_95__95_toStrInt(arg0):
  while True:
    return str(arg0)

# prim__vm
def _idris_prim_95__95_vm(arg0):
  while True:
    return _idris_error("unimplemented external: prim__vm")

# prim__writeFile
def _idris_prim_95__95_writeFile(arg0, arg1, arg2):
  while True:
    return _idris_error("unimplemented external: prim__writeFile")

# prim__writeString
def _idris_prim_95__95_writeString(arg0, arg1):
  while True:
    return sys.stdout.write(arg1)

# prim__zextInt_BigInt
def _idris_prim_95__95_zextInt_95_BigInt(arg0):
  while True:
    return arg0

# prim_io_bind
def _idris_prim_95_io_95_bind(arg0, arg1, arg2, arg3):
  while True:
    return APPLY0(arg3, arg2)

# prim_lenString
def _idris_prim_95_lenString(arg0):
  while True:
    return len(arg0)

# Python.Exceptions.raise
def _idris_Python_46_Exceptions_46_raise(arg0, arg1, in2):
  while True:
    in3 = _idris_raise(arg1)
    return in3

# Prelude.List.reverseOnto
def _idris_Prelude_46_List_46_reverseOnto(arg0, arg1, arg2):
  while True:
    if arg2:  # Prelude.List.::
      in3, in4 = arg2.head, arg2.tail
      arg0, arg1, arg2, = None, arg1.cons(in3), in4,
      continue
      return _idris_error("unreachable due to tail call")
    else:  # Prelude.List.Nil
      return arg1
    return _idris_error("unreachable due to case in tail position")

# run__IO
def _idris_run_95__95_IO(arg0, arg1):
  while True:
    return APPLY0(arg1, None)

# Python.Exceptions.showException
def _idris_Python_46_Exceptions_46_showException(arg0):
  while True:
    return str(arg0)

# Prelude.Show.showParens
def _idris_Prelude_46_Show_46_showParens(arg0, arg1):
  while True:
    if not arg0:  # Prelude.Bool.False
      return arg1
    else:  # Prelude.Bool.True
      return (u'(' + (arg1 + u')'))
    return _idris_error("unreachable due to case in tail position")

# Python.Functions.strip
def _idris_Python_46_Functions_46_strip(arg0, arg1, arg2):
  while True:
    if arg1[0] == 1:  # Python.Telescope.Bind
      in3, in4 = arg1[1:]
      if in3[0] == 2:  # Python.Telescope.Default
        in5 = in3[1]
        assert arg2[0] == 0  # Builtins.MkDPair
        in6, in7 = arg2[1:]
        if in6 is not None:  # Prelude.Maybe.Just
          in8 = in6
          aux1 = in8
        else:  # Prelude.Maybe.Nothing
          aux1 = in5
        return _idris_Python_46_Functions_46_strip(None, APPLY0(in4, aux1), in7).cons(in6)
        return _idris_error("unreachable due to case in tail position")
      elif in3[0] == 1:  # Python.Telescope.Forall
        assert arg2[0] == 0  # Builtins.MkDPair
        in9, in10 = arg2[1:]
        arg0, arg1, arg2, = None, APPLY0(in4, in9), in10,
        continue
        return _idris_error("unreachable due to tail call")
        return _idris_error("unreachable due to case in tail position")
      else:  # Python.Telescope.Pi
        assert arg2[0] == 0  # Builtins.MkDPair
        in11, in12 = arg2[1:]
        return _idris_Python_46_Functions_46_strip(None, APPLY0(in4, in11), in12).cons(in11)
        return _idris_error("unreachable due to case in tail position")
      return _idris_error("unreachable due to case in tail position")
    else:  # Python.Telescope.Return
      return ConsList()
    return _idris_error("unreachable due to case in tail position")

# Python.Exceptions.try
def _idris_Python_46_Exceptions_46_try(arg0, arg1, in2):
  while True:
    in11 = _idris_try(arg1, (65677,), (65678,))  # {U_Python.Exceptions.{try_19}_1}, {U_Python.Exceptions.{try_20}_1}
    if in11[0] == 0:  # Prelude.Either.Left
      in12 = in11[1]
      return (
        1,  # Python.Exceptions.Except
        _idris_Python_46_Exceptions_46_fromString(
          _idris_Python_46_Fields_46__47__46_(
            None,
            None,
            _idris_Python_46_Fields_46__47__46_(None, None, in12, u'__class__', None),
            u'__name__',
            None
          )
        ),
        in12
      )
    else:  # Prelude.Either.Right
      in13 = in11[1]
      return (0, in13)  # Python.Exceptions.OK
    return _idris_error("unreachable due to case in tail position")

# Python.IO.unRaw
def _idris_Python_46_IO_46_unRaw(arg0, arg1):
  while True:
    return arg1

# unsafePerformPrimIO
def _idris_unsafePerformPrimIO():
  while True:
    return None

# Python.Lib.Threading.wait
def _idris_Python_46_Lib_46_Threading_46_wait(arg0, arg1):
  while True:
    return (
      65679,  # {U_Python.Functions.$._1}
      None,
      None,
      (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}
      _idris_Python_46_Fields_46__47__46_(None, None, arg1, u'get', None),
      None,
      (0, 1, Unit)  # Builtins.MkDPair
    )

# world
def _idris_world(arg0):
  while True:
    return arg0

# Prelude.Bool.||
def _idris_Prelude_46_Bool_46__124__124_(arg0, arg1):
  while True:
    if not arg0:  # Prelude.Bool.False
      return EVAL0(arg1)
    else:  # Prelude.Bool.True
      return arg0
    return _idris_error("unreachable due to case in tail position")

# {APPLY_0}
def APPLY0(fn0, arg0):
  while True:
    if fn0[0] < 65681:
      if fn0[0] < 65671:
        if fn0[0] < 65666:
          if fn0[0] < 65664:
            if fn0[0] == 65662:  # {U_Main.{main_10}_1}
              P_c0, P_c1 = fn0[1:]
              return _idris_Main_46__123_main_95_10_125_(P_c0, P_c1, arg0)
            else:  # {U_Main.{main_12}_1}
              P_c0, P_c1 = fn0[1:]
              return _idris_Main_46__123_main_95_12_125_(P_c0, P_c1, arg0)
          else:
            if fn0[0] == 65664:  # {U_Main.{main_14}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_14_125_(P_c0, arg0)
            else:  # {U_Main.{main_15}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_15_125_(P_c0, arg0)
        else:
          if fn0[0] < 65668:
            if fn0[0] == 65666:  # {U_Main.{main_16}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_16_125_(P_c0, arg0)
            else:  # {U_Main.{main_17}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_17_125_(P_c0, arg0)
          else:
            if fn0[0] == 65668:  # {U_Main.{main_9}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_9_125_(P_c0, arg0)
            elif fn0[0] == 65669:  # {U_Main.{main_example__idr_84_32_84_36_case_lam_29}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_example_95__95_idr_95_84_95_32_95_84_95_36_95_case_95_lam_95_29_125_(
                P_c0, arg0
              )
            else:  # {U_Main.{main_example__idr_84_32_84_36_case_lam_30}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_example_95__95_idr_95_84_95_32_95_84_95_36_95_case_95_lam_95_30_125_(
                P_c0, arg0
              )
      else:
        if fn0[0] < 65676:
          if fn0[0] < 65673:
            if fn0[0] == 65671:  # {U_Main.{main_example__idr_91_13_91_50_case_lam_31}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_example_95__95_idr_95_91_95_13_95_91_95_50_95_case_95_lam_95_31_125_(
                P_c0, arg0
              )
            else:  # {U_Main.{main_example__idr_91_13_91_50_case_lam_32}_1}
              P_c0 = fn0[1]
              return _idris_Main_46__123_main_95_example_95__95_idr_95_91_95_13_95_91_95_50_95_case_95_lam_95_32_125_(
                P_c0, arg0
              )
          else:
            if fn0[0] == 65673:  # {U_Main.{main_example__idr_91_13_91_50_case_lam_33}_1}
              return _idris_Main_46__123_main_95_example_95__95_idr_95_91_95_13_95_91_95_50_95_case_95_lam_95_33_125_(
                arg0
              )
            elif fn0[0] == 65674:  # {U_Python.Exceptions.raise_1}
              P_c0, P_c1 = fn0[1:]
              return _idris_Python_46_Exceptions_46_raise(P_c0, P_c1, arg0)
            else:  # {U_Python.Exceptions.try_1}
              P_c0, P_c1 = fn0[1:]
              return _idris_Python_46_Exceptions_46_try(P_c0, P_c1, arg0)
        else:
          if fn0[0] < 65678:
            if fn0[0] == 65676:  # {U_Python.Exceptions.{catch_____Python__Exceptions__idr_132_16_132_21_case_lam_24}_1}
              P_c0 = fn0[1]
              return _idris_Python_46_Exceptions_46__123_catch_95__95__95__95__95_Python_95__95_Exceptions_95__95_idr_95_132_95_16_95_132_95_21_95_case_95_lam_95_24_125_(
                P_c0, arg0
              )
            else:  # {U_Python.Exceptions.{try_19}_1}
              return _idris_Python_46_Exceptions_46__123_try_95_19_125_(arg0)
          else:
            if fn0[0] == 65678:  # {U_Python.Exceptions.{try_20}_1}
              return _idris_Python_46_Exceptions_46__123_try_95_20_125_(arg0)
            elif fn0[0] == 65679:  # {U_Python.Functions.$._1}
              P_c0, P_c1, P_c2, P_c3, P_c4, P_c5 = fn0[1:]
              return _idris_Python_46_Functions_46__36__46_(P_c0, P_c1, P_c2, P_c3, P_c4, P_c5, arg0)
            else:  # {U_Python.Lib.Threading.forkPIO, worker_1}
              P_c0, P_c1, P_c2 = fn0[1:]
              return _idris_Python_46_Lib_46_Threading_46_forkPIO_58_worker_58_0(
                P_c0, P_c1, P_c2, arg0
              )
    else:
      if fn0[0] < 65690:
        if fn0[0] < 65685:
          if fn0[0] < 65683:
            if fn0[0] == 65681:  # {U_Python.Lib.Threading.{forkPIO_1}_1}
              return _idris_Python_46_Lib_46_Threading_46__123_forkPIO_95_1_125_(arg0)
            else:  # {U_Python.Lib.Threading.{forkPIO_2}_1}
              return _idris_Python_46_Lib_46_Threading_46__123_forkPIO_95_2_125_(arg0)
          else:
            if fn0[0] == 65683:  # {U_Python.Lib.Threading.{forkPIO_4}_1}
              return _idris_Python_46_Lib_46_Threading_46__123_forkPIO_95_4_125_(arg0)
            else:  # {U_Python.Prim.iterate, iter_1}
              P_c0, P_c1, P_c2, P_c3, P_c4, P_c5, P_c6, P_c7, P_c8, P_c9, P_c10 = fn0[1:]
              return _idris_Python_46_Prim_46_iterate_58_iter_58_0(
                P_c0, P_c1, P_c2, P_c3, P_c4, P_c5, P_c6, P_c7, P_c8, P_c9, P_c10,
                arg0
              )
        else:
          if fn0[0] < 65687:
            if fn0[0] == 65685:  # {U_Python.Prim.{collect_0}_1}
              P_c0, P_c1 = fn0[1:]
              return _idris_Python_46_Prim_46__123_collect_95_0_125_(P_c0, P_c1, arg0)
            else:  # {U_Python.Prim.{next_____Python__Prim__idr_61_11_61_38_case_lam_25}_1}
              return _idris_Python_46_Prim_46__123_next_95__95__95__95__95_Python_95__95_Prim_95__95_idr_95_61_95_11_95_61_95_38_95_case_95_lam_95_25_125_(
                arg0
              )
          else:
            if fn0[0] == 65687:  # {U_Python.Prim.{next_____Python__Prim__idr_61_11_61_38_case_lam_26}_1}
              P_c0 = fn0[1]
              return _idris_Python_46_Prim_46__123_next_95__95__95__95__95_Python_95__95_Prim_95__95_idr_95_61_95_11_95_61_95_38_95_case_95_lam_95_26_125_(
                P_c0, arg0
              )
            elif fn0[0] == 65688:  # {U_Python.importModule_1}
              P_c0, P_c1 = fn0[1:]
              return _idris_Python_46_importModule(P_c0, P_c1, arg0)
            else:  # {U_prim__toStrBigInt_1}
              return _idris_prim_95__95_toStrBigInt(arg0)
      else:
        if fn0[0] < 65698:
          if fn0[0] < 65692:
            if fn0[0] == 65690:  # {U_prim__toStrInt_1}
              return _idris_prim_95__95_toStrInt(arg0)
            else:  # {U_{Python.Prim.iterate:iter:0_lam_23}_1}
              P_c0, P_c1 = fn0[1:]
              return _idris__123_Python_46_Prim_46_iterate_58_iter_58_0_95_lam_95_23_125_(
                P_c0, P_c1, arg0
              )
          else:
            if fn0[0] == 65692:  # {U_Main.{main_10}_2}
              P_c0 = fn0[1]
              return (65662, P_c0, arg0)  # {U_Main.{main_10}_1}
            elif fn0[0] == 65694:  # {U_Main.{main_12}_2}
              P_c0 = fn0[1]
              return (65663, P_c0, arg0)  # {U_Main.{main_12}_1}
            else:  # {U_Main.{main_17}_2}
              return (65667, arg0)  # {U_Main.{main_17}_1}
        else:
          if fn0[0] < 65702:
            if fn0[0] == 65698:  # {U_Main.{main_9}_2}
              return (65668, arg0)  # {U_Main.{main_9}_1}
            else:  # {U_Python.Prim.{collect_0}_2}
              P_c0 = fn0[1]
              return (65685, P_c0, arg0)  # {U_Python.Prim.{collect_0}_1}
          else:
            if fn0[0] == 65702:  # {U_Main.{main_10}_3}
              return (65692, arg0)  # {U_Main.{main_10}_2}
            else:  # {U_Python.Prim.{collect_0}_3}
              return (65700, arg0)  # {U_Python.Prim.{collect_0}_2}
    return _idris_error("unreachable due to case in tail position")

# {APPLY2_0}
def _idris__123_APPLY2_95_0_125_(
  fn0,
  _idris__123_arg0_95_0_125_,
  _idris__123_arg1_95_0_125_
):
  while True:
    if fn0[0] < 65700:
      if fn0[0] < 65696:
        if fn0[0] == 65692:  # {U_Main.{main_10}_2}
          P_c0 = fn0[1]
          return _idris_Main_46__123_main_95_10_125_(
            P_c0,
            _idris__123_arg0_95_0_125_,
            _idris__123_arg1_95_0_125_
          )
        else:  # {U_Main.{main_12}_2}
          P_c0 = fn0[1]
          return _idris_Main_46__123_main_95_12_125_(
            P_c0,
            _idris__123_arg0_95_0_125_,
            _idris__123_arg1_95_0_125_
          )
      else:
        if fn0[0] == 65696:  # {U_Main.{main_17}_2}
          return _idris_Main_46__123_main_95_17_125_(
            _idris__123_arg0_95_0_125_,
            _idris__123_arg1_95_0_125_
          )
        else:  # {U_Main.{main_9}_2}
          return _idris_Main_46__123_main_95_9_125_(
            _idris__123_arg0_95_0_125_,
            _idris__123_arg1_95_0_125_
          )
    else:
      if fn0[0] < 65704:
        if fn0[0] == 65700:  # {U_Python.Prim.{collect_0}_2}
          P_c0 = fn0[1]
          return _idris_Python_46_Prim_46__123_collect_95_0_125_(
            P_c0,
            _idris__123_arg0_95_0_125_,
            _idris__123_arg1_95_0_125_
          )
        else:  # {U_Main.{main_10}_3}
          return (65662, _idris__123_arg0_95_0_125_, _idris__123_arg1_95_0_125_)  # {U_Main.{main_10}_1}
      else:
        assert fn0[0] == 65704  # {U_Python.Prim.{collect_0}_3}
        return (65685, _idris__123_arg0_95_0_125_, _idris__123_arg1_95_0_125_)  # {U_Python.Prim.{collect_0}_1}
    return _idris_error("unreachable due to case in tail position")

# {EVAL_0}
def EVAL0(arg0):
  while True:
    return arg0

# Python.Prim.{collect_0}
def _idris_Python_46_Prim_46__123_collect_95_0_125_(lift0, lift1, lift2):
  while True:
    return lift0.cons(lift1)

# {runMain_0}
def runMain0():
  while True:
    return EVAL0(_idris_Main_46_main(None))

# Python.Lib.Threading.{forkPIO_1}
def _idris_Python_46_Lib_46_Threading_46__123_forkPIO_95_1_125_(lift0):
  while True:
    return (0,)  # Python.Telescope.Return

# Python.Lib.Threading.{forkPIO_2}
def _idris_Python_46_Lib_46_Threading_46__123_forkPIO_95_2_125_(lift0):
  while True:
    return (1, (2, 0), (65681,))  # Python.Telescope.Bind, Python.Telescope.Default, {U_Python.Lib.Threading.{forkPIO_1}_1}

# Python.Lib.Threading.{forkPIO_4}
def _idris_Python_46_Lib_46_Threading_46__123_forkPIO_95_4_125_(lift0):
  while True:
    return (1, (0,), (65681,))  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}

# Main.{main_9}
def _idris_Main_46__123_main_95_9_125_(lift0, lift1):
  while True:
    return (lift0 + lift1)

# Main.{main_10}
def _idris_Main_46__123_main_95_10_125_(lift0, lift1, lift2):
  while True:
    in16 = _idris_Python_46_Prim_46_collect(
      None,
      None,
      _idris_Python_46_Fields_46__47__46_(None, None, lift1, u'strings', None),
      None,
      lift2
    )
    in21 = _idris_Prelude_46_Foldable_46_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List_58__33_foldr_58_0(
      None,
      None,
      (65698,),  # {U_Main.{main_9}_2}
      u'',
      in16
    )
    in22 = sys.stdout.write(((_idris_Prelude_46_Show_46_primNumShow(None, (65690,), (0,), (lift0 + 1)) + (u'. ' + in21)) + u'\u000a'))  # {U_prim__toStrInt_1}, Prelude.Show.Open
    in23 = Unit
    return (lift0 + 1)

# Main.{main_12}
def _idris_Main_46__123_main_95_12_125_(lift0, lift1, lift2):
  while True:
    in32 = sys.stdout.write(((u'thread ' + (lift1 + u' starting')) + u'\u000a'))
    in33 = Unit
    in35 = _idris_Python_46_Fields_46__47__58_(
      None,
      None,
      (
        65679,  # {U_Python.Functions.$._1}
        None,
        None,
        (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}
        _idris_Python_46_Fields_46__47__46_(None, None, lift0, u'get', None),
        None,
        (0, u'http://idris-lang.org', Unit)  # Builtins.MkDPair
      ),
      u'text',
      None,
      lift2
    )
    in36 = sys.stdout.write(((u'thread ' + (lift1 + u' done')) + u'\u000a'))
    in37 = Unit
    return len(in35)

# Main.{main_14}
def _idris_Main_46__123_main_95_14_125_(lift0, lift1):
  while True:
    in53 = _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}
      _idris_Python_46_Fields_46__47__46_(None, None, lift0, u'mkdir', None),
      None,
      (0, u'/root/hello', Unit),  # Builtins.MkDPair
      lift1
    )
    in54 = sys.stdout.write(u'Something\'s wrong, your root\'s homedir is writable!\u000a')
    return Unit

# Main.{main_15}
def _idris_Main_46__123_main_95_15_125_(lift0, lift1):
  while True:
    in58 = sys.stdout.write(((u'  -> (2) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(lift0)) + u'\u000a'))
    return Unit

# Main.{main_16}
def _idris_Main_46__123_main_95_16_125_(lift0, lift1):
  while True:
    in60 = sys.stdout.write(((u'  -> (1) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(lift0)) + u'\u000a'))
    return Unit

# Main.{main_17}
def _idris_Main_46__123_main_95_17_125_(lift0, lift1):
  while True:
    if lift0[0] == 12:  # Python.Exceptions.FileNotFoundError
      return (65665, lift1)  # {U_Main.{main_15}_1}
    elif lift0[0] == 11:  # Python.Exceptions.OSError
      return (65666, lift1)  # {U_Main.{main_16}_1}
    else:
      return (65674, None, lift1)  # {U_Python.Exceptions.raise_1}
    return _idris_error("unreachable due to case in tail position")

# Python.Exceptions.{try_19}
def _idris_Python_46_Exceptions_46__123_try_95_19_125_(lift0):
  while True:
    return (0, lift0)  # Prelude.Either.Left

# Python.Exceptions.{try_20}
def _idris_Python_46_Exceptions_46__123_try_95_20_125_(lift0):
  while True:
    return (1, lift0)  # Prelude.Either.Right

# {Python.Prim.iterate:iter:0_lam_23}
def _idris__123_Python_46_Prim_46_iterate_58_iter_58_0_95_lam_95_23_125_(
  lift0, lift1, lift2
):
  while True:
    return (65684, None, None, None, None, None, None, None, None, lift0, lift2, lift1)  # {U_Python.Prim.iterate, iter_1}

# Python.Exceptions.{catch_____Python__Exceptions__idr_132_16_132_21_case_lam_24}
def _idris_Python_46_Exceptions_46__123_catch_95__95__95__95__95_Python_95__95_Exceptions_95__95_idr_95_132_95_16_95_132_95_21_95_case_95_lam_95_24_125_(
  lift0, lift1
):
  while True:
    return lift0

# Python.Prim.{next_____Python__Prim__idr_61_11_61_38_case_lam_25}
def _idris_Python_46_Prim_46__123_next_95__95__95__95__95_Python_95__95_Prim_95__95_idr_95_61_95_11_95_61_95_38_95_case_95_lam_95_25_125_(
  lift0
):
  while True:
    return None

# Python.Prim.{next_____Python__Prim__idr_61_11_61_38_case_lam_26}
def _idris_Python_46_Prim_46__123_next_95__95__95__95__95_Python_95__95_Prim_95__95_idr_95_61_95_11_95_61_95_38_95_case_95_lam_95_26_125_(
  lift0, lift1
):
  while True:
    return lift0

# Main.{main_example__idr_84_32_84_36_case_lam_29}
def _idris_Main_46__123_main_95_example_95__95_idr_95_84_95_32_95_84_95_36_95_case_95_lam_95_29_125_(
  lift0, lift1
):
  while True:
    in46 = sys.stdout.write(((u'  -> (2) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(lift0)) + u'\u000a'))
    return Unit

# Main.{main_example__idr_84_32_84_36_case_lam_30}
def _idris_Main_46__123_main_95_example_95__95_idr_95_84_95_32_95_84_95_36_95_case_95_lam_95_30_125_(
  lift0, lift1
):
  while True:
    in48 = sys.stdout.write(((u'  -> (1) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(lift0)) + u'\u000a'))
    return Unit

# Main.{main_example__idr_91_13_91_50_case_lam_31}
def _idris_Main_46__123_main_95_example_95__95_idr_95_91_95_13_95_91_95_50_95_case_95_lam_95_31_125_(
  lift0, lift1
):
  while True:
    in49 = sys.stdout.write(((u'  -> (2) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(lift0)) + u'\u000a'))
    return Unit

# Main.{main_example__idr_91_13_91_50_case_lam_32}
def _idris_Main_46__123_main_95_example_95__95_idr_95_91_95_13_95_91_95_50_95_case_95_lam_95_32_125_(
  lift0, lift1
):
  while True:
    in51 = sys.stdout.write(((u'  -> (2) everything\'s fine: ' + _idris_Python_46_Exceptions_46_showException(lift0)) + u'\u000a'))
    return Unit

# Main.{main_example__idr_91_13_91_50_case_lam_33}
def _idris_Main_46__123_main_95_example_95__95_idr_95_91_95_13_95_91_95_50_95_case_95_lam_95_33_125_(
  lift0
):
  while True:
    in54 = sys.stdout.write(u'Your root could probably use some security lessons!\u000a')
    return Unit

# Main.exports, greet
def _idris_Main_46_exports_58_greet_58_0(arg0, in1):
  while True:
    in2 = sys.stdout.write(((u'Hello ' + (arg0 + u'!')) + u'\u000a'))
    return Unit

# Python.Lib.Threading.forkPIO, worker
def _idris_Python_46_Lib_46_Threading_46_forkPIO_58_worker_58_0(
  arg0, arg1, arg2, in3
):
  while True:
    in4 = APPLY0(arg1, in3)
    return _idris_Python_46_Functions_46__36__46_(
      None,
      None,
      (1, (0,), (65681,)),  # Python.Telescope.Bind, Python.Telescope.Pi, {U_Python.Lib.Threading.{forkPIO_1}_1}
      _idris_Python_46_Fields_46__47__46_(None, None, arg2, u'put', None),
      None,
      (0, in4, Unit),  # Builtins.MkDPair
      in3
    )

# Python.Prim.iterate, iter
def _idris_Python_46_Prim_46_iterate_58_iter_58_0(
  arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10,
  in11
):
  while True:
    in12 = _idris_Python_46_Prim_46_next(None, arg8, in11)
    if in12 is not None:  # Prelude.Maybe.Just
      in17 = in12
      return _idris_io_95_bind(
        None,
        None,
        None,
        APPLY0(APPLY0(arg10, arg9), in17),
        (65691, arg8, arg10),  # {U_{Python.Prim.iterate:iter:0_lam_23}_1}
        in11
      )
    else:  # Prelude.Maybe.Nothing
      return arg9
    return _idris_error("unreachable due to case in tail position")

# Decidable.Equality.Decidable.Equality.Bool implementation of Decidable.Equality.DecEq, method decEq
def _idris_Decidable_46_Equality_46_Decidable_46_Equality_46__64_Decidable_46_Equality_46_DecEq_36_Bool_58__33_decEq_58_0(
  arg0, arg1
):
  while True:
    if not arg1:  # Prelude.Bool.False
      if not arg0:  # Prelude.Bool.False
        return (0,)  # Prelude.Basics.Yes
      else:  # Prelude.Bool.True
        return (1,)  # Prelude.Basics.No
      return _idris_error("unreachable due to case in tail position")
    else:  # Prelude.Bool.True
      if not arg0:  # Prelude.Bool.False
        return (1,)  # Prelude.Basics.No
      else:  # Prelude.Bool.True
        return (0,)  # Prelude.Basics.Yes
      return _idris_error("unreachable due to case in tail position")
    return _idris_error("unreachable due to case in tail position")

# Prelude.Foldable.Prelude.List.List implementation of Prelude.Foldable.Foldable, method foldr
def _idris_Prelude_46_Foldable_46_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List_58__33_foldr_58_0(
  arg0, arg1, arg2, arg3, arg4
):
  while True:
    if arg4:  # Prelude.List.::
      in5, in6 = arg4.head, arg4.tail
      return APPLY0(
        APPLY0(arg2, in5),
        _idris_Prelude_46_Foldable_46_Prelude_46_List_46__64_Prelude_46_Foldable_46_Foldable_36_List_58__33_foldr_58_0(
          None, None, arg2, arg3, in6
        )
      )
    else:  # Prelude.List.Nil
      return arg3
    return _idris_error("unreachable due to case in tail position")

# Prelude.Interfaces.Prelude.Interfaces.Integer implementation of Prelude.Interfaces.Ord, method compare
def _idris_Prelude_46_Interfaces_46_Prelude_46_Interfaces_46__64_Prelude_46_Interfaces_46_Ord_36_Integer_58__33_compare_58_0(
  arg0, arg1
):
  while True:
    aux1 = (arg0 == arg1)
    if aux1 == 0:
      aux2 = (arg0 < arg1)
      if aux2 == 0:
        return (2,)  # Prelude.Interfaces.GT
      else:
        return (0,)  # Prelude.Interfaces.LT
      return _idris_error("unreachable due to case in tail position")
    else:
      return (1,)  # Prelude.Interfaces.EQ
    return _idris_error("unreachable due to case in tail position")

# with block in Prelude.Interfaces.Prelude.Show.Prec implementation of Prelude.Interfaces.Ord, method >
def _idris__95_Prelude_46_Interfaces_46_Prelude_46_Show_46__64_Prelude_46_Interfaces_46_Ord_36_Prec_58__33__62__58_0_95_with_95_27(
  arg0, arg1, arg2
):
  while True:
    if arg0[0] == 2:  # Prelude.Interfaces.GT
      return True
    else:
      return False
    return _idris_error("unreachable due to case in tail position")

# with block in Prelude.Strings.strM
def _idris__95_Prelude_46_Strings_46_strM_95_with_95_32(arg0, arg1):
  while True:
    if arg1[0] == 1:  # Prelude.Basics.No
      return (0,)  # Prelude.Strings.StrNil
    else:  # Prelude.Basics.Yes
      return (1, arg0[0])  # Prelude.Strings.StrCons
    return _idris_error("unreachable due to case in tail position")

# with block in Prelude.Show.firstCharIs
def _idris__95_Prelude_46_Show_46_firstCharIs_95_with_95_45(arg0, arg1, arg2):
  while True:
    if arg2[0] == 1:  # Prelude.Strings.StrCons
      in3 = arg2[1]
      return APPLY0(arg0, in3)
    else:  # Prelude.Strings.StrNil
      return False
    return _idris_error("unreachable due to case in tail position")

# Python.Exceptions.case block in fromString at ./Python/Exceptions.idr:57:21
def _idris_Python_46_Exceptions_46_fromString_95__95__95__95__95_Python_95__95_Exceptions_95__95_idr_95_57_95_21_95_case(
  arg0, arg1
):
  while True:
    return {
      u'ArithmeticError': (3,),  # Python.Exceptions.ArithmeticError
      u'AssertionError': (7,),  # Python.Exceptions.AssertionError
      u'AttributeError': (8,),  # Python.Exceptions.AttributeError
      u'BufferError': (2,),  # Python.Exceptions.BufferError
      u'EOFError': (15,),  # Python.Exceptions.EOFError
      u'EnvironmentError': (9,),  # Python.Exceptions.EnvironmentError
      u'FileNotFoundError': (12,),  # Python.Exceptions.FileNotFoundError
      u'FloatingPointError': (4,),  # Python.Exceptions.FloatingPointError
      u'IOError': (10,),  # Python.Exceptions.IOError
      u'ImportError': (16,),  # Python.Exceptions.ImportError
      u'IndentationError': (27,),  # Python.Exceptions.IndentationError
      u'IndexError': (18,),  # Python.Exceptions.IndexError
      u'KeyError': (19,),  # Python.Exceptions.KeyError
      u'LookupError': (17,),  # Python.Exceptions.LookupError
      u'MemoryError': (20,),  # Python.Exceptions.MemoryError
      u'NameError': (21,),  # Python.Exceptions.NameError
      u'NotImplementedError': (25,),  # Python.Exceptions.NotImplementedError
      u'OSError': (11,),  # Python.Exceptions.OSError
      u'OverflowError': (5,),  # Python.Exceptions.OverflowError
      u'ReferenceError': (23,),  # Python.Exceptions.ReferenceError
      u'RuntimeError': (24,),  # Python.Exceptions.RuntimeError
      u'StandardError': (1,),  # Python.Exceptions.StandardError
      u'StopIteration': (0,),  # Python.Exceptions.StopIteration
      u'SyntaxError': (26,),  # Python.Exceptions.SyntaxError
      u'SystemError': (29,),  # Python.Exceptions.SystemError
      u'TabError': (28,),  # Python.Exceptions.TabError
      u'TypeError': (30,),  # Python.Exceptions.TypeError
      u'UnboundLocalError': (22,),  # Python.Exceptions.UnboundLocalError
      u'UnicodeDecodeError': (33,),  # Python.Exceptions.UnicodeDecodeError
      u'UnicodeEncodeError': (34,),  # Python.Exceptions.UnicodeEncodeError
      u'UnicodeError': (32,),  # Python.Exceptions.UnicodeError
      u'UnicodeTranslateError': (35,),  # Python.Exceptions.UnicodeTranslateError
      u'VMSError': (14,),  # Python.Exceptions.VMSError
      u'ValueError': (31,),  # Python.Exceptions.ValueError
      u'WindowsError': (13,),  # Python.Exceptions.WindowsError
      u'ZeroDivisionError': (6,)  # Python.Exceptions.ZeroDivisionError
    }.get(arg0, (36,))  # Python.Exceptions.Other

# Python.Exceptions.case block in try at ./Python/Exceptions.idr:108:16-118:29
def _idris_Python_46_Exceptions_46_try_95__95__95__95__95_Python_95__95_Exceptions_95__95_idr_95_108_95_16_95_118_95_29_95_case(
  arg0, arg1, arg2, arg3, arg4, in6
):
  while True:
    if arg3[0] == 0:  # Prelude.Either.Left
      in5 = arg3[1]
      return (
        1,  # Python.Exceptions.Except
        _idris_Python_46_Exceptions_46_fromString(
          _idris_Python_46_Fields_46__47__46_(
            None,
            None,
            _idris_Python_46_Fields_46__47__46_(None, None, in5, u'__class__', None),
            u'__name__',
            None
          )
        ),
        in5
      )
    else:  # Prelude.Either.Right
      in7 = arg3[1]
      return (0, in7)  # Python.Exceptions.OK
    return _idris_error("unreachable due to case in tail position")

# Python.Exceptions.case block in case block in try at ./Python/Exceptions.idr:108:16-118:29 at ./Python/Exceptions.idr:120:10
def _idris_Python_46_Exceptions_46_try_95__95__95__95__95_Python_95__95_Exceptions_95__95_idr_95_108_95_16_95_118_95_29_95_case_95__95__95__95__95_Python_95__95_Exceptions_95__95_idr_95_120_95_10_95_case(
  arg0, arg1, arg2, arg3, arg4, arg5, in7
):
  while True:
    if arg2[0] == 0:  # Prelude.Either.Left
      in6 = arg2[1]
      return (
        1,  # Python.Exceptions.Except
        _idris_Python_46_Exceptions_46_fromString(
          _idris_Python_46_Fields_46__47__46_(
            None,
            None,
            _idris_Python_46_Fields_46__47__46_(None, None, in6, u'__class__', None),
            u'__name__',
            None
          )
        ),
        in6
      )
    else:  # Prelude.Either.Right
      in8 = arg2[1]
      return (0, in8)  # Python.Exceptions.OK
    return _idris_error("unreachable due to case in tail position")

# Python.Exceptions.case block in catch at ./Python/Exceptions.idr:132:16-21
def _idris_Python_46_Exceptions_46_catch_95__95__95__95__95_Python_95__95_Exceptions_95__95_idr_95_132_95_16_95_132_95_21_95_case(
  arg0, arg1, arg2, arg3, arg4, arg5
):
  while True:
    if arg4[0] == 1:  # Python.Exceptions.Except
      in6, in7 = arg4[1:]
      return APPLY0(APPLY0(arg2, in6), in7)
    else:  # Python.Exceptions.OK
      in8 = arg4[1]
      return (65676, in8)  # {U_Python.Exceptions.{catch_____Python__Exceptions__idr_132_16_132_21_case_lam_24}_1}
    return _idris_error("unreachable due to case in tail position")

# Python.Prim.case block in next at ./Python/Prim.idr:61:11-38
def _idris_Python_46_Prim_46_next_95__95__95__95__95_Python_95__95_Prim_95__95_idr_95_61_95_11_95_61_95_38_95_case(
  arg0, arg1, arg2, arg3, arg4
):
  while True:
    if arg3[0] == 1:  # Python.Exceptions.Except
      in5, in6 = arg3[1:]
      if in5[0] == 0:  # Python.Exceptions.StopIteration
        return (65686,)  # {U_Python.Prim.{next_____Python__Prim__idr_61_11_61_38_case_lam_25}_1}
      else:
        return (65674, None, in6)  # {U_Python.Exceptions.raise_1}
      return _idris_error("unreachable due to case in tail position")
    else:  # Python.Exceptions.OK
      in8 = arg3[1]
      return (65687, in8)  # {U_Python.Prim.{next_____Python__Prim__idr_61_11_61_38_case_lam_26}_1}
    return _idris_error("unreachable due to case in tail position")

# Python.Prim.case block in Python.Prim.iterate, iter at ./Python/Prim.idr:84:17-23
def _idris_Python_46_Prim_46_Python_46_Prim_46_iterate_58_iter_58_0_95__95__95__95__95_Python_95__95_Prim_95__95_idr_95_84_95_17_95_84_95_23_95_case(
  arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10,
  arg11, arg12, arg13
):
  while True:
    if arg12 is not None:  # Prelude.Maybe.Just
      in14 = arg12
      return APPLY0(
        APPLY0(APPLY0(APPLY0(arg11, None), None), APPLY0(APPLY0(arg10, arg7), in14)),
        (65691, arg9, arg10)  # {U_{Python.Prim.iterate:iter:0_lam_23}_1}
      )
    else:  # Prelude.Maybe.Nothing
      return (65676, arg7)  # {U_Python.Exceptions.{catch_____Python__Exceptions__idr_132_16_132_21_case_lam_24}_1}
    return _idris_error("unreachable due to case in tail position")

# case block in io_bind at IO.idr:108:34-36
def _idris_io_95_bind_95_IO_95__95_idr_95_108_95_34_95_108_95_36_95_case(
  arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7
):
  while True:
    return APPLY0(arg7, arg5)

# Main.case block in main at example.idr:84:32-36
def _idris_Main_46_main_95_example_95__95_idr_95_84_95_32_95_84_95_36_95_case(
  arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10,
  arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19,
  arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28,
  arg29, arg30, arg31, arg32, arg33, arg34, arg35, arg36, arg37,
  arg38, arg39, arg40, arg41, arg42, arg43, arg44
):
  while True:
    if arg42[0] == 12:  # Python.Exceptions.FileNotFoundError
      return (65669, arg43)  # {U_Main.{main_example__idr_84_32_84_36_case_lam_29}_1}
    elif arg42[0] == 11:  # Python.Exceptions.OSError
      return (65670, arg43)  # {U_Main.{main_example__idr_84_32_84_36_case_lam_30}_1}
    else:
      return (65674, None, arg43)  # {U_Python.Exceptions.raise_1}
    return _idris_error("unreachable due to case in tail position")

# Main.case block in main at example.idr:91:13-50
def _idris_Main_46_main_95_example_95__95_idr_95_91_95_13_95_91_95_50_95_case(
  arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10,
  arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19,
  arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28,
  arg29, arg30, arg31, arg32, arg33, arg34, arg35, arg36, arg37,
  arg38, arg39, arg40, arg41, arg42, arg43, arg44, arg45
):
  while True:
    if arg44[0] == 1:  # Python.Exceptions.Except
      in46, in47 = arg44[1:]
      if in46[0] == 12:  # Python.Exceptions.FileNotFoundError
        return (65671, in47)  # {U_Main.{main_example__idr_91_13_91_50_case_lam_31}_1}
      elif in46[0] == 11:  # Python.Exceptions.OSError
        return (65672, in47)  # {U_Main.{main_example__idr_91_13_91_50_case_lam_32}_1}
      else:
        return (65674, None, in47)  # {U_Python.Exceptions.raise_1}
      return _idris_error("unreachable due to case in tail position")
    else:  # Python.Exceptions.OK
      in52 = arg44[1]
      return (65673,)  # {U_Main.{main_example__idr_91_13_91_50_case_lam_33}_1}
    return _idris_error("unreachable due to case in tail position")

# export: Main.exports, greet
def greet(arg1):
  APPLY0(_idris_Main_46_exports_58_greet_58_0(arg1), World)

if __name__ == '__main__':
  runMain0()
