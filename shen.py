"""
The License
-----------
The user is free to produce commercial applications with the software, to
distribute these applications in source or binary form, and to charge monies
for them as he sees fit and in concordance with the laws of the land subject
to the following license.

1. The license applies to all the software and all derived software and must
   appear on such.

2. It is illegal to distribute the software without this license attached to
   it and use of the software implies agreement with the license as such. It
   is illegal for anyone who is not the copyright holder to tamper with or
   change the license.

3. Neither the names of Lambda Associates or the copyright holder may be used
   to endorse or promote products built using the software without specific
   prior written permission from the copyright holder.

4. That possession of this license does not confer on the copyright holder any
   special contractual obligation towards the user. That in no event shall the
   copyright holder be liable for any direct, indirect, incidental, special,
   exemplary or consequential damages (including but not limited to
   procurement of substitute goods or services, loss of use, data, or profits;
   or business interruption), however caused and on any theory of liability,
   whether in contract, strict liability or tort (including negligence)
   arising in any way out of the use of the software, even if advised of the
   possibility of such damage.

5. It is permitted for the user to change the software, for the purpose of
   improving performance, correcting an error, or porting to a new platform,
   and distribute the modified version of Shen (hereafter the modified
   version) provided the resulting program conforms in all respects to the
   Shen standard and is issued under that title. The user must make it clear
   with his distribution that he/she is the author of the changes and what
   these changes are and why.

6. Derived versions of this software in whatever form are subject to the same
   restrictions. In particular it is not permitted to make derived copies of
   this software which do not conform to the Shen standard or appear under a
   different title.

7. It is permitted to distribute versions of Shen which incorporate libraries,
   graphics or other facilities which are not part of the Shen standard.

For an explication of this license see
[http://www.lambdassociates.org/News/june11/license.htm] which explains this
license in full.
"""


import sys
from pyshen import *

class SymDic:
    symdic_kl_x58x45 = Sym(':-')
    symdic_kl_mapcan = Sym('mapcan')
    symdic_V = Sym('V')
    symdic_shen_casesx45macro = Sym('shen.cases-macro')
    symdic_kl_integerx63 = Sym('integer?')
    symdic_kl_x58x61 = Sym(':=')
    symdic_shen_sysx45error = Sym('shen.sys-error')
    symdic_shen_explicit_modes = Sym('shen.explicit_modes')
    symdic_shen_free_variable_check = Sym('shen.free_variable_check')
    symdic_kl_inferences = Sym('inferences')
    symdic_shen_linearise_help = Sym('shen.linearise_help')
    symdic_shen_explodex45h = Sym('shen.explode-h')
    symdic_kl_tl = Sym('tl')
    symdic_shen_curryx45type = Sym('shen.curry-type')
    symdic_kl_adjoin = Sym('adjoin')
    symdic_shen_yacc = Sym('shen.yacc')
    symdic_kl_include = Sym('include')
    symdic_shen_incinfs = Sym('shen.incinfs')
    symdic_kl_tc = Sym('tc')
    symdic_shen_printx45pastx45inputs = Sym('shen.print-past-inputs')
    symdic_kl_booleanx63 = Sym('boolean?')
    symdic_kl_string = Sym('string')
    symdic_shen_procx45inputx43 = Sym('shen.proc-input+')
    symdic_shen_x45nullx45 = Sym('shen.-null-')
    symdic_P = Sym('P')
    symdic_shen_readx45charx45h = Sym('shen.read-char-h')
    symdic_kl_difference = Sym('difference')
    symdic_kl_readx45filex45asx45string = Sym('read-file-as-string')
    symdic_shen_ue = Sym('shen.ue')
    symdic_kl_reverse = Sym('reverse')
    symdic_kl_x42macrosx42 = Sym('*macros*')
    symdic_kl_list = Sym('list')
    symdic_kl_gensym = Sym('gensym')
    symdic_kl_consx63 = Sym('cons?')
    symdic_kl_vector = Sym('vector')
    symdic_shen_complexity = Sym('shen.complexity')
    symdic_shen_post = Sym('shen.post')
    symdic_kl_x45x62 = Sym('->')
    symdic_shen_assocx45macro = Sym('shen.assoc-macro')
    symdic_shen_constructx45premissx45literal = Sym('shen.construct-premiss-literal')
    symdic_kl_prologx63 = Sym('prolog?')
    symdic_shen_typetable = Sym('shen.typetable')
    symdic_kl_x42stinputx42 = Sym('*stinput*')
    symdic_kl_append = Sym('append')
    symdic_G = Sym('G')
    symdic_kl_vectorx63 = Sym('vector?')
    symdic_kl_x43 = Sym('+')
    symdic_shen_nextline = Sym('shen.nextline')
    symdic_kl_x64s = Sym('@s')
    symdic_kl_x64p = Sym('@p')
    symdic_kl_version = Sym('version')
    symdic_kl_x64v = Sym('@v')
    symdic_shen_synonymsx45help = Sym('shen.synonyms-help')
    symdic_kl_x59 = Sym(';')
    symdic_shen_em_help = Sym('shen.em_help')
    symdic_kl_undefmacro = Sym('undefmacro')
    symdic_kl_hash = Sym('hash')
    symdic_shen_x42datatypesx42 = Sym('shen.*datatypes*')
    symdic_K = Sym('K')
    symdic_kl_trapx45error = Sym('trap-error')
    symdic_shen_absx45macro = Sym('shen.abs-macro')
    symdic_kl_x60x45vector = Sym('<-vector')
    symdic_kl_let = Sym('let')
    symdic_kl_x38x38 = Sym('&&')
    symdic_shen_cl = Sym('shen.cl')
    symdic_kl_tlstr = Sym('tlstr')
    symdic_shen_prologx45macro = Sym('shen.prolog-macro')
    symdic_shen_toplevel_evaluate = Sym('shen.toplevel_evaluate')
    symdic_Stream = Sym('Stream')
    symdic_Record = Sym('Record')
    symdic_shen_bytex45x62digit = Sym('shen.byte->digit')
    symdic_shen_processx45datatype = Sym('shen.process-datatype')
    symdic_Freeze = Sym('Freeze')
    symdic_kl_x123 = Sym('{')
    symdic_shen_group_clauses = Sym('shen.group_clauses')
    symdic_kl_simplex45error = Sym('simple-error')
    symdic_shen_pvarx63 = Sym('shen.pvar?')
    symdic_kl_boolean = Sym('boolean')
    symdic_shen_collect = Sym('shen.collect')
    symdic_kl_unit = Sym('unit')
    symdic_kl_x60x45x45 = Sym('<--')
    symdic_shen_make_mu_application = Sym('shen.make_mu_application')
    symdic_shen_complexity_head = Sym('shen.complexity_head')
    symdic_shen_x42signedfuncsx42 = Sym('shen.*signedfuncs*')
    symdic_kl_tail = Sym('tail')
    symdic_kl_call = Sym('call')
    symdic_kl_type = Sym('type')
    symdic_kl_nx45x62string = Sym('n->string')
    symdic_kl_x60x61 = Sym('<=')
    symdic_shen_pvar = Sym('shen.pvar')
    symdic_F = Sym('F')
    symdic_shen_x42spyx42 = Sym('shen.*spy*')
    symdic_kl_stinput = Sym('stinput')
    symdic_shen_embedx45and = Sym('shen.embed-and')
    symdic_kl_cases = Sym('cases')
    symdic_shen_internx45type = Sym('shen.intern-type')
    symdic_shen_split_cc_rules = Sym('shen.split_cc_rules')
    symdic_shen_cc_body = Sym('shen.cc_body')
    symdic_shen_removetype = Sym('shen.removetype')
    symdic_kl_spy = Sym('spy')
    symdic_kl_stream = Sym('stream')
    symdic_shen_aritycheck = Sym('shen.aritycheck')
    symdic_shen_single = Sym('shen.single')
    symdic_shen_then = Sym('shen.then')
    symdic_shen_showx45assumptions = Sym('shen.show-assumptions')
    symdic_shen_readx45error = Sym('shen.read-error')
    symdic_kl_inputx43 = Sym('input+')
    symdic_shen_unbindv = Sym('shen.unbindv')
    symdic_kl_x33 = Sym('!')
    symdic_shen_unwindx45types = Sym('shen.unwind-types')
    symdic_shen_extract_vars = Sym('shen.extract_vars')
    symdic_kl_includex45allx45but = Sym('include-all-but')
    symdic_shen_removex45synonyms = Sym('shen.remove-synonyms')
    symdic_kl_emptyx63 = Sym('empty?')
    symdic_kl_x42homex45directoryx42 = Sym('*home-directory*')
    symdic_shen_rulesx45x62hornx45clauses = Sym('shen.rules->horn-clauses')
    symdic_shen_aum = Sym('shen.aum')
    symdic_kl_profile = Sym('profile')
    symdic_shen_nextx4550 = Sym('shen.next-50')
    symdic_kl_snd = Sym('snd')
    symdic_shen_failx33 = Sym('shen.fail!')
    symdic_shen_initialise_arity_table = Sym('shen.initialise_arity_table')
    symdic_shen_x42gensymx42 = Sym('shen.*gensym*')
    symdic_shen_x42varcounterx42 = Sym('shen.*varcounter*')
    symdic_kl_numberx63 = Sym('number?')
    symdic_shen_putx47getx45macro = Sym('shen.put/get-macro')
    symdic_kl_datatype = Sym('datatype')
    symdic_kl_bind = Sym('bind')
    symdic_kl_readx45byte = Sym('read-byte')
    symdic_ContextOut_1957 = Sym('ContextOut_1957')
    symdic_kl_readx45fromx45string = Sym('read-from-string')
    symdic_shen_analysex45variablex63 = Sym('shen.analyse-variable?')
    symdic_shen_x42synonymsx42 = Sym('shen.*synonyms*')
    symdic_shen_stack = Sym('shen.stack')
    symdic_kl_synonyms = Sym('synonyms')
    symdic_shen_reverse_help = Sym('shen.reverse_help')
    symdic_kl_systemf = Sym('systemf')
    symdic_kl_writex45tox45file = Sym('write-to-file')
    symdic_Finish = Sym('Finish')
    symdic_kl_failx45if = Sym('fail-if')
    symdic_kl_fix = Sym('fix')
    symdic_shen_f_error = Sym('shen.f_error')
    symdic_kl_x60 = Sym('<')
    symdic_shen_skip = Sym('shen.skip')
    symdic_kl_unifyx33 = Sym('unify!')
    symdic_shen_pre = Sym('shen.pre')
    symdic_shen_getx45profile = Sym('shen.get-profile')
    symdic_ProcessN = Sym('ProcessN')
    symdic_L = Sym('L')
    symdic_shen_mapx45h = Sym('shen.map-h')
    symdic_Out_1957 = Sym('Out_1957')
    symdic_kl_not = Sym('not')
    symdic_kl_fwhen = Sym('fwhen')
    symdic_kl_symbolx63 = Sym('symbol?')
    symdic_shen_failedx33 = Sym('shen.failed!')
    symdic_shen_x42infsx42 = Sym('shen.*infs*')
    symdic_shen_recursivelyx45print = Sym('shen.recursively-print')
    symdic_shen_void = Sym('shen.void')
    symdic_shen_r = Sym('shen.r')
    symdic_shen_s = Sym('shen.s')
    symdic_shen_x42maxinferencesx42 = Sym('shen.*maxinferences*')
    symdic_kl_mode = Sym('mode')
    symdic_shen_a = Sym('shen.a')
    symdic_shen_f = Sym('shen.f')
    symdic_A = Sym('A')
    symdic_kl_map = Sym('map')
    symdic_shen_compressx4550 = Sym('shen.compress-50')
    symdic_shen_inputx45track = Sym('shen.input-track')
    symdic_kl_out = Sym('out')
    symdic_kl_vectorx45x62 = Sym('vector->')
    symdic_shen_application_build = Sym('shen.application_build')
    symdic_kl_stringx45x62symbol = Sym('string->symbol')
    symdic_shen_x60st_inputx62 = Sym('shen.<st_input>')
    symdic_shen_list_variables = Sym('shen.list_variables')
    symdic_kl_print = Sym('print')
    symdic_shen_procx45nl = Sym('shen.proc-nl')
    symdic_shen_dereferencing = Sym('shen.dereferencing')
    symdic_shen_compose = Sym('shen.compose')
    symdic_kl_nth = Sym('nth')
    symdic_W = Sym('W')
    symdic_kl_put = Sym('put')
    symdic_Q = Sym('Q')
    symdic_shen_recursive_descent = Sym('shen.recursive_descent')
    symdic_shen_cons_form = Sym('shen.cons_form')
    symdic_shen_datatypex45error = Sym('shen.datatype-error')
    symdic_shen_x42installingx45klx42 = Sym('shen.*installing-kl*')
    symdic_kl_length = Sym('length')
    symdic_kl_readx45filex45asx45bytelist = Sym('read-file-as-bytelist')
    symdic_shen_choicepointx33 = Sym('shen.choicepoint!')
    symdic_kl_lambda = Sym('lambda')
    symdic_shen_else = Sym('shen.else')
    symdic_kl_x62x61 = Sym('>=')
    symdic_kl_x62x62 = Sym('>>')
    symdic_kl_number = Sym('number')
    symdic_kl_readx45file = Sym('read-file')
    symdic_shen_catchpoint = Sym('shen.catchpoint')
    symdic_Start = Sym('Start')
    symdic_kl_occurrences = Sym('occurrences')
    symdic_shen_lazyderef = Sym('shen.lazyderef')
    symdic_shen_syntax = Sym('shen.syntax')
    symdic_shen_callx45rest = Sym('shen.call-rest')
    symdic_kl_open = Sym('open')
    symdic_shen_x42shenx45typex45theoryx45enabledx63x42 = Sym('shen.*shen-type-theory-enabled?*')
    symdic_shen_datatypex45macro = Sym('shen.datatype-macro')
    symdic_B = Sym('B')
    symdic_kl_thaw = Sym('thaw')
    symdic_kl_preclude = Sym('preclude')
    symdic_kl_variablex63 = Sym('variable?')
    symdic_kl_x42implementationx42 = Sym('*implementation*')
    symdic_shen_multiplex45set = Sym('shen.multiple-set')
    symdic_kl_arity = Sym('arity')
    symdic_R = Sym('R')
    symdic_kl_getx45time = Sym('get-time')
    symdic_shen_x60defprologx62 = Sym('shen.<defprolog>')
    symdic_kl_x61x61x62 = Sym('==>')
    symdic_optimise = Sym('optimise')
    symdic_shen_x60sigx43rulesx62 = Sym('shen.<sig+rules>')
    symdic_kl_untrack = Sym('untrack')
    symdic_shen_the = Sym('shen.the')
    symdic_shen_aritycheckx45action = Sym('shen.aritycheck-action')
    symdic_shen_aum_to_shen = Sym('shen.aum_to_shen')
    symdic_kl_str = Sym('str')
    symdic_kl_and = Sym('and')
    symdic_shen_demodh = Sym('shen.demodh')
    symdic_shen_synonymsx45macro = Sym('shen.synonyms-macro')
    symdic_shen_controlx45chars = Sym('shen.control-chars')
    symdic_shen_rename = Sym('shen.rename')
    symdic_shen_chwild = Sym('shen.chwild')
    symdic_shen_nlx45macro = Sym('shen.nl-macro')
    symdic_kl_null = Sym('null')
    symdic_shen_x43vectorx63 = Sym('shen.+vector?')
    symdic_shen_truncate = Sym('shen.truncate')
    symdic_kl_x45 = Sym('-')
    symdic_shen_of = Sym('shen.of')
    symdic_shen_deref = Sym('shen.deref')
    symdic_kl_destroy = Sym('destroy')
    symdic_kl_x61 = Sym('=')
    symdic_shen_outputx45track = Sym('shen.output-track')
    symdic_Qv = Sym('Qv')
    symdic_kl_track = Sym('track')
    symdic_M = Sym('M')
    symdic_kl_assoc = Sym('assoc')
    symdic_shen_hdtl = Sym('shen.hdtl')
    symdic_x42hushx42 = Sym('*hush*')
    symdic_kl_x42maximumx45printx45sequencex45sizex42 = Sym('*maximum-print-sequence-size*')
    symdic_shen_source = Sym('shen.source')
    symdic_kl_x125 = Sym('}')
    symdic_shen_find = Sym('shen.find')
    symdic_shen_encodex45choices = Sym('shen.encode-choices')
    symdic_kl_x42propertyx45vectorx42 = Sym('*property-vector*')
    symdic_shen_split_cc_rule = Sym('shen.split_cc_rule')
    symdic_kl_x42portersx42 = Sym('*porters*')
    symdic_shen_outx45ofx45bounds = Sym('shen.out-of-bounds')
    symdic_shen_semantics = Sym('shen.semantics')
    symdic_kl_macroexpand = Sym('macroexpand')
    symdic_Parse_Y = Sym('Parse_Y')
    symdic_Parse_X = Sym('Parse_X')
    symdic_shen_rightx45x62left = Sym('shen.right->left')
    symdic_shen_casex45form = Sym('shen.case-form')
    symdic_kl_x42versionx42 = Sym('*version*')
    symdic_Assumption_1957 = Sym('Assumption_1957')
    symdic_shen_callx45help = Sym('shen.call-help')
    symdic_kl_hdstr = Sym('hdstr')
    symdic_kl_do = Sym('do')
    symdic_shen_x42catchx42 = Sym('shen.*catch*')
    symdic_kl_get = Sym('get')
    symdic_kl_x61x61 = Sym('==')
    symdic_H = Sym('H')
    symdic_shen_tests = Sym('shen.tests')
    symdic_kl_x61x33 = Sym('=!')
    symdic_shen_packagex45contents = Sym('shen.package-contents')
    symdic_X = Sym('X')
    symdic_shen_insertx45predicate = Sym('shen.insert-predicate')
    symdic_shen_nonx45empty = Sym('shen.non-empty')
    symdic_kl_enablex45typex45theory = Sym('enable-type-theory')
    symdic_shen_check_stream = Sym('shen.check_stream')
    symdic_kl_remove = Sym('remove')
    symdic_kl_where = Sym('where')
    symdic_kl_set = Sym('set')
    symdic_kl_lazy = Sym('lazy')
    symdic_kl_freeze = Sym('freeze')
    symdic_shen_defmacrox45macro = Sym('shen.defmacro-macro')
    symdic_kl_fail = Sym('fail')
    symdic_kl_close = Sym('close')
    symdic_shen_evalx45withoutx45macros = Sym('shen.eval-without-macros')
    symdic_shen_insert = Sym('shen.insert')
    symdic_shen_intprologx45help = Sym('shen.intprolog-help')
    symdic_shen_externalx45symbols = Sym('shen.external-symbols')
    symdic_shen_linearise = Sym('shen.linearise')
    symdic_C = Sym('C')
    symdic_shen_outputx45macro = Sym('shen.output-macro')
    symdic_shen_functionx45macro = Sym('shen.function-macro')
    symdic_kl_barx33 = Sym('bar!')
    symdic_shen_x42alphabetx42 = Sym('shen.*alphabet*')
    symdic_shen_thisx45symbolx45isx45unbound = Sym('shen.this-symbol-is-unbound')
    symdic_kl_specialise = Sym('specialise')
    symdic_kl_protect = Sym('protect')
    symdic_shen_newpv = Sym('shen.newpv')
    symdic_kl_tlv = Sym('tlv')
    symdic_shen_reduce = Sym('shen.reduce')
    symdic_kl_errorx45tox45string = Sym('error-to-string')
    symdic_S = Sym('S')
    symdic_shen_x42stepx42 = Sym('shen.*step*')
    symdic_shen_constructx45sidex45literals = Sym('shen.construct-side-literals')
    symdic_Result = Sym('Result')
    symdic_shen_alphanumsx63 = Sym('shen.alphanums?')
    symdic_shen_insertx45prologx45variablesx45help = Sym('shen.insert-prolog-variables-help')
    symdic_shen_x42prologvectorsx42 = Sym('shen.*prologvectors*')
    symdic_shen_mult_subst = Sym('shen.mult_subst')
    symdic_kl_precludex45allx45but = Sym('preclude-all-but')
    symdic_shen_errorx45macro = Sym('shen.error-macro')
    symdic_kl_load = Sym('load')
    symdic_shen_x42processx45counterx42 = Sym('shen.*process-counter*')
    symdic_kl_cn = Sym('cn')
    symdic_kl_pos = Sym('pos')
    symdic_shen_timerx45macro = Sym('shen.timer-macro')
    symdic_kl_cd = Sym('cd')
    symdic_shen_x42trackingx42 = Sym('shen.*tracking*')
    symdic_kl_x45x45x62 = Sym('-->')
    symdic_shen_x42historyx42 = Sym('shen.*history*')
    symdic_kl_loaded = Sym('loaded')
    symdic_kl_pr = Sym('pr')
    symdic_kl_ps = Sym('ps')
    symdic_shen_mu = Sym('shen.mu')
    symdic_kl_union = Sym('union')
    symdic_shen_removex45h = Sym('shen.remove-h')
    symdic_kl_stoutput = Sym('stoutput')
    symdic_shen_x60definex62 = Sym('shen.<define>')
    symdic_kl_define = Sym('define')
    symdic_shen_terprix45orx45readx45char = Sym('shen.terpri-or-read-char')
    symdic_Time = Sym('Time')
    symdic_shen_call_the_continuation = Sym('shen.call_the_continuation')
    symdic_kl_occursx45check = Sym('occurs-check')
    symdic_N = Sym('N')
    symdic_shen_elimx45define = Sym('shen.elim-define')
    symdic_kl_external = Sym('external')
    symdic_shen_x42occursx42 = Sym('shen.*occurs*')
    symdic_shen_app = Sym('shen.app')
    symdic_x42stoutputx42 = Sym('*stoutput*')
    symdic_kl_hdv = Sym('hdv')
    symdic_kl_exception = Sym('exception')
    symdic_kl_unify = Sym('unify')
    symdic_shen_clause_form = Sym('shen.clause_form')
    symdic_shen_sx45prolog_literal = Sym('shen.s-prolog_literal')
    symdic_Continuation = Sym('Continuation')
    symdic_shen_prhush = Sym('shen.prhush')
    symdic_kl_value = Sym('value')
    symdic_kl_compile = Sym('compile')
    symdic_shen_variable = Sym('shen.variable')
    symdic_kl_error = Sym('error')
    symdic_shen_letx45macro = Sym('shen.let-macro')
    symdic_shen_x42readerx45macrosx42 = Sym('shen.*reader-macros*')
    symdic_shen_typex45signaturex45ofx45 = Sym('shen.type-signature-of-')
    symdic_shen_variablex45match = Sym('shen.variable-match')
    symdic_kl_cons = Sym('cons')
    symdic_kl_is = Sym('is')
    symdic_shen_x60sigx43restx62 = Sym('shen.<sig+rest>')
    symdic_shen_tx42 = Sym('shen.t*')
    symdic_kl_cond = Sym('cond')
    symdic_kl_in = Sym('in')
    symdic_kl_x60x45 = Sym('<-')
    symdic_shen_x42systemx42 = Sym('shen.*system*')
    symdic_kl_if = Sym('if')
    symdic_kl_verified = Sym('verified')
    symdic_shen_x42specialx42 = Sym('shen.*special*')
    symdic_kl_defun = Sym('defun')
    symdic_shen_tuple = Sym('shen.tuple')
    symdic_shen_jump_stream = Sym('shen.jump_stream')
    symdic_I = Sym('I')
    symdic_shen_sx45prolog_clause = Sym('shen.s-prolog_clause')
    symdic_readx43 = Sym('read+')
    symdic_shen_product = Sym('shen.product')
    symdic_shen_makex45stringx45macro = Sym('shen.make-string-macro')
    symdic_shen_to = Sym('shen.to')
    symdic_Y = Sym('Y')
    symdic_shen_prologx45aritycheck = Sym('shen.prolog-aritycheck')
    symdic_kl_x42languagex42 = Sym('*language*')
    symdic_kl_x47_ = Sym('/.')
    symdic_kl_macro = Sym('macro')
    symdic_shen_mkstrx45l = Sym('shen.mkstr-l')
    symdic_shen_mkstrx45r = Sym('shen.mkstr-r')
    symdic_shen_x64sx45macro = Sym('shen.@s-macro')
    symdic_shen_plugx45wildcards = Sym('shen.plug-wildcards')
    symdic_shen_ok = Sym('shen.ok')
    symdic_shen_rulex45x62hornx45clause = Sym('shen.rule->horn-clause')
    symdic_shen_newcontinuation = Sym('shen.newcontinuation')
    symdic_shen_sndx45orx45fail = Sym('shen.snd-or-fail')
    symdic_shen_compile_to_kl = Sym('shen.compile_to_kl')
    symdic_shen_be = Sym('shen.be')
    symdic_kl_defcc = Sym('defcc')
    symdic_shen_compilex45macro = Sym('shen.compile-macro')
    symdic_kl_cut = Sym('cut')
    symdic_kl_x36 = Sym('$')
    symdic_shen_variables = Sym('shen.variables')
    symdic_shen_intprolog = Sym('shen.intprolog')
    symdic_kl_identical = Sym('identical')
    symdic_kl_tcx63 = Sym('tc?')
    symdic_D = Sym('D')
    symdic_format = Sym('format')
    symdic_shen_head_abstraction = Sym('shen.head_abstraction')
    symdic_kl_maxinferences = Sym('maxinferences')
    symdic_shen_x43stringx63 = Sym('shen.+string?')
    symdic_T = Sym('T')
    symdic_shen_result = Sym('shen.result')
    symdic_shen_curry = Sym('shen.curry')
    symdic_kl_intersection = Sym('intersection')
    symdic_shen_compile_prolog_procedure = Sym('shen.compile_prolog_procedure')
    symdic_shen_x42tcx42 = Sym('shen.*tc*')
    symdic_kl_makex45string = Sym('make-string')
    symdic_kl_output = Sym('output')
    symdic_Context1_1957 = Sym('Context1_1957')
    symdic_kl_tuplex63 = Sym('tuple?')
    symdic_shen_leftx45rule = Sym('shen.left-rule')
    symdic_shen_x42optimisex42 = Sym('shen.*optimise*')
    symdic_shen_x42alldatatypesx42 = Sym('shen.*alldatatypes*')
    symdic_shen_abstraction_build = Sym('shen.abstraction_build')
    symdic_shen_x42extraspecialx42 = Sym('shen.*extraspecial*')
    symdic_shen_insertx45h = Sym('shen.insert-h')
    symdic_shen_assumetype = Sym('shen.assumetype')
    symdic_shen_x60x45sem = Sym('shen.<-sem')
    symdic_kl_explode = Sym('explode')
    symdic_shen_same_predicatex63 = Sym('shen.same_predicate?')
    symdic_shen_x42callx42 = Sym('shen.*call*')
    symdic_kl_x47 = Sym('/')
    symdic_kl_defprolog = Sym('defprolog')
    symdic_Throwcontrol = Sym('Throwcontrol')
    symdic_kl_run = Sym('run')
    symdic_Parse_ = Sym('Parse_')
    symdic_O = Sym('O')
    symdic_shen_bindv = Sym('shen.bindv')
    symdic_kl_step = Sym('step')
    symdic_shen_typecheckx45andx45load = Sym('shen.typecheck-and-load')
    symdic_kl__ = Sym('_')
    symdic_kl_x42portx42 = Sym('*port*')
    symdic_shen_cslx45help = Sym('shen.csl-help')
    symdic_shen_intprologx45helpx45help = Sym('shen.intprolog-help-help')
    symdic_kl_package = Sym('package')
    symdic_shen_double = Sym('shen.double')
    symdic_shen_default_semantics = Sym('shen.default_semantics')
    symdic_kl_unprofile = Sym('unprofile')
    symdic_shen_x60datatypex45rulesx62 = Sym('shen.<datatype-rules>')
    symdic_Message = Sym('Message')
    symdic_shen_trackx45function = Sym('shen.track-function')
    symdic_kl_or = Sym('or')
    symdic_shen_walk = Sym('shen.walk')
    symdic_shen_first_n = Sym('shen.first_n')
    symdic_In_1957 = Sym('In_1957')
    symdic_shen_putx45profile = Sym('shen.put-profile')
    symdic_shen_constructx45searchx45clauses = Sym('shen.construct-search-clauses')
    symdic_shen_abstract_rule = Sym('shen.abstract_rule')
    symdic_kl_boundx63 = Sym('bound?')
    symdic_kl_unspecialise = Sym('unspecialise')
    symdic_kl_x42 = Sym('*')
    symdic_Context_1957 = Sym('Context_1957')
    symdic_shen_sum = Sym('shen.sum')
    symdic_kl_x58 = Sym(':')
    symdic_kl_function = Sym('function')
    symdic_shen_analysex45symbolx63 = Sym('shen.analyse-symbol?')
    symdic_kl_head = Sym('head')
    symdic_J = Sym('J')
    symdic_kl_defmacro = Sym('defmacro')
    symdic_shen_pop = Sym('shen.pop')
    symdic_Z = Sym('Z')
    symdic_kl_hd = Sym('hd')
    symdic_shen_modh = Sym('shen.modh')
    symdic_kl_limit = Sym('limit')
    symdic_shen_stripx45protect = Sym('shen.strip-protect')
    symdic_kl_x62 = Sym('>')
    symdic_shen_nestx45disjunct = Sym('shen.nest-disjunct')
    symdic_shen_procedure_name = Sym('shen.procedure_name')
    symdic_shen_pair = Sym('shen.pair')
    symdic_shen_cutpoint = Sym('shen.cutpoint')
    symdic_Assumptions_1957 = Sym('Assumptions_1957')
    symdic_shen_x42teststackx42 = Sym('shen.*teststack*')
    symdic_shen_insertx45l = Sym('shen.insert-l')
    symdic_kl_x60ex62 = Sym('<e>')
    symdic_kl_elementx63 = Sym('element?')
    symdic_kl_stringx45x62n = Sym('string->n')
    symdic_shen_constructx45context = Sym('shen.construct-context')
    symdic_kl_file = Sym('file')
    symdic_shen_leavex33 = Sym('shen.leave!')
    symdic_shen_afterx45codepoint = Sym('shen.after-codepoint')
    symdic_shen_linearisex45clause = Sym('shen.linearise-clause')
    symdic_kl_nl = Sym('nl')
    symdic_shen_changex45pointerx45value = Sym('shen.change-pointer-value')
    symdic_shen_stripx45pathname = Sym('shen.strip-pathname')
    symdic_kl_when = Sym('when')
    symdic_kl_stringx63 = Sym('string?')
    symdic_kl_absvectorx63 = Sym('absvector?')
    symdic_shen_x42maxcomplexityx42 = Sym('shen.*maxcomplexity*')
    symdic_shen_rememberx45datatype = Sym('shen.remember-datatype')
    symdic_shen_defprologx45macro = Sym('shen.defprolog-macro')
    symdic_Case = Sym('Case')
    symdic_kl_yx45orx45nx63 = Sym('y-or-n?')
    symdic_x60x33x62 = Sym('<!>')
    symdic_E = Sym('E')
    symdic_shen_continuation = Sym('shen.continuation')
    symdic_kl_symbol = Sym('symbol')
    symdic_kl_profilex45results = Sym('profile-results')
    symdic_U = Sym('U')
    symdic_Context = Sym('Context')
    symdic_shen_multiples = Sym('shen.multiples')
    symdic_kl_fst = Sym('fst')
    symdic_kl_time = Sym('time')
symdic = SymDic()
FUNCTIONS.update({'or': shen_or, 'and': shen_and})
VARS.update({'*language*': 'Python', '*implementation*': 'pyshen', '*release*': "", '*port*': "0.135", '*porters*': 'Matthieu Lagacherie and Yannick Drant', '*home-directory*': '~/', '*stinput*': sys.stdin, '*stoutput*': sys.stdout, '*version*': "version 11"})


#============================== toplevel.kl==============================



@tail_recursion
def shen_shen():
    global symdic
    return [tco_apply(shen_credits, []), tail_call(shen_loop, [])][(-1)]
shen_add_fun('shen.shen', shen_shen)

@tail_recursion
def shen_loop():
    global symdic
    return [tco_apply(shen_initialise_environment, []), [tco_apply(shen_prompt, []), [shen_try_except((lambda : tco_apply(shen_readx45evaluatex45print, [])), (lambda KL_ARG_E_0: shen_pr(KL_ARG_E_0.message, tco_apply(kl_stoutput, [])))), tail_call(shen_loop, [])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.loop', shen_loop)

@tail_recursion
def kl_version(KL_ARG_V2308_1):
    global symdic
    return shen_set(symdic.symdic_kl_x42versionx42, KL_ARG_V2308_1)
shen_add_fun('version', kl_version)
tail_call(kl_version, ['version 11'])

@tail_recursion
def shen_credits():
    global symdic
    return [tco_apply(shen_prhush, ['\r\nShen 2010, copyright (C) 2010 Mark Tarver\r\n', tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, ['released under the Shen license\r\n', tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, [('www.shenlanguage.org, ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42versionx42), '\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), [tco_apply(shen_prhush, [('running under ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42languagex42), (', implementation: ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42implementationx42), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), tail_call(shen_prhush, [('\r\nport ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portx42), (' ported by ' + tco_apply(shen_app, [shen_get(symdic.symdic_kl_x42portersx42), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.credits', shen_credits)

@tail_recursion
def shen_initialise_environment():
    global symdic
    return tail_call(shen_multiplex45set, [[symdic.symdic_shen_x42callx42, [0, [symdic.symdic_shen_x42infsx42, [0, [symdic.symdic_shen_x42processx45counterx42, [0, [symdic.symdic_shen_x42catchx42, [0, []]]]]]]]]])
shen_add_fun('shen.initialise_environment', shen_initialise_environment)

@tail_recursion
def shen_multiplex45set(KL_ARG_V2309_2):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2309_2) else ([shen_set(KL_ARG_V2309_2[0], KL_ARG_V2309_2[1][0]), tail_call(shen_multiplex45set, [KL_ARG_V2309_2[1][1]])][(-1)] if (shen_consp(KL_ARG_V2309_2[1]) if shen_consp(KL_ARG_V2309_2) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiplex45set]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiple-set', shen_multiplex45set)

@tail_recursion
def kl_destroy(KL_ARG_V2310_3):
    global symdic
    return apply(kl_declare, [KL_ARG_V2310_3, []])
shen_add_fun('destroy', kl_destroy)
shen_set(symdic.symdic_shen_x42historyx42, [])

@tail_recursion
def shen_readx45evaluatex45print():

    class KL_Context:
        KL_LOC_Lineread_4 = None
        KL_LOC_History_5 = None
        KL_LOC_NewLineread_6 = None
        KL_LOC_NewHistory_7 = None
        KL_LOC_Parsed_8 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Lineread_4', tco_apply(shen_toplineread, [])), [setattr(KL_CTX, 'KL_LOC_History_5', shen_get(symdic.symdic_shen_x42historyx42)), [setattr(KL_CTX, 'KL_LOC_NewLineread_6', tco_apply(shen_retrievex45fromx45historyx45ifx45needed, [KL_CTX.KL_LOC_Lineread_4, KL_CTX.KL_LOC_History_5])), [setattr(KL_CTX, 'KL_LOC_NewHistory_7', tco_apply(shen_update_history, [KL_CTX.KL_LOC_NewLineread_6, KL_CTX.KL_LOC_History_5])), [setattr(KL_CTX, 'KL_LOC_Parsed_8', tco_apply(kl_fst, [KL_CTX.KL_LOC_NewLineread_6])), tail_call(shen_toplevel, [KL_CTX.KL_LOC_Parsed_8])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.read-evaluate-print', shen_readx45evaluatex45print)

@tail_recursion
def shen_retrievex45fromx45historyx45ifx45needed(KL_ARG_V2320_9, KL_ARG_V2321_10):

    class KL_Context:
        KL_LOC_PastPrint_11 = None
        KL_LOC_Keyx63_12 = None
        KL_LOC_Find_13 = None
        KL_LOC_PastPrint_14 = None
        KL_LOC_Keyx63_16 = None
        KL_LOC_Pastprint_17 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_PastPrint_11', tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_ARG_V2321_10[0]])])), KL_ARG_V2321_10[0]][(-1)] if ((((((shen_eq(tco_apply(kl_snd, [KL_ARG_V2320_9])[1][0], tco_apply(shen_exclamation, [])) if shen_eq(tco_apply(kl_snd, [KL_ARG_V2320_9])[0], tco_apply(shen_exclamation, [])) else False) if shen_consp(KL_ARG_V2321_10) else False) if shen_eq([], tco_apply(kl_snd, [KL_ARG_V2320_9])[1][1]) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])[1]) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_12', tco_apply(shen_makex45key, [tco_apply(kl_snd, [KL_ARG_V2320_9])[1], KL_ARG_V2321_10])), [setattr(KL_CTX, 'KL_LOC_Find_13', tco_apply(kl_head, [tco_apply(shen_findx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_12, KL_ARG_V2321_10])])), [setattr(KL_CTX, 'KL_LOC_PastPrint_14', tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_CTX.KL_LOC_Find_13])])), KL_CTX.KL_LOC_Find_13][(-1)]][(-1)]][(-1)] if ((shen_eq(tco_apply(kl_snd, [KL_ARG_V2320_9])[0], tco_apply(shen_exclamation, [])) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else ([tco_apply(shen_printx45pastx45inputs, [(lambda KL_ARG_X_15: True), tco_apply(kl_reverse, [KL_ARG_V2321_10]), 0]), tail_call(kl_abort, [])][(-1)] if (((shen_eq(tco_apply(kl_snd, [KL_ARG_V2320_9])[0], tco_apply(shen_percent, [])) if shen_eq([], tco_apply(kl_snd, [KL_ARG_V2320_9])[1]) else False) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else ([setattr(KL_CTX, 'KL_LOC_Keyx63_16', tco_apply(shen_makex45key, [tco_apply(kl_snd, [KL_ARG_V2320_9])[1], KL_ARG_V2321_10])), [setattr(KL_CTX, 'KL_LOC_Pastprint_17', tco_apply(shen_printx45pastx45inputs, [KL_CTX.KL_LOC_Keyx63_16, tco_apply(kl_reverse, [KL_ARG_V2321_10]), 0])), tail_call(kl_abort, [])][(-1)]][(-1)] if ((shen_eq(tco_apply(kl_snd, [KL_ARG_V2320_9])[0], tco_apply(shen_percent, [])) if shen_consp(tco_apply(kl_snd, [KL_ARG_V2320_9])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V2320_9]) else False) else (KL_ARG_V2320_9 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.retrieve-from-history-if-needed', shen_retrievex45fromx45historyx45ifx45needed)

@tail_recursion
def shen_percent():
    global symdic
    return 37
shen_add_fun('shen.percent', shen_percent)

@tail_recursion
def shen_exclamation():
    global symdic
    return 33
shen_add_fun('shen.exclamation', shen_exclamation)

@tail_recursion
def shen_prbytes(KL_ARG_V2322_18):
    global symdic
    return [tco_apply(kl_map, [(lambda KL_ARG_Byte_19: shen_pr(chr(KL_ARG_Byte_19), tco_apply(kl_stoutput, []))), KL_ARG_V2322_18]), tail_call(kl_nl, [1])][(-1)]
shen_add_fun('shen.prbytes', shen_prbytes)

@tail_recursion
def shen_update_history(KL_ARG_V2323_20, KL_ARG_V2324_21):
    global symdic
    return shen_set(symdic.symdic_shen_x42historyx42, [KL_ARG_V2323_20, KL_ARG_V2324_21])
shen_add_fun('shen.update_history', shen_update_history)

@tail_recursion
def shen_toplineread():
    global symdic
    return tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), []])
shen_add_fun('shen.toplineread', shen_toplineread)

@tail_recursion
def shen_toplineread_loop(KL_ARG_V2326_22, KL_ARG_V2327_23):

    class KL_Context:
        KL_LOC_Line_24 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if shen_eq(KL_ARG_V2326_22, tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_24', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2327_23, (lambda KL_ARG_E_25: symdic.symdic_shen_nextline)])), (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2327_23, [KL_ARG_V2326_22, []]])]) if (True if shen_eq(KL_CTX.KL_LOC_Line_24, symdic.symdic_shen_nextline) else tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_24])) else tail_call(kl_x64p, [KL_CTX.KL_LOC_Line_24, KL_ARG_V2327_23]))][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V2326_22, [tco_apply(shen_newline, []), [tco_apply(shen_carriagex45return, []), []]]]) else (tail_call(shen_toplineread_loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V2327_23, [KL_ARG_V2326_22, []]])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.toplineread_loop', shen_toplineread_loop)

@tail_recursion
def shen_hat():
    global symdic
    return 94
shen_add_fun('shen.hat', shen_hat)

@tail_recursion
def shen_newline():
    global symdic
    return 10
shen_add_fun('shen.newline', shen_newline)

@tail_recursion
def shen_carriagex45return():
    global symdic
    return 13
shen_add_fun('shen.carriage-return', shen_carriagex45return)

@tail_recursion
def kl_tc(KL_ARG_V2332_26):
    global symdic
    return (shen_set(symdic.symdic_shen_x42tcx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2332_26) else (shen_set(symdic.symdic_shen_x42tcx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2332_26) else (shen_simple_error('tc expects a + or -') if True else shen_simple_error('condition failure'))))
shen_add_fun('tc', kl_tc)

@tail_recursion
def shen_prompt():
    global symdic
    return (tail_call(shen_prhush, [('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '+) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if shen_get(symdic.symdic_shen_x42tcx42) else tail_call(shen_prhush, [('\r\n\r\n(' + tco_apply(shen_app, [tco_apply(kl_length, [shen_get(symdic.symdic_shen_x42historyx42)]), '-) ', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]))
shen_add_fun('shen.prompt', shen_prompt)

@tail_recursion
def shen_toplevel(KL_ARG_V2333_27):
    global symdic
    return tail_call(shen_toplevel_evaluate, [KL_ARG_V2333_27, shen_get(symdic.symdic_shen_x42tcx42)])
shen_add_fun('shen.toplevel', shen_toplevel)

@tail_recursion
def shen_findx45pastx45inputs(KL_ARG_V2334_28, KL_ARG_V2335_29):

    class KL_Context:
        KL_LOC_F_30 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_30', tco_apply(shen_find, [KL_ARG_V2334_28, KL_ARG_V2335_29])), (shen_simple_error('input not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_F_30]) else KL_CTX.KL_LOC_F_30)][(-1)]
shen_add_fun('shen.find-past-inputs', shen_findx45pastx45inputs)

@tail_recursion
def shen_makex45key(KL_ARG_V2336_31, KL_ARG_V2337_32):

    class KL_Context:
        KL_LOC_Atom_33 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Atom_33', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V2336_31, (lambda KL_ARG_E_34: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_34, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_34) else shen_simple_error('parse error\r\n')))])[0]), ((lambda KL_ARG_X_35: shen_eq(KL_ARG_X_35, tco_apply(kl_nth, [(KL_CTX.KL_LOC_Atom_33 + 1), tco_apply(kl_reverse, [KL_ARG_V2337_32])]))) if tco_apply(kl_integerx63, [KL_CTX.KL_LOC_Atom_33]) else (lambda KL_ARG_X_36: tail_call(shen_prefixx63, [KL_ARG_V2336_31, tco_apply(shen_trimx45gubbins, [tco_apply(kl_snd, [KL_ARG_X_36])])])))][(-1)]
shen_add_fun('shen.make-key', shen_makex45key)

@tail_recursion
def shen_trimx45gubbins(KL_ARG_V2338_37):
    global symdic
    return (tail_call(shen_trimx45gubbins, [KL_ARG_V2338_37[1]]) if (shen_eq(KL_ARG_V2338_37[0], tco_apply(shen_space, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2338_37[1]]) if (shen_eq(KL_ARG_V2338_37[0], tco_apply(shen_newline, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2338_37[1]]) if (shen_eq(KL_ARG_V2338_37[0], tco_apply(shen_carriagex45return, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2338_37[1]]) if (shen_eq(KL_ARG_V2338_37[0], tco_apply(shen_tab, [])) if shen_consp(KL_ARG_V2338_37) else False) else (tail_call(shen_trimx45gubbins, [KL_ARG_V2338_37[1]]) if (shen_eq(KL_ARG_V2338_37[0], tco_apply(shen_leftx45round, [])) if shen_consp(KL_ARG_V2338_37) else False) else (KL_ARG_V2338_37 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.trim-gubbins', shen_trimx45gubbins)

@tail_recursion
def shen_space():
    global symdic
    return 32
shen_add_fun('shen.space', shen_space)

@tail_recursion
def shen_tab():
    global symdic
    return 9
shen_add_fun('shen.tab', shen_tab)

@tail_recursion
def shen_leftx45round():
    global symdic
    return 40
shen_add_fun('shen.left-round', shen_leftx45round)

@tail_recursion
def shen_find(KL_ARG_V2345_38, KL_ARG_V2346_39):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2346_39) else ([KL_ARG_V2346_39[0], tco_apply(shen_find, [KL_ARG_V2345_38, KL_ARG_V2346_39[1]])] if (shen_apply(KL_ARG_V2345_38, [KL_ARG_V2346_39[0]]) if shen_consp(KL_ARG_V2346_39) else False) else (tail_call(shen_find, [KL_ARG_V2345_38, KL_ARG_V2346_39[1]]) if shen_consp(KL_ARG_V2346_39) else (tail_call(shen_sysx45error, [symdic.symdic_shen_find]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.find', shen_find)

@tail_recursion
def shen_prefixx63(KL_ARG_V2357_40, KL_ARG_V2358_41):
    global symdic
    return (True if shen_eq([], KL_ARG_V2357_40) else (tail_call(shen_prefixx63, [KL_ARG_V2357_40[1], KL_ARG_V2358_41[1]]) if ((shen_eq(KL_ARG_V2358_41[0], KL_ARG_V2357_40[0]) if shen_consp(KL_ARG_V2358_41) else False) if shen_consp(KL_ARG_V2357_40) else False) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prefix?', shen_prefixx63)

@tail_recursion
def shen_printx45pastx45inputs(KL_ARG_V2368_42, KL_ARG_V2369_43, KL_ARG_V2370_44):
    global symdic
    return (symdic.symdic_kl__ if shen_eq([], KL_ARG_V2369_43) else (tail_call(shen_printx45pastx45inputs, [KL_ARG_V2368_42, KL_ARG_V2369_43[1], (KL_ARG_V2370_44 + 1)]) if ((not shen_apply(KL_ARG_V2368_42, [KL_ARG_V2369_43[0]])) if shen_consp(KL_ARG_V2369_43) else False) else ([tco_apply(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2370_44, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), [tco_apply(shen_prbytes, [tco_apply(kl_snd, [KL_ARG_V2369_43[0]])]), tail_call(shen_printx45pastx45inputs, [KL_ARG_V2368_42, KL_ARG_V2369_43[1], (KL_ARG_V2370_44 + 1)])][(-1)]][(-1)] if (tco_apply(kl_tuplex63, [KL_ARG_V2369_43[0]]) if shen_consp(KL_ARG_V2369_43) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_printx45pastx45inputs]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.print-past-inputs', shen_printx45pastx45inputs)

@tail_recursion
def shen_toplevel_evaluate(KL_ARG_V2371_45, KL_ARG_V2372_46):

    class KL_Context:
        KL_LOC_Eval_47 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V2371_45[0], KL_ARG_V2371_45[1][1][0]]) if (((((shen_eq(True, KL_ARG_V2372_46) if shen_eq([], KL_ARG_V2371_45[1][1][1]) else False) if shen_consp(KL_ARG_V2371_45[1][1]) else False) if shen_eq(symdic.symdic_kl_x58, KL_ARG_V2371_45[1][0]) else False) if shen_consp(KL_ARG_V2371_45[1]) else False) if shen_consp(KL_ARG_V2371_45) else False) else ([tco_apply(shen_toplevel_evaluate, [[KL_ARG_V2371_45[0], []], KL_ARG_V2372_46]), [tco_apply(kl_nl, [1]), tail_call(shen_toplevel_evaluate, [KL_ARG_V2371_45[1], KL_ARG_V2372_46])][(-1)]][(-1)] if (shen_consp(KL_ARG_V2371_45[1]) if shen_consp(KL_ARG_V2371_45) else False) else (tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V2371_45[0], tco_apply(kl_gensym, [symdic.symdic_A])]) if ((shen_eq(True, KL_ARG_V2372_46) if shen_eq([], KL_ARG_V2371_45[1]) else False) if shen_consp(KL_ARG_V2371_45) else False) else ([setattr(KL_CTX, 'KL_LOC_Eval_47', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V2371_45[0]])), tail_call(kl_print, [KL_CTX.KL_LOC_Eval_47])][(-1)] if ((shen_eq(False, KL_ARG_V2372_46) if shen_eq([], KL_ARG_V2371_45[1]) else False) if shen_consp(KL_ARG_V2371_45) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_toplevel_evaluate]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.toplevel_evaluate', shen_toplevel_evaluate)

@tail_recursion
def shen_typecheckx45andx45evaluate(KL_ARG_V2373_48, KL_ARG_V2374_49):

    class KL_Context:
        KL_LOC_Typecheck_50 = None
        KL_LOC_Eval_51 = None
        KL_LOC_Type_52 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Typecheck_50', tco_apply(shen_typecheck, [KL_ARG_V2373_48, KL_ARG_V2374_49])), (shen_simple_error('type error\r\n') if shen_eq(KL_CTX.KL_LOC_Typecheck_50, False) else [setattr(KL_CTX, 'KL_LOC_Eval_51', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V2373_48])), [setattr(KL_CTX, 'KL_LOC_Type_52', tco_apply(shen_prettyx45type, [KL_CTX.KL_LOC_Typecheck_50])), tail_call(shen_prhush, [tco_apply(shen_app, [KL_CTX.KL_LOC_Eval_51, (' : ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Type_52, '', symdic.symdic_shen_r])), symdic.symdic_shen_s]), tco_apply(kl_stoutput, [])])][(-1)]][(-1)])][(-1)]
shen_add_fun('shen.typecheck-and-evaluate', shen_typecheckx45andx45evaluate)

@tail_recursion
def shen_prettyx45type(KL_ARG_V2375_53):
    global symdic
    return tail_call(shen_mult_subst, [shen_get(symdic.symdic_shen_x42alphabetx42), tco_apply(shen_extractx45pvars, [KL_ARG_V2375_53]), KL_ARG_V2375_53])
shen_add_fun('shen.pretty-type', shen_prettyx45type)

@tail_recursion
def shen_extractx45pvars(KL_ARG_V2380_54):
    global symdic
    return ([KL_ARG_V2380_54, []] if tco_apply(shen_pvarx63, [KL_ARG_V2380_54]) else (tail_call(kl_union, [tco_apply(shen_extractx45pvars, [KL_ARG_V2380_54[0]]), tco_apply(shen_extractx45pvars, [KL_ARG_V2380_54[1]])]) if shen_consp(KL_ARG_V2380_54) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract-pvars', shen_extractx45pvars)

@tail_recursion
def shen_mult_subst(KL_ARG_V2385_55, KL_ARG_V2386_56, KL_ARG_V2387_57):
    global symdic
    return (KL_ARG_V2387_57 if shen_eq([], KL_ARG_V2385_55) else (KL_ARG_V2387_57 if shen_eq([], KL_ARG_V2386_56) else (tail_call(shen_mult_subst, [KL_ARG_V2385_55[1], KL_ARG_V2386_56[1], tco_apply(kl_subst, [KL_ARG_V2385_55[0], KL_ARG_V2386_56[0], KL_ARG_V2387_57])]) if (shen_consp(KL_ARG_V2386_56) if shen_consp(KL_ARG_V2385_55) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mult_subst]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.mult_subst', shen_mult_subst)


#============================== core.kl==============================



@tail_recursion
def shen_shenx45x62kl(KL_ARG_V607_58, KL_ARG_V608_59):
    global symdic
    return tail_call(kl_compile, [symdic.symdic_shen_x60definex62, [KL_ARG_V607_58, KL_ARG_V608_59], (lambda KL_ARG_X_60: tail_call(shen_shenx45syntaxx45error, [KL_ARG_V607_58, KL_ARG_X_60]))])
shen_add_fun('shen.shen->kl', shen_shenx45x62kl)

@tail_recursion
def shen_shenx45syntaxx45error(KL_ARG_V609_61, KL_ARG_V610_62):
    global symdic
    return shen_simple_error(('syntax error in ' + tco_apply(shen_app, [KL_ARG_V609_61, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V610_62]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])))
shen_add_fun('shen.shen-syntax-error', shen_shenx45syntaxx45error)

@tail_recursion
def shen_x60definex62(KL_ARG_V615_63):

    class KL_Context:
        KL_LOC_Result_64 = None
        KL_LOC_Parse_shen_x60namex62_65 = None
        KL_LOC_Parse_shen_x60signaturex62_66 = None
        KL_LOC_Parse_shen_x60rulesx62_67 = None
        KL_LOC_Result_68 = None
        KL_LOC_Parse_shen_x60namex62_69 = None
        KL_LOC_Parse_shen_x60rulesx62_70 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_64', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_65', tco_apply(shen_x60namex62, [KL_ARG_V615_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_66', tco_apply(shen_x60signaturex62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_67', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67[0], tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_65]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_67)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_66)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_65)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_68', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_69', tco_apply(shen_x60namex62, [KL_ARG_V615_63])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_70', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70[0], tco_apply(shen_compile_to_machine_code, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_69]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_70)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_69)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_68, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_68)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_64, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_64)][(-1)]
shen_add_fun('shen.<define>', shen_x60definex62)

@tail_recursion
def shen_x60namex62(KL_ARG_V620_71):

    class KL_Context:
        KL_LOC_Result_72 = None
        KL_LOC_Parse_X_73 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_72', ([setattr(KL_CTX, 'KL_LOC_Parse_X_73', KL_ARG_V620_71[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V620_71[0][1], tco_apply(shen_hdtl, [KL_ARG_V620_71])])[0], (KL_CTX.KL_LOC_Parse_X_73 if ((not tco_apply(shen_sysfuncx63, [KL_CTX.KL_LOC_Parse_X_73])) if tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Parse_X_73]) else False) else shen_simple_error(tco_apply(shen_app, [KL_CTX.KL_LOC_Parse_X_73, ' is not a legitimate function name.\r\n', symdic.symdic_shen_a])))])][(-1)] if shen_consp(KL_ARG_V620_71[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_72, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_72)][(-1)]
shen_add_fun('shen.<name>', shen_x60namex62)

@tail_recursion
def shen_sysfuncx63(KL_ARG_V621_74):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V621_74, tco_apply(kl_get, [shen_intern('shen'), symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])])
shen_add_fun('shen.sysfunc?', shen_sysfuncx63)

@tail_recursion
def shen_x60signaturex62(KL_ARG_V626_75):

    class KL_Context:
        KL_LOC_Result_76 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_77 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_76', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_77', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [KL_ARG_V626_75[0][1], tco_apply(shen_hdtl, [KL_ARG_V626_75])])])), ((tco_apply(shen_pair, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])[0], tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77])])])]) if (shen_eq(symdic.symdic_kl_x125, KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_77)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x123, KL_ARG_V626_75[0][0]) if shen_consp(KL_ARG_V626_75[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_76, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_76)][(-1)]
shen_add_fun('shen.<signature>', shen_x60signaturex62)

@tail_recursion
def shen_curryx45type(KL_ARG_V629_78):
    global symdic
    return (tail_call(shen_curryx45type, [[KL_ARG_V629_78[0], [symdic.symdic_kl_x45x45x62, [KL_ARG_V629_78[1][1], []]]]]) if (((((shen_eq(symdic.symdic_kl_x45x45x62, KL_ARG_V629_78[1][1][1][0]) if shen_consp(KL_ARG_V629_78[1][1][1]) else False) if shen_consp(KL_ARG_V629_78[1][1]) else False) if shen_eq(symdic.symdic_kl_x45x45x62, KL_ARG_V629_78[1][0]) else False) if shen_consp(KL_ARG_V629_78[1]) else False) if shen_consp(KL_ARG_V629_78) else False) else ([symdic.symdic_kl_list, [tco_apply(shen_curryx45type, [KL_ARG_V629_78[1][0]]), []]] if ((((shen_eq([], KL_ARG_V629_78[1][1][1]) if shen_consp(KL_ARG_V629_78[1][1]) else False) if shen_consp(KL_ARG_V629_78[1]) else False) if shen_eq(symdic.symdic_kl_cons, KL_ARG_V629_78[0]) else False) if shen_consp(KL_ARG_V629_78) else False) else (tail_call(shen_curryx45type, [[KL_ARG_V629_78[0], [symdic.symdic_kl_x42, [KL_ARG_V629_78[1][1], []]]]]) if (((((shen_eq(symdic.symdic_kl_x42, KL_ARG_V629_78[1][1][1][0]) if shen_consp(KL_ARG_V629_78[1][1][1]) else False) if shen_consp(KL_ARG_V629_78[1][1]) else False) if shen_eq(symdic.symdic_kl_x42, KL_ARG_V629_78[1][0]) else False) if shen_consp(KL_ARG_V629_78[1]) else False) if shen_consp(KL_ARG_V629_78) else False) else (tail_call(kl_map, [symdic.symdic_shen_curryx45type, KL_ARG_V629_78]) if shen_consp(KL_ARG_V629_78) else (KL_ARG_V629_78 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry-type', shen_curryx45type)

@tail_recursion
def shen_x60signaturex45helpx62(KL_ARG_V634_79):

    class KL_Context:
        KL_LOC_Result_80 = None
        KL_LOC_Parse_X_81 = None
        KL_LOC_Parse_shen_x60signaturex45helpx62_82 = None
        KL_LOC_Result_83 = None
        KL_LOC_Parse_x60ex62_84 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_80', ([setattr(KL_CTX, 'KL_LOC_Parse_X_81', KL_ARG_V634_79[0][0]), [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex45helpx62_82', tco_apply(shen_x60signaturex45helpx62, [tco_apply(shen_pair, [KL_ARG_V634_79[0][1], tco_apply(shen_hdtl, [KL_ARG_V634_79])])])), ((tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82[0], [KL_CTX.KL_LOC_Parse_X_81, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82])]]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_81, [symdic.symdic_kl_x123, [symdic.symdic_kl_x125, []]]])) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex45helpx62_82)) else tco_apply(kl_fail, []))][(-1)]][(-1)] if shen_consp(KL_ARG_V634_79[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_83', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_84', tco_apply(kl_x60ex62, [KL_ARG_V634_79])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_84[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_84)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_83, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_83)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_80, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_80)][(-1)]
shen_add_fun('shen.<signature-help>', shen_x60signaturex45helpx62)

@tail_recursion
def shen_x60rulesx62(KL_ARG_V639_85):

    class KL_Context:
        KL_LOC_Result_86 = None
        KL_LOC_Parse_shen_x60rulex62_87 = None
        KL_LOC_Parse_shen_x60rulesx62_88 = None
        KL_LOC_Result_89 = None
        KL_LOC_Parse_shen_x60rulex62_90 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_86', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_87', tco_apply(shen_x60rulex62, [KL_ARG_V639_85])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_88', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88[0], [tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_87])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_88)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulex62_87)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_89', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulex62_90', tco_apply(shen_x60rulex62, [KL_ARG_V639_85])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_90[0], [tco_apply(shen_linearise, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulex62_90])]), []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulex62_90)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_89, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_89)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_86, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_86)][(-1)]
shen_add_fun('shen.<rules>', shen_x60rulesx62)

@tail_recursion
def shen_x60rulex62(KL_ARG_V644_91):

    class KL_Context:
        KL_LOC_Result_92 = None
        KL_LOC_Parse_shen_x60patternsx62_93 = None
        KL_LOC_Parse_shen_x60actionx62_94 = None
        KL_LOC_Parse_shen_x60guardx62_95 = None
        KL_LOC_Result_96 = None
        KL_LOC_Parse_shen_x60patternsx62_97 = None
        KL_LOC_Parse_shen_x60actionx62_98 = None
        KL_LOC_Result_99 = None
        KL_LOC_Parse_shen_x60patternsx62_100 = None
        KL_LOC_Parse_shen_x60actionx62_101 = None
        KL_LOC_Parse_shen_x60guardx62_102 = None
        KL_LOC_Result_103 = None
        KL_LOC_Parse_shen_x60patternsx62_104 = None
        KL_LOC_Parse_shen_x60actionx62_105 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_92', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_93', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_94', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_95', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_95[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93]), [[symdic.symdic_kl_where, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_95]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_94]), []]]], []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_95)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60actionx62_94[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_94)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_93)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_96', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_97', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_98', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_98[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_98]), []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_98)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_97)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_99', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_100', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_101', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_102', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_102[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100]), [[symdic.symdic_kl_where, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_102]), [[symdic.symdic_shen_choicepointx33, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_101]), []]], []]]], []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_102)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60actionx62_101[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_101)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_100)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_103', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_104', tco_apply(shen_x60patternsx62, [KL_ARG_V644_91])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_105', tco_apply(shen_x60actionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_105[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104]), [[symdic.symdic_shen_choicepointx33, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_105]), []]], []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_105)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_104)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_103, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_103)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_99, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_99)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_96, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_96)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_92, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_92)][(-1)]
shen_add_fun('shen.<rule>', shen_x60rulex62)

@tail_recursion
def shen_fail_if(KL_ARG_V645_106, KL_ARG_V646_107):
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V645_106, [KL_ARG_V646_107]) else KL_ARG_V646_107)
shen_add_fun('shen.fail_if', shen_fail_if)

@tail_recursion
def shen_succeedsx63(KL_ARG_V651_108):
    global symdic
    return (False if shen_eq(KL_ARG_V651_108, tco_apply(kl_fail, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.succeeds?', shen_succeedsx63)

@tail_recursion
def shen_x60patternsx62(KL_ARG_V656_109):

    class KL_Context:
        KL_LOC_Result_110 = None
        KL_LOC_Parse_shen_x60patternx62_111 = None
        KL_LOC_Parse_shen_x60patternsx62_112 = None
        KL_LOC_Result_113 = None
        KL_LOC_Parse_x60ex62_114 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_110', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_111', tco_apply(shen_x60patternx62, [KL_ARG_V656_109])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_112', tco_apply(shen_x60patternsx62, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_111]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_112)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_111)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_113', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_114', tco_apply(kl_x60ex62, [KL_ARG_V656_109])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_114[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_114)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_113, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_113)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_110, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_110)][(-1)]
shen_add_fun('shen.<patterns>', shen_x60patternsx62)

@tail_recursion
def shen_x60patternx62(KL_ARG_V661_115):

    class KL_Context:
        KL_LOC_Result_116 = None
        KL_LOC_Parse_shen_x60pattern1x62_117 = None
        KL_LOC_Parse_shen_x60pattern2x62_118 = None
        KL_LOC_Result_119 = None
        KL_LOC_Parse_shen_x60pattern1x62_120 = None
        KL_LOC_Parse_shen_x60pattern2x62_121 = None
        KL_LOC_Result_122 = None
        KL_LOC_Parse_shen_x60pattern1x62_123 = None
        KL_LOC_Parse_shen_x60pattern2x62_124 = None
        KL_LOC_Result_125 = None
        KL_LOC_Parse_shen_x60pattern1x62_126 = None
        KL_LOC_Parse_shen_x60pattern2x62_127 = None
        KL_LOC_Result_128 = None
        KL_LOC_Result_129 = None
        KL_LOC_Parse_X_130 = None
        KL_LOC_Result_131 = None
        KL_LOC_Parse_shen_x60simple_patternx62_132 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_116', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_117', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_118', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_x64p, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_118)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_117)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x64p, tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_119', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_120', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_121', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_cons, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_121)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_120)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_cons, tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_122', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_123', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_124', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_x64v, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_124)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_123)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x64v, tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_125', (tco_apply(shen_sndx45orx45fail, [([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern1x62_126', tco_apply(shen_x60pattern1x62, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60pattern2x62_127', tco_apply(shen_x60pattern2x62, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern2x62_127)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60pattern1x62_126)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x64s, tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_128', (tco_apply(shen_sndx45orx45fail, [((tco_apply(shen_pair, [tco_apply(shen_pair, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])])])[0], tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], [symdic.symdic_kl_vector, [0, []]]])]) if (shen_eq(0, tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])[0][0]) if shen_consp(tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][1], tco_apply(shen_hdtl, [tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])])])[0]) else False) else tco_apply(kl_fail, [])) if (shen_eq(symdic.symdic_kl_vector, tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0][0]) if shen_consp(tco_apply(shen_pair, [KL_ARG_V661_115[0][0], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0]) else False) else tco_apply(kl_fail, []))]) if (shen_consp(KL_ARG_V661_115[0][0]) if shen_consp(KL_ARG_V661_115[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_129', ([setattr(KL_CTX, 'KL_LOC_Parse_X_130', KL_ARG_V661_115[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V661_115[0][1], tco_apply(shen_hdtl, [KL_ARG_V661_115])])[0], tco_apply(shen_constructorx45error, [KL_CTX.KL_LOC_Parse_X_130])]) if shen_consp(KL_CTX.KL_LOC_Parse_X_130) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V661_115[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_131', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60simple_patternx62_132', tco_apply(shen_x60simple_patternx62, [KL_ARG_V661_115])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60simple_patternx62_132)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_131, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_131)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_129, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_129)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_128, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_128)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_125, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_125)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_122, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_122)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_119, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_119)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_116, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_116)][(-1)]
shen_add_fun('shen.<pattern>', shen_x60patternx62)

@tail_recursion
def shen_constructorx45error(KL_ARG_V662_133):
    global symdic
    return shen_simple_error(tco_apply(shen_app, [KL_ARG_V662_133, ' is not a legitimate constructor\r\n', symdic.symdic_shen_a]))
shen_add_fun('shen.constructor-error', shen_constructorx45error)

@tail_recursion
def shen_x60simple_patternx62(KL_ARG_V667_134):

    class KL_Context:
        KL_LOC_Result_135 = None
        KL_LOC_Parse_X_136 = None
        KL_LOC_Result_137 = None
        KL_LOC_Parse_X_138 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_135', ([setattr(KL_CTX, 'KL_LOC_Parse_X_136', KL_ARG_V667_134[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V667_134[0][1], tco_apply(shen_hdtl, [KL_ARG_V667_134])])[0], tco_apply(kl_gensym, [symdic.symdic_Parse_Y])]) if shen_eq(KL_CTX.KL_LOC_Parse_X_136, symdic.symdic_kl__) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V667_134[0]) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_137', ([setattr(KL_CTX, 'KL_LOC_Parse_X_138', KL_ARG_V667_134[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V667_134[0][1], tco_apply(shen_hdtl, [KL_ARG_V667_134])])[0], KL_CTX.KL_LOC_Parse_X_138]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_138, [symdic.symdic_kl_x45x62, [symdic.symdic_kl_x60x45, []]]])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V667_134[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_137, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_137)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_135, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_135)][(-1)]
shen_add_fun('shen.<simple_pattern>', shen_x60simple_patternx62)

@tail_recursion
def shen_x60pattern1x62(KL_ARG_V672_139):

    class KL_Context:
        KL_LOC_Result_140 = None
        KL_LOC_Parse_shen_x60patternx62_141 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_140', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_141', tco_apply(shen_x60patternx62, [KL_ARG_V672_139])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_141[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_141])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_141)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_140, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_140)][(-1)]
shen_add_fun('shen.<pattern1>', shen_x60pattern1x62)

@tail_recursion
def shen_x60pattern2x62(KL_ARG_V677_142):

    class KL_Context:
        KL_LOC_Result_143 = None
        KL_LOC_Parse_shen_x60patternx62_144 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_143', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternx62_144', tco_apply(shen_x60patternx62, [KL_ARG_V677_142])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_144[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternx62_144])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternx62_144)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_143, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_143)][(-1)]
shen_add_fun('shen.<pattern2>', shen_x60pattern2x62)

@tail_recursion
def shen_x60actionx62(KL_ARG_V682_145):

    class KL_Context:
        KL_LOC_Result_146 = None
        KL_LOC_Parse_X_147 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_146', ([setattr(KL_CTX, 'KL_LOC_Parse_X_147', KL_ARG_V682_145[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V682_145[0][1], tco_apply(shen_hdtl, [KL_ARG_V682_145])])[0], KL_CTX.KL_LOC_Parse_X_147])][(-1)] if shen_consp(KL_ARG_V682_145[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_146, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_146)][(-1)]
shen_add_fun('shen.<action>', shen_x60actionx62)

@tail_recursion
def shen_x60guardx62(KL_ARG_V687_148):

    class KL_Context:
        KL_LOC_Result_149 = None
        KL_LOC_Parse_X_150 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_149', ([setattr(KL_CTX, 'KL_LOC_Parse_X_150', KL_ARG_V687_148[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V687_148[0][1], tco_apply(shen_hdtl, [KL_ARG_V687_148])])[0], KL_CTX.KL_LOC_Parse_X_150])][(-1)] if shen_consp(KL_ARG_V687_148[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_149, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_149)][(-1)]
shen_add_fun('shen.<guard>', shen_x60guardx62)

@tail_recursion
def shen_compile_to_machine_code(KL_ARG_V688_151, KL_ARG_V689_152):

    class KL_Context:
        KL_LOC_Lambdax43_153 = None
        KL_LOC_KL_154 = None
        KL_LOC_Record_155 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Lambdax43_153', tco_apply(shen_compile_to_lambdax43, [KL_ARG_V688_151, KL_ARG_V689_152])), [setattr(KL_CTX, 'KL_LOC_KL_154', tco_apply(shen_compile_to_kl, [KL_ARG_V688_151, KL_CTX.KL_LOC_Lambdax43_153])), [setattr(KL_CTX, 'KL_LOC_Record_155', tco_apply(shen_recordx45source, [KL_ARG_V688_151, KL_CTX.KL_LOC_KL_154])), KL_CTX.KL_LOC_KL_154][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_machine_code', shen_compile_to_machine_code)

@tail_recursion
def shen_recordx45source(KL_ARG_V692_156, KL_ARG_V693_157):
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V692_156, symdic.symdic_shen_source, KL_ARG_V693_157, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.record-source', shen_recordx45source)

@tail_recursion
def shen_compile_to_lambdax43(KL_ARG_V694_158, KL_ARG_V695_159):

    class KL_Context:
        KL_LOC_Arity_160 = None
        KL_LOC_Free_161 = None
        KL_LOC_Variables_163 = None
        KL_LOC_Strip_164 = None
        KL_LOC_Abstractions_165 = None
        KL_LOC_Applications_166 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_160', tco_apply(shen_aritycheck, [KL_ARG_V694_158, KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Free_161', tco_apply(kl_map, [(lambda KL_ARG_Rule_162: tail_call(shen_free_variable_check, [KL_ARG_V694_158, KL_ARG_Rule_162])), KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Variables_163', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_160])), [setattr(KL_CTX, 'KL_LOC_Strip_164', tco_apply(kl_map, [symdic.symdic_shen_stripx45protect, KL_ARG_V695_159])), [setattr(KL_CTX, 'KL_LOC_Abstractions_165', tco_apply(kl_map, [symdic.symdic_shen_abstract_rule, KL_CTX.KL_LOC_Strip_164])), [setattr(KL_CTX, 'KL_LOC_Applications_166', tco_apply(kl_map, [(lambda KL_ARG_X_167: tail_call(shen_application_build, [KL_CTX.KL_LOC_Variables_163, KL_ARG_X_167])), KL_CTX.KL_LOC_Abstractions_165])), [KL_CTX.KL_LOC_Variables_163, [KL_CTX.KL_LOC_Applications_166, []]]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.compile_to_lambda+', shen_compile_to_lambdax43)

@tail_recursion
def shen_free_variable_check(KL_ARG_V696_168, KL_ARG_V697_169):

    class KL_Context:
        KL_LOC_Bound_170 = None
        KL_LOC_Free_171 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Bound_170', tco_apply(shen_extract_vars, [KL_ARG_V697_169[0]])), [setattr(KL_CTX, 'KL_LOC_Free_171', tco_apply(shen_extract_free_vars, [KL_CTX.KL_LOC_Bound_170, KL_ARG_V697_169[1][0]])), tail_call(shen_free_variable_warnings, [KL_ARG_V696_168, KL_CTX.KL_LOC_Free_171])][(-1)]][(-1)] if ((shen_eq([], KL_ARG_V697_169[1][1]) if shen_consp(KL_ARG_V697_169[1]) else False) if shen_consp(KL_ARG_V697_169) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_free_variable_check]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_check', shen_free_variable_check)

@tail_recursion
def shen_extract_vars(KL_ARG_V698_172):
    global symdic
    return ([KL_ARG_V698_172, []] if tco_apply(kl_variablex63, [KL_ARG_V698_172]) else (tail_call(kl_union, [tco_apply(shen_extract_vars, [KL_ARG_V698_172[0]]), tco_apply(shen_extract_vars, [KL_ARG_V698_172[1]])]) if shen_consp(KL_ARG_V698_172) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.extract_vars', shen_extract_vars)

@tail_recursion
def shen_extract_free_vars(KL_ARG_V708_173, KL_ARG_V709_174):
    global symdic
    return ([] if (((shen_eq(KL_ARG_V709_174[0], symdic.symdic_kl_protect) if shen_eq([], KL_ARG_V709_174[1][1]) else False) if shen_consp(KL_ARG_V709_174[1]) else False) if shen_consp(KL_ARG_V709_174) else False) else ([KL_ARG_V709_174, []] if ((not tco_apply(kl_elementx63, [KL_ARG_V709_174, KL_ARG_V708_173])) if tco_apply(kl_variablex63, [KL_ARG_V709_174]) else False) else (tail_call(shen_extract_free_vars, [[KL_ARG_V709_174[1][0], KL_ARG_V708_173], KL_ARG_V709_174[1][1][0]]) if ((((shen_eq([], KL_ARG_V709_174[1][1][1]) if shen_consp(KL_ARG_V709_174[1][1]) else False) if shen_consp(KL_ARG_V709_174[1]) else False) if shen_eq(symdic.symdic_kl_lambda, KL_ARG_V709_174[0]) else False) if shen_consp(KL_ARG_V709_174) else False) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, KL_ARG_V709_174[1][1][0]]), tco_apply(shen_extract_free_vars, [[KL_ARG_V709_174[1][0], KL_ARG_V708_173], KL_ARG_V709_174[1][1][1][0]])]) if (((((shen_eq([], KL_ARG_V709_174[1][1][1][1]) if shen_consp(KL_ARG_V709_174[1][1][1]) else False) if shen_consp(KL_ARG_V709_174[1][1]) else False) if shen_consp(KL_ARG_V709_174[1]) else False) if shen_eq(symdic.symdic_kl_let, KL_ARG_V709_174[0]) else False) if shen_consp(KL_ARG_V709_174) else False) else (tail_call(kl_union, [tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, KL_ARG_V709_174[0]]), tco_apply(shen_extract_free_vars, [KL_ARG_V708_173, KL_ARG_V709_174[1]])]) if shen_consp(KL_ARG_V709_174) else ([] if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.extract_free_vars', shen_extract_free_vars)

@tail_recursion
def shen_free_variable_warnings(KL_ARG_V712_175, KL_ARG_V713_176):
    global symdic
    return (symdic.symdic_kl__ if shen_eq([], KL_ARG_V713_176) else (shen_simple_error(('error: the following variables are free in ' + tco_apply(shen_app, [KL_ARG_V712_175, (': ' + tco_apply(shen_app, [tco_apply(shen_list_variables, [KL_ARG_V713_176]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.free_variable_warnings', shen_free_variable_warnings)

@tail_recursion
def shen_list_variables(KL_ARG_V714_177):
    global symdic
    return ((str(KL_ARG_V714_177[0]) + '.') if (shen_eq([], KL_ARG_V714_177[1]) if shen_consp(KL_ARG_V714_177) else False) else ((str(KL_ARG_V714_177[0]) + (', ' + tco_apply(shen_list_variables, [KL_ARG_V714_177[1]]))) if shen_consp(KL_ARG_V714_177) else (tail_call(shen_sysx45error, [symdic.symdic_shen_list_variables]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.list_variables', shen_list_variables)

@tail_recursion
def shen_stripx45protect(KL_ARG_V715_178):
    global symdic
    return (KL_ARG_V715_178[1][0] if (((shen_eq(KL_ARG_V715_178[0], symdic.symdic_kl_protect) if shen_eq([], KL_ARG_V715_178[1][1]) else False) if shen_consp(KL_ARG_V715_178[1]) else False) if shen_consp(KL_ARG_V715_178) else False) else ([tco_apply(shen_stripx45protect, [KL_ARG_V715_178[0]]), tco_apply(shen_stripx45protect, [KL_ARG_V715_178[1]])] if shen_consp(KL_ARG_V715_178) else (KL_ARG_V715_178 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.strip-protect', shen_stripx45protect)

@tail_recursion
def shen_linearise(KL_ARG_V716_179):
    global symdic
    return (tail_call(shen_linearise_help, [tco_apply(shen_flatten, [KL_ARG_V716_179[0]]), KL_ARG_V716_179[0], KL_ARG_V716_179[1][0]]) if ((shen_eq([], KL_ARG_V716_179[1][1]) if shen_consp(KL_ARG_V716_179[1]) else False) if shen_consp(KL_ARG_V716_179) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise', shen_linearise)

@tail_recursion
def shen_flatten(KL_ARG_V717_180):
    global symdic
    return ([] if shen_eq([], KL_ARG_V717_180) else (tail_call(kl_append, [tco_apply(shen_flatten, [KL_ARG_V717_180[0]]), tco_apply(shen_flatten, [KL_ARG_V717_180[1]])]) if shen_consp(KL_ARG_V717_180) else ([KL_ARG_V717_180, []] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.flatten', shen_flatten)

@tail_recursion
def shen_linearise_help(KL_ARG_V718_181, KL_ARG_V719_182, KL_ARG_V720_183):

    class KL_Context:
        KL_LOC_Var_184 = None
        KL_LOC_NewAction_185 = None
        KL_LOC_NewPatts_186 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V719_182, [KL_ARG_V720_183, []]] if shen_eq([], KL_ARG_V718_181) else (([setattr(KL_CTX, 'KL_LOC_Var_184', tco_apply(kl_gensym, [KL_ARG_V718_181[0]])), [setattr(KL_CTX, 'KL_LOC_NewAction_185', [symdic.symdic_kl_where, [[symdic.symdic_kl_x61, [KL_ARG_V718_181[0], [KL_CTX.KL_LOC_Var_184, []]]], [KL_ARG_V720_183, []]]]), [setattr(KL_CTX, 'KL_LOC_NewPatts_186', tco_apply(shen_linearise_X, [KL_ARG_V718_181[0], KL_CTX.KL_LOC_Var_184, KL_ARG_V719_182])), tail_call(shen_linearise_help, [KL_ARG_V718_181[1], KL_CTX.KL_LOC_NewPatts_186, KL_CTX.KL_LOC_NewAction_185])][(-1)]][(-1)]][(-1)] if (tco_apply(kl_elementx63, [KL_ARG_V718_181[0], KL_ARG_V718_181[1]]) if tco_apply(kl_variablex63, [KL_ARG_V718_181[0]]) else False) else tail_call(shen_linearise_help, [KL_ARG_V718_181[1], KL_ARG_V719_182, KL_ARG_V720_183])) if shen_consp(KL_ARG_V718_181) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearise_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_help', shen_linearise_help)

@tail_recursion
def shen_linearise_X(KL_ARG_V729_187, KL_ARG_V730_188, KL_ARG_V731_189):

    class KL_Context:
        KL_LOC_L_190 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V730_188 if shen_eq(KL_ARG_V731_189, KL_ARG_V729_187) else ([setattr(KL_CTX, 'KL_LOC_L_190', tco_apply(shen_linearise_X, [KL_ARG_V729_187, KL_ARG_V730_188, KL_ARG_V731_189[0]])), ([KL_ARG_V731_189[0], tco_apply(shen_linearise_X, [KL_ARG_V729_187, KL_ARG_V730_188, KL_ARG_V731_189[1]])] if shen_eq(KL_CTX.KL_LOC_L_190, KL_ARG_V731_189[0]) else [KL_CTX.KL_LOC_L_190, KL_ARG_V731_189[1]])][(-1)] if shen_consp(KL_ARG_V731_189) else (KL_ARG_V731_189 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.linearise_X', shen_linearise_X)

@tail_recursion
def shen_aritycheck(KL_ARG_V733_191, KL_ARG_V734_192):
    global symdic
    return ([tco_apply(shen_aritycheckx45action, [KL_ARG_V734_192[0][1][0]]), tail_call(shen_aritycheckx45name, [KL_ARG_V733_191, tco_apply(kl_arity, [KL_ARG_V733_191]), tco_apply(kl_length, [KL_ARG_V734_192[0][0]])])][(-1)] if ((((shen_eq([], KL_ARG_V734_192[1]) if shen_eq([], KL_ARG_V734_192[0][1][1]) else False) if shen_consp(KL_ARG_V734_192[0][1]) else False) if shen_consp(KL_ARG_V734_192[0]) else False) if shen_consp(KL_ARG_V734_192) else False) else (([tco_apply(shen_aritycheckx45action, [KL_ARG_V734_192[0][1][0]]), tail_call(shen_aritycheck, [KL_ARG_V733_191, KL_ARG_V734_192[1]])][(-1)] if shen_eq(tco_apply(kl_length, [KL_ARG_V734_192[0][0]]), tco_apply(kl_length, [KL_ARG_V734_192[1][0][0]])) else shen_simple_error(('arity error in ' + tco_apply(shen_app, [KL_ARG_V733_191, '\r\n', symdic.symdic_shen_a])))) if (((((((shen_eq([], KL_ARG_V734_192[1][0][1][1]) if shen_consp(KL_ARG_V734_192[1][0][1]) else False) if shen_consp(KL_ARG_V734_192[1][0]) else False) if shen_consp(KL_ARG_V734_192[1]) else False) if shen_eq([], KL_ARG_V734_192[0][1][1]) else False) if shen_consp(KL_ARG_V734_192[0][1]) else False) if shen_consp(KL_ARG_V734_192[0]) else False) if shen_consp(KL_ARG_V734_192) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck', shen_aritycheck)

@tail_recursion
def shen_aritycheckx45name(KL_ARG_V743_193, KL_ARG_V744_194, KL_ARG_V745_195):
    global symdic
    return (KL_ARG_V745_195 if shen_eq((-1), KL_ARG_V744_194) else (KL_ARG_V745_195 if shen_eq(KL_ARG_V745_195, KL_ARG_V744_194) else ([tco_apply(shen_prhush, [('\r\nwarning: changing the arity of ' + tco_apply(shen_app, [KL_ARG_V743_193, ' can cause errors.\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), KL_ARG_V745_195][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.aritycheck-name', shen_aritycheckx45name)

@tail_recursion
def shen_aritycheckx45action(KL_ARG_V751_196):
    global symdic
    return ([tco_apply(shen_aah, [KL_ARG_V751_196[0], KL_ARG_V751_196[1]]), tail_call(kl_map, [symdic.symdic_shen_aritycheckx45action, KL_ARG_V751_196])][(-1)] if shen_consp(KL_ARG_V751_196) else (symdic.symdic_shen_skip if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aritycheck-action', shen_aritycheckx45action)

@tail_recursion
def shen_aah(KL_ARG_V752_197, KL_ARG_V753_198):

    class KL_Context:
        KL_LOC_Arity_199 = None
        KL_LOC_Len_200 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Arity_199', tco_apply(kl_arity, [KL_ARG_V752_197])), [setattr(KL_CTX, 'KL_LOC_Len_200', tco_apply(kl_length, [KL_ARG_V753_198])), (tail_call(shen_prhush, [('warning: ' + tco_apply(shen_app, [KL_ARG_V752_197, (' might not like ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Len_200, (' argument' + tco_apply(shen_app, [('s' if (KL_CTX.KL_LOC_Len_200 > 1) else ''), '.\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if ((KL_CTX.KL_LOC_Len_200 > KL_CTX.KL_LOC_Arity_199) if (KL_CTX.KL_LOC_Arity_199 > (-1)) else False) else symdic.symdic_shen_skip)][(-1)]][(-1)]
shen_add_fun('shen.aah', shen_aah)

@tail_recursion
def shen_abstract_rule(KL_ARG_V754_201):
    global symdic
    return (tail_call(shen_abstraction_build, [KL_ARG_V754_201[0], KL_ARG_V754_201[1][0]]) if ((shen_eq([], KL_ARG_V754_201[1][1]) if shen_consp(KL_ARG_V754_201[1]) else False) if shen_consp(KL_ARG_V754_201) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstract_rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.abstract_rule', shen_abstract_rule)

@tail_recursion
def shen_abstraction_build(KL_ARG_V755_202, KL_ARG_V756_203):
    global symdic
    return (KL_ARG_V756_203 if shen_eq([], KL_ARG_V755_202) else ([symdic.symdic_kl_x47_, [KL_ARG_V755_202[0], [tco_apply(shen_abstraction_build, [KL_ARG_V755_202[1], KL_ARG_V756_203]), []]]] if shen_consp(KL_ARG_V755_202) else (tail_call(shen_sysx45error, [symdic.symdic_shen_abstraction_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abstraction_build', shen_abstraction_build)

@tail_recursion
def shen_parameters(KL_ARG_V757_204):
    global symdic
    return ([] if shen_eq(0, KL_ARG_V757_204) else ([tco_apply(kl_gensym, [symdic.symdic_V]), tco_apply(shen_parameters, [(KL_ARG_V757_204 - 1)])] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.parameters', shen_parameters)

@tail_recursion
def shen_application_build(KL_ARG_V758_205, KL_ARG_V759_206):
    global symdic
    return (KL_ARG_V759_206 if shen_eq([], KL_ARG_V758_205) else (tail_call(shen_application_build, [KL_ARG_V758_205[1], [KL_ARG_V759_206, [KL_ARG_V758_205[0], []]]]) if shen_consp(KL_ARG_V758_205) else (tail_call(shen_sysx45error, [symdic.symdic_shen_application_build]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.application_build', shen_application_build)

@tail_recursion
def shen_compile_to_kl(KL_ARG_V760_207, KL_ARG_V761_208):

    class KL_Context:
        KL_LOC_Arity_209 = None
        KL_LOC_Reduce_210 = None
        KL_LOC_CondExpression_211 = None
        KL_LOC_TypeTable_212 = None
        KL_LOC_TypedCondExpression_213 = None
        KL_LOC_KL_214 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Arity_209', tco_apply(shen_storex45arity, [KL_ARG_V760_207, tco_apply(kl_length, [KL_ARG_V761_208[0]])])), [setattr(KL_CTX, 'KL_LOC_Reduce_210', tco_apply(kl_map, [symdic.symdic_shen_reduce, KL_ARG_V761_208[1][0]])), [setattr(KL_CTX, 'KL_LOC_CondExpression_211', tco_apply(shen_condx45expression, [KL_ARG_V760_207, KL_ARG_V761_208[0], KL_CTX.KL_LOC_Reduce_210])), [setattr(KL_CTX, 'KL_LOC_TypeTable_212', (tco_apply(shen_typextable, [tco_apply(shen_getx45type, [KL_ARG_V760_207]), KL_ARG_V761_208[0]]) if shen_get(symdic.symdic_shen_x42optimisex42) else symdic.symdic_shen_skip)), [setattr(KL_CTX, 'KL_LOC_TypedCondExpression_213', (tco_apply(shen_assignx45types, [KL_ARG_V761_208[0], KL_CTX.KL_LOC_TypeTable_212, KL_CTX.KL_LOC_CondExpression_211]) if shen_get(symdic.symdic_shen_x42optimisex42) else KL_CTX.KL_LOC_CondExpression_211)), [setattr(KL_CTX, 'KL_LOC_KL_214', [symdic.symdic_kl_defun, [KL_ARG_V760_207, [KL_ARG_V761_208[0], [KL_CTX.KL_LOC_TypedCondExpression_213, []]]]]), KL_CTX.KL_LOC_KL_214][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if ((shen_eq([], KL_ARG_V761_208[1][1]) if shen_consp(KL_ARG_V761_208[1]) else False) if shen_consp(KL_ARG_V761_208) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compile_to_kl]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile_to_kl', shen_compile_to_kl)

@tail_recursion
def shen_getx45type(KL_ARG_V766_215):

    class KL_Context:
        KL_LOC_FType_216 = None
    KL_CTX = KL_Context()
    global symdic
    return (symdic.symdic_shen_skip if shen_consp(KL_ARG_V766_215) else ([setattr(KL_CTX, 'KL_LOC_FType_216', tco_apply(kl_assoc, [KL_ARG_V766_215, shen_get(symdic.symdic_shen_x42signedfuncsx42)])), (symdic.symdic_shen_skip if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_FType_216]) else KL_CTX.KL_LOC_FType_216[1])][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.get-type', shen_getx45type)

@tail_recursion
def shen_typextable(KL_ARG_V775_217, KL_ARG_V776_218):
    global symdic
    return ((tail_call(shen_typextable, [KL_ARG_V775_217[1][1][0], KL_ARG_V776_218[1]]) if tco_apply(kl_variablex63, [KL_ARG_V775_217[0]]) else [[KL_ARG_V776_218[0], KL_ARG_V775_217[0]], tco_apply(shen_typextable, [KL_ARG_V775_217[1][1][0], KL_ARG_V776_218[1]])]) if (((((shen_consp(KL_ARG_V776_218) if shen_eq([], KL_ARG_V775_217[1][1][1]) else False) if shen_consp(KL_ARG_V775_217[1][1]) else False) if shen_eq(symdic.symdic_kl_x45x45x62, KL_ARG_V775_217[1][0]) else False) if shen_consp(KL_ARG_V775_217[1]) else False) if shen_consp(KL_ARG_V775_217) else False) else ([] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.typextable', shen_typextable)

@tail_recursion
def shen_assignx45types(KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_V779_221):

    class KL_Context:
        KL_LOC_NewTable_223 = None
        KL_LOC_AtomType_225 = None
    KL_CTX = KL_Context()
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V779_221[1][0], [tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_V779_221[1][1][0]]), [tco_apply(shen_assignx45types, [[KL_ARG_V779_221[1][0], KL_ARG_V777_219], KL_ARG_V778_220, KL_ARG_V779_221[1][1][1][0]]), []]]]] if (((((shen_eq([], KL_ARG_V779_221[1][1][1][1]) if shen_consp(KL_ARG_V779_221[1][1][1]) else False) if shen_consp(KL_ARG_V779_221[1][1]) else False) if shen_consp(KL_ARG_V779_221[1]) else False) if shen_eq(symdic.symdic_kl_let, KL_ARG_V779_221[0]) else False) if shen_consp(KL_ARG_V779_221) else False) else ([symdic.symdic_kl_lambda, [KL_ARG_V779_221[1][0], [tco_apply(shen_assignx45types, [[KL_ARG_V779_221[1][0], KL_ARG_V777_219], KL_ARG_V778_220, KL_ARG_V779_221[1][1][0]]), []]]] if ((((shen_eq([], KL_ARG_V779_221[1][1][1]) if shen_consp(KL_ARG_V779_221[1][1]) else False) if shen_consp(KL_ARG_V779_221[1]) else False) if shen_eq(symdic.symdic_kl_lambda, KL_ARG_V779_221[0]) else False) if shen_consp(KL_ARG_V779_221) else False) else ([symdic.symdic_kl_cond, tco_apply(kl_map, [(lambda KL_ARG_Y_222: [tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_Y_222[0]]), [tco_apply(shen_assignx45types, [KL_ARG_V777_219, KL_ARG_V778_220, KL_ARG_Y_222[1][0]]), []]]), KL_ARG_V779_221[1]])] if (shen_eq(symdic.symdic_kl_cond, KL_ARG_V779_221[0]) if shen_consp(KL_ARG_V779_221) else False) else ([setattr(KL_CTX, 'KL_LOC_NewTable_223', tco_apply(shen_typextable, [tco_apply(shen_getx45type, [KL_ARG_V779_221[0]]), KL_ARG_V779_221[1]])), [KL_ARG_V779_221[0], tco_apply(kl_map, [(lambda KL_ARG_Y_224: tail_call(shen_assignx45types, [KL_ARG_V777_219, tco_apply(kl_append, [KL_ARG_V778_220, KL_CTX.KL_LOC_NewTable_223]), KL_ARG_Y_224])), KL_ARG_V779_221[1]])]][(-1)] if shen_consp(KL_ARG_V779_221) else ([setattr(KL_CTX, 'KL_LOC_AtomType_225', tco_apply(kl_assoc, [KL_ARG_V779_221, KL_ARG_V778_220])), ([symdic.symdic_kl_type, [KL_ARG_V779_221, [KL_CTX.KL_LOC_AtomType_225[1], []]]] if shen_consp(KL_CTX.KL_LOC_AtomType_225) else (KL_ARG_V779_221 if tco_apply(kl_elementx63, [KL_ARG_V779_221, KL_ARG_V777_219]) else tail_call(shen_atomx45type, [KL_ARG_V779_221])))][(-1)] if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.assign-types', shen_assignx45types)

@tail_recursion
def shen_atomx45type(KL_ARG_V780_226):
    global symdic
    return ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_string, []]]] if isinstance(KL_ARG_V780_226, str) else ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_number, []]]] if isinstance(KL_ARG_V780_226, numbers.Number) else ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_boolean, []]]] if tco_apply(kl_booleanx63, [KL_ARG_V780_226]) else ([symdic.symdic_kl_type, [KL_ARG_V780_226, [symdic.symdic_kl_symbol, []]]] if tco_apply(kl_symbolx63, [KL_ARG_V780_226]) else KL_ARG_V780_226))))
shen_add_fun('shen.atom-type', shen_atomx45type)

@tail_recursion
def shen_storex45arity(KL_ARG_V783_227, KL_ARG_V784_228):
    global symdic
    return (symdic.symdic_shen_skip if shen_get(symdic.symdic_shen_x42installingx45klx42) else (tail_call(kl_put, [KL_ARG_V783_227, symdic.symdic_kl_arity, KL_ARG_V784_228, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.store-arity', shen_storex45arity)

@tail_recursion
def shen_reduce(KL_ARG_V785_229):

    class KL_Context:
        KL_LOC_Result_230 = None
    KL_CTX = KL_Context()
    global symdic
    return [shen_set(symdic.symdic_shen_x42teststackx42, []), [setattr(KL_CTX, 'KL_LOC_Result_230', tco_apply(shen_reduce_help, [KL_ARG_V785_229])), [[symdic.symdic_kl_x58, [symdic.symdic_shen_tests, tco_apply(kl_reverse, [shen_get(symdic.symdic_shen_x42teststackx42)])]], [KL_CTX.KL_LOC_Result_230, []]]][(-1)]][(-1)]
shen_add_fun('shen.reduce', shen_reduce)

@tail_recursion
def shen_reduce_help(KL_ARG_V786_231):

    class KL_Context:
        KL_LOC_Abstraction_232 = None
        KL_LOC_Application_233 = None
        KL_LOC_Abstraction_234 = None
        KL_LOC_Application_235 = None
        KL_LOC_Abstraction_236 = None
        KL_LOC_Application_237 = None
        KL_LOC_Abstraction_238 = None
        KL_LOC_Application_239 = None
        KL_LOC_Z_240 = None
    KL_CTX = KL_Context()
    global symdic
    return ([tco_apply(shen_add_test, [[symdic.symdic_kl_consx63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_232', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_233', [[KL_CTX.KL_LOC_Abstraction_232, [[symdic.symdic_kl_hd, KL_ARG_V786_231[1]], []]], [[symdic.symdic_kl_tl, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_233])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq([], KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if shen_eq(symdic.symdic_kl_cons, KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_kl_tuplex63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_234', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_235', [[KL_CTX.KL_LOC_Abstraction_234, [[symdic.symdic_kl_fst, KL_ARG_V786_231[1]], []]], [[symdic.symdic_kl_snd, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_235])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq([], KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if shen_eq(symdic.symdic_kl_x64p, KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_shen_x43vectorx63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_236', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_237', [[KL_CTX.KL_LOC_Abstraction_236, [[symdic.symdic_kl_hdv, KL_ARG_V786_231[1]], []]], [[symdic.symdic_kl_tlv, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_237])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq([], KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if shen_eq(symdic.symdic_kl_x64v, KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_shen_x43stringx63, KL_ARG_V786_231[1]]]), [setattr(KL_CTX, 'KL_LOC_Abstraction_238', [symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][0], [[symdic.symdic_kl_x47_, [KL_ARG_V786_231[0][1][0][1][1][0], [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]]), []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Application_239', [[KL_CTX.KL_LOC_Abstraction_238, [[symdic.symdic_kl_pos, [KL_ARG_V786_231[1][0], [0, []]]], []]], [[symdic.symdic_kl_tlstr, KL_ARG_V786_231[1]], []]]), tail_call(shen_reduce_help, [KL_CTX.KL_LOC_Application_239])][(-1)]][(-1)]][(-1)] if ((((((((((((shen_eq([], KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][0][1]) else False) if shen_eq(symdic.symdic_kl_x64s, KL_ARG_V786_231[0][1][0][0]) else False) if shen_consp(KL_ARG_V786_231[0][1][0]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [[symdic.symdic_kl_x61, [KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[1]]]]), tail_call(shen_reduce_help, [KL_ARG_V786_231[0][1][1][0]])][(-1)] if (((((((((not tco_apply(kl_variablex63, [KL_ARG_V786_231[0][1][0]])) if shen_eq([], KL_ARG_V786_231[1][1]) else False) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else (tail_call(shen_reduce_help, [tco_apply(shen_ebr, [KL_ARG_V786_231[1][0], KL_ARG_V786_231[0][1][0], KL_ARG_V786_231[0][1][1][0]])]) if (((((((shen_eq([], KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_eq([], KL_ARG_V786_231[0][1][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1][1]) else False) if shen_consp(KL_ARG_V786_231[0][1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V786_231[0][0]) else False) if shen_consp(KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([tco_apply(shen_add_test, [KL_ARG_V786_231[1][0]]), tail_call(shen_reduce_help, [KL_ARG_V786_231[1][1][0]])][(-1)] if ((((shen_eq([], KL_ARG_V786_231[1][1][1]) if shen_consp(KL_ARG_V786_231[1][1]) else False) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_eq(symdic.symdic_kl_where, KL_ARG_V786_231[0]) else False) if shen_consp(KL_ARG_V786_231) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_240', tco_apply(shen_reduce_help, [KL_ARG_V786_231[0]])), (KL_ARG_V786_231 if shen_eq(KL_ARG_V786_231[0], KL_CTX.KL_LOC_Z_240) else tail_call(shen_reduce_help, [[KL_CTX.KL_LOC_Z_240, KL_ARG_V786_231[1]]]))][(-1)] if ((shen_eq([], KL_ARG_V786_231[1][1]) if shen_consp(KL_ARG_V786_231[1]) else False) if shen_consp(KL_ARG_V786_231) else False) else (KL_ARG_V786_231 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.reduce_help', shen_reduce_help)

@tail_recursion
def shen_x43stringx63(KL_ARG_V787_241):
    global symdic
    return (False if shen_eq('', KL_ARG_V787_241) else (isinstance(KL_ARG_V787_241, str) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+string?', shen_x43stringx63)

@tail_recursion
def shen_x43vector(KL_ARG_V788_242):
    global symdic
    return (False if shen_eq(KL_ARG_V788_242, tco_apply(kl_vector, [0])) else (tail_call(kl_vectorx63, [KL_ARG_V788_242]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.+vector', shen_x43vector)

@tail_recursion
def shen_ebr(KL_ARG_V797_243, KL_ARG_V798_244, KL_ARG_V799_245):
    global symdic
    return (KL_ARG_V797_243 if shen_eq(KL_ARG_V799_245, KL_ARG_V798_244) else (KL_ARG_V799_245 if ((((((tco_apply(kl_occurrences, [KL_ARG_V798_244, KL_ARG_V799_245[1][0]]) > 0) if shen_eq([], KL_ARG_V799_245[1][1][1]) else False) if shen_consp(KL_ARG_V799_245[1][1]) else False) if shen_consp(KL_ARG_V799_245[1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V799_245[0]) else False) if shen_consp(KL_ARG_V799_245) else False) else ([symdic.symdic_kl_let, [KL_ARG_V799_245[1][0], [tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V799_245[1][0], KL_ARG_V799_245[1][1][0]]), KL_ARG_V799_245[1][1][1]]]] if ((((((shen_eq(KL_ARG_V799_245[1][0], KL_ARG_V798_244) if shen_eq([], KL_ARG_V799_245[1][1][1][1]) else False) if shen_consp(KL_ARG_V799_245[1][1][1]) else False) if shen_consp(KL_ARG_V799_245[1][1]) else False) if shen_consp(KL_ARG_V799_245[1]) else False) if shen_eq(symdic.symdic_kl_let, KL_ARG_V799_245[0]) else False) if shen_consp(KL_ARG_V799_245) else False) else ([tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V798_244, KL_ARG_V799_245[0]]), tco_apply(shen_ebr, [KL_ARG_V797_243, KL_ARG_V798_244, KL_ARG_V799_245[1]])] if shen_consp(KL_ARG_V799_245) else (KL_ARG_V799_245 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.ebr', shen_ebr)

@tail_recursion
def shen_add_test(KL_ARG_V802_246):
    global symdic
    return shen_set(symdic.symdic_shen_x42teststackx42, [KL_ARG_V802_246, shen_get(symdic.symdic_shen_x42teststackx42)])
shen_add_fun('shen.add_test', shen_add_test)

@tail_recursion
def shen_condx45expression(KL_ARG_V803_247, KL_ARG_V804_248, KL_ARG_V805_249):

    class KL_Context:
        KL_LOC_Err_250 = None
        KL_LOC_Cases_251 = None
        KL_LOC_EncodeChoices_252 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Err_250', tco_apply(shen_errx45condition, [KL_ARG_V803_247])), [setattr(KL_CTX, 'KL_LOC_Cases_251', tco_apply(shen_casex45form, [KL_ARG_V805_249, KL_CTX.KL_LOC_Err_250])), [setattr(KL_CTX, 'KL_LOC_EncodeChoices_252', tco_apply(shen_encodex45choices, [KL_CTX.KL_LOC_Cases_251, KL_ARG_V803_247])), tail_call(shen_condx45form, [KL_CTX.KL_LOC_EncodeChoices_252])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.cond-expression', shen_condx45expression)

@tail_recursion
def shen_condx45form(KL_ARG_V808_253):
    global symdic
    return (KL_ARG_V808_253[0][1][0] if ((((shen_eq([], KL_ARG_V808_253[0][1][1]) if shen_consp(KL_ARG_V808_253[0][1]) else False) if shen_eq(True, KL_ARG_V808_253[0][0]) else False) if shen_consp(KL_ARG_V808_253[0]) else False) if shen_consp(KL_ARG_V808_253) else False) else ([symdic.symdic_kl_cond, KL_ARG_V808_253] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cond-form', shen_condx45form)

@tail_recursion
def shen_encodex45choices(KL_ARG_V811_254, KL_ARG_V812_255):
    global symdic
    return ([] if shen_eq([], KL_ARG_V811_254) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V811_254[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [([symdic.symdic_shen_sysx45error, [KL_ARG_V812_255, []]] if shen_get(symdic.symdic_shen_x42installingx45klx42) else [symdic.symdic_shen_f_error, [KL_ARG_V812_255, []]]), [symdic.symdic_Result, []]]]], []]]]], []]], []] if (((((((((shen_eq([], KL_ARG_V811_254[1]) if shen_eq([], KL_ARG_V811_254[0][1][1]) else False) if shen_eq([], KL_ARG_V811_254[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V811_254[0][1][0][1]) else False) if shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V811_254[0][1][0][0]) else False) if shen_consp(KL_ARG_V811_254[0][1][0]) else False) if shen_consp(KL_ARG_V811_254[0][1]) else False) if shen_eq(True, KL_ARG_V811_254[0][0]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V811_254[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [KL_ARG_V811_254[1], KL_ARG_V812_255])]), [symdic.symdic_Result, []]]]], []]]]], []]], []] if ((((((((shen_eq([], KL_ARG_V811_254[0][1][1]) if shen_eq([], KL_ARG_V811_254[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V811_254[0][1][0][1]) else False) if shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V811_254[0][1][0][0]) else False) if shen_consp(KL_ARG_V811_254[0][1][0]) else False) if shen_consp(KL_ARG_V811_254[0][1]) else False) if shen_eq(True, KL_ARG_V811_254[0][0]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else ([[True, [[symdic.symdic_kl_let, [symdic.symdic_Freeze, [[symdic.symdic_kl_freeze, [tco_apply(shen_condx45form, [tco_apply(shen_encodex45choices, [KL_ARG_V811_254[1], KL_ARG_V812_255])]), []]], [[symdic.symdic_kl_if, [KL_ARG_V811_254[0][0], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V811_254[0][1][0][1][0], [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Result, [[symdic.symdic_kl_fail, []], []]]], [[symdic.symdic_kl_thaw, [symdic.symdic_Freeze, []]], [symdic.symdic_Result, []]]]], []]]]], [[symdic.symdic_kl_thaw, [symdic.symdic_Freeze, []]], []]]]], []]]]], []]], []] if (((((((shen_eq([], KL_ARG_V811_254[0][1][1]) if shen_eq([], KL_ARG_V811_254[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V811_254[0][1][0][1]) else False) if shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V811_254[0][1][0][0]) else False) if shen_consp(KL_ARG_V811_254[0][1][0]) else False) if shen_consp(KL_ARG_V811_254[0][1]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else ([KL_ARG_V811_254[0], tco_apply(shen_encodex45choices, [KL_ARG_V811_254[1], KL_ARG_V812_255])] if (((shen_eq([], KL_ARG_V811_254[0][1][1]) if shen_consp(KL_ARG_V811_254[0][1]) else False) if shen_consp(KL_ARG_V811_254[0]) else False) if shen_consp(KL_ARG_V811_254) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_encodex45choices]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.encode-choices', shen_encodex45choices)

@tail_recursion
def shen_casex45form(KL_ARG_V817_256, KL_ARG_V818_257):
    global symdic
    return ([KL_ARG_V818_257, []] if shen_eq([], KL_ARG_V817_256) else ([[True, KL_ARG_V817_256[0][1]], tco_apply(shen_casex45form, [KL_ARG_V817_256[1], KL_ARG_V818_257])] if ((((((((((((shen_eq([], KL_ARG_V817_256[0][1][1]) if shen_eq([], KL_ARG_V817_256[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V817_256[0][1][0][1]) else False) if shen_eq(symdic.symdic_shen_choicepointx33, KL_ARG_V817_256[0][1][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][1]) else False) if shen_eq([], KL_ARG_V817_256[0][0][1][1]) else False) if shen_eq(symdic.symdic_shen_tests, KL_ARG_V817_256[0][0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][0][1]) else False) if shen_eq(symdic.symdic_kl_x58, KL_ARG_V817_256[0][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][0]) else False) if shen_consp(KL_ARG_V817_256[0]) else False) if shen_consp(KL_ARG_V817_256) else False) else ([[True, KL_ARG_V817_256[0][1]], []] if ((((((((shen_eq([], KL_ARG_V817_256[0][1][1]) if shen_consp(KL_ARG_V817_256[0][1]) else False) if shen_eq([], KL_ARG_V817_256[0][0][1][1]) else False) if shen_eq(symdic.symdic_shen_tests, KL_ARG_V817_256[0][0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][0][1]) else False) if shen_eq(symdic.symdic_kl_x58, KL_ARG_V817_256[0][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][0]) else False) if shen_consp(KL_ARG_V817_256[0]) else False) if shen_consp(KL_ARG_V817_256) else False) else ([[tco_apply(shen_embedx45and, [KL_ARG_V817_256[0][0][1][1]]), KL_ARG_V817_256[0][1]], tco_apply(shen_casex45form, [KL_ARG_V817_256[1], KL_ARG_V818_257])] if (((((((shen_eq([], KL_ARG_V817_256[0][1][1]) if shen_consp(KL_ARG_V817_256[0][1]) else False) if shen_eq(symdic.symdic_shen_tests, KL_ARG_V817_256[0][0][1][0]) else False) if shen_consp(KL_ARG_V817_256[0][0][1]) else False) if shen_eq(symdic.symdic_kl_x58, KL_ARG_V817_256[0][0][0]) else False) if shen_consp(KL_ARG_V817_256[0][0]) else False) if shen_consp(KL_ARG_V817_256[0]) else False) if shen_consp(KL_ARG_V817_256) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_casex45form]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.case-form', shen_casex45form)

@tail_recursion
def shen_embedx45and(KL_ARG_V819_258):
    global symdic
    return (KL_ARG_V819_258[0] if (shen_eq([], KL_ARG_V819_258[1]) if shen_consp(KL_ARG_V819_258) else False) else ([symdic.symdic_kl_and, [KL_ARG_V819_258[0], [tco_apply(shen_embedx45and, [KL_ARG_V819_258[1]]), []]]] if shen_consp(KL_ARG_V819_258) else (tail_call(shen_sysx45error, [symdic.symdic_shen_embedx45and]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.embed-and', shen_embedx45and)

@tail_recursion
def shen_errx45condition(KL_ARG_V820_259):
    global symdic
    return [True, [[symdic.symdic_shen_f_error, [KL_ARG_V820_259, []]], []]]
shen_add_fun('shen.err-condition', shen_errx45condition)

@tail_recursion
def shen_sysx45error(KL_ARG_V821_260):
    global symdic
    return shen_simple_error(('system function ' + tco_apply(shen_app, [KL_ARG_V821_260, ': unexpected argument\r\n', symdic.symdic_shen_a])))
shen_add_fun('shen.sys-error', shen_sysx45error)


#============================== sys.kl==============================



@tail_recursion
def kl_thaw(KL_ARG_V1802_261):
    global symdic
    return shen_apply(KL_ARG_V1802_261, [])
shen_add_fun('thaw', kl_thaw)

@tail_recursion
def kl_eval(KL_ARG_V1803_262):

    class KL_Context:
        KL_LOC_Macroexpand_263 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Macroexpand_263', tco_apply(shen_walk, [(lambda KL_ARG_V1800_264: tail_call(kl_macroexpand, [KL_ARG_V1800_264])), KL_ARG_V1803_262])), (tail_call(kl_map, [symdic.symdic_shen_evalx45withoutx45macros, tco_apply(shen_packagex45contents, [KL_CTX.KL_LOC_Macroexpand_263])]) if tco_apply(shen_packagedx63, [KL_CTX.KL_LOC_Macroexpand_263]) else tail_call(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Macroexpand_263]))][(-1)]
shen_add_fun('eval', kl_eval)

@tail_recursion
def shen_evalx45withoutx45macros(KL_ARG_V1804_265):
    global symdic
    return shen_eval_kl(tco_apply(shen_elimx45define, [tco_apply(shen_procx45inputx43, [KL_ARG_V1804_265])]))
shen_add_fun('shen.eval-without-macros', shen_evalx45withoutx45macros)

@tail_recursion
def shen_procx45inputx43(KL_ARG_V1805_266):
    global symdic
    return ([symdic.symdic_kl_inputx43, [KL_ARG_V1805_266[1][0], [tco_apply(shen_rcons_form, [KL_ARG_V1805_266[1][1][0]]), []]]] if ((((shen_eq([], KL_ARG_V1805_266[1][1][1]) if shen_consp(KL_ARG_V1805_266[1][1]) else False) if shen_consp(KL_ARG_V1805_266[1]) else False) if shen_eq(symdic.symdic_kl_inputx43, KL_ARG_V1805_266[0]) else False) if shen_consp(KL_ARG_V1805_266) else False) else ([symdic.symdic_readx43, [KL_ARG_V1805_266[1][0], [tco_apply(shen_rcons_form, [KL_ARG_V1805_266[1][1][0]]), []]]] if ((((shen_eq([], KL_ARG_V1805_266[1][1][1]) if shen_consp(KL_ARG_V1805_266[1][1]) else False) if shen_consp(KL_ARG_V1805_266[1]) else False) if shen_eq(symdic.symdic_readx43, KL_ARG_V1805_266[0]) else False) if shen_consp(KL_ARG_V1805_266) else False) else (tail_call(kl_map, [symdic.symdic_shen_procx45inputx43, KL_ARG_V1805_266]) if shen_consp(KL_ARG_V1805_266) else (KL_ARG_V1805_266 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.proc-input+', shen_procx45inputx43)

@tail_recursion
def shen_elimx45define(KL_ARG_V1806_267):
    global symdic
    return (tail_call(shen_shenx45x62kl, [KL_ARG_V1806_267[1][0], KL_ARG_V1806_267[1][1]]) if ((shen_consp(KL_ARG_V1806_267[1]) if shen_eq(symdic.symdic_kl_define, KL_ARG_V1806_267[0]) else False) if shen_consp(KL_ARG_V1806_267) else False) else (tail_call(shen_elimx45define, [tco_apply(shen_yacc, [KL_ARG_V1806_267])]) if ((shen_consp(KL_ARG_V1806_267[1]) if shen_eq(symdic.symdic_kl_defcc, KL_ARG_V1806_267[0]) else False) if shen_consp(KL_ARG_V1806_267) else False) else (tail_call(kl_map, [symdic.symdic_shen_elimx45define, KL_ARG_V1806_267]) if shen_consp(KL_ARG_V1806_267) else (KL_ARG_V1806_267 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.elim-define', shen_elimx45define)

@tail_recursion
def shen_packagedx63(KL_ARG_V1813_268):
    global symdic
    return (True if (((shen_consp(KL_ARG_V1813_268[1][1]) if shen_consp(KL_ARG_V1813_268[1]) else False) if shen_eq(symdic.symdic_kl_package, KL_ARG_V1813_268[0]) else False) if shen_consp(KL_ARG_V1813_268) else False) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.packaged?', shen_packagedx63)

@tail_recursion
def kl_external(KL_ARG_V1814_269):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1814_269, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_270: shen_simple_error(('package ' + tco_apply(shen_app, [KL_ARG_V1814_269, ' has not been used.\r\n', symdic.symdic_shen_a])))))
shen_add_fun('external', kl_external)

@tail_recursion
def shen_packagex45contents(KL_ARG_V1817_271):
    global symdic
    return (KL_ARG_V1817_271[1][1][1] if ((((shen_consp(KL_ARG_V1817_271[1][1]) if shen_eq(symdic.symdic_kl_null, KL_ARG_V1817_271[1][0]) else False) if shen_consp(KL_ARG_V1817_271[1]) else False) if shen_eq(symdic.symdic_kl_package, KL_ARG_V1817_271[0]) else False) if shen_consp(KL_ARG_V1817_271) else False) else (tail_call(shen_packageh, [KL_ARG_V1817_271[1][0], KL_ARG_V1817_271[1][1][0], KL_ARG_V1817_271[1][1][1]]) if (((shen_consp(KL_ARG_V1817_271[1][1]) if shen_consp(KL_ARG_V1817_271[1]) else False) if shen_eq(symdic.symdic_kl_package, KL_ARG_V1817_271[0]) else False) if shen_consp(KL_ARG_V1817_271) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_packagex45contents]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.package-contents', shen_packagex45contents)

@tail_recursion
def shen_walk(KL_ARG_V1818_272, KL_ARG_V1819_273):
    global symdic
    return (shen_apply(KL_ARG_V1818_272, [tco_apply(kl_map, [(lambda KL_ARG_Z_274: tail_call(shen_walk, [KL_ARG_V1818_272, KL_ARG_Z_274])), KL_ARG_V1819_273])]) if shen_consp(KL_ARG_V1819_273) else (shen_apply(KL_ARG_V1818_272, [KL_ARG_V1819_273]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.walk', shen_walk)

@tail_recursion
def kl_compile(KL_ARG_V1820_275, KL_ARG_V1821_276, KL_ARG_V1822_277):

    class KL_Context:
        KL_LOC_O_278 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_O_278', shen_apply(KL_ARG_V1820_275, [[KL_ARG_V1821_276, [[], []]]])), (shen_apply(KL_ARG_V1822_277, [KL_CTX.KL_LOC_O_278]) if (True if shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_O_278) else (not tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_O_278[0]]))) else tail_call(shen_hdtl, [KL_CTX.KL_LOC_O_278]))][(-1)]
shen_add_fun('compile', kl_compile)

@tail_recursion
def kl_failx45if(KL_ARG_V1823_279, KL_ARG_V1824_280):
    global symdic
    return (tail_call(kl_fail, []) if shen_apply(KL_ARG_V1823_279, [KL_ARG_V1824_280]) else KL_ARG_V1824_280)
shen_add_fun('fail-if', kl_failx45if)

@tail_recursion
def kl_x64s(KL_ARG_V1825_281, KL_ARG_V1826_282):
    global symdic
    return (KL_ARG_V1825_281 + KL_ARG_V1826_282)
shen_add_fun('@s', kl_x64s)

@tail_recursion
def kl_tcx63(KL_ARG_V1831_283):
    global symdic
    return shen_get(symdic.symdic_shen_x42tcx42)
shen_add_fun('tc?', kl_tcx63)

@tail_recursion
def kl_ps(KL_ARG_V1832_284):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1832_284, symdic.symdic_shen_source, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_285: shen_simple_error(tco_apply(shen_app, [KL_ARG_V1832_284, ' not found.\r\n', symdic.symdic_shen_a]))))
shen_add_fun('ps', kl_ps)

@tail_recursion
def kl_stinput():
    global symdic
    return shen_get(symdic.symdic_kl_x42stinputx42)
shen_add_fun('stinput', kl_stinput)

@tail_recursion
def shen_x43vectorx63(KL_ARG_V1833_286):
    global symdic
    return ((shen_absvector_get(KL_ARG_V1833_286, 0) > 0) if shen_absvectorp(KL_ARG_V1833_286) else False)
shen_add_fun('shen.+vector?', shen_x43vectorx63)

@tail_recursion
def kl_vector(KL_ARG_V1834_287):

    class KL_Context:
        KL_LOC_Vector_288 = None
        KL_LOC_ZeroStamp_289 = None
        KL_LOC_Standard_290 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_288', shen_absvector((KL_ARG_V1834_287 + 1))), [setattr(KL_CTX, 'KL_LOC_ZeroStamp_289', shen_absvector_set(KL_CTX.KL_LOC_Vector_288, 0, KL_ARG_V1834_287)), [setattr(KL_CTX, 'KL_LOC_Standard_290', (KL_CTX.KL_LOC_ZeroStamp_289 if shen_eq(KL_ARG_V1834_287, 0) else tco_apply(shen_fillvector, [KL_CTX.KL_LOC_ZeroStamp_289, 1, KL_ARG_V1834_287, tco_apply(kl_fail, [])]))), KL_CTX.KL_LOC_Standard_290][(-1)]][(-1)]][(-1)]
shen_add_fun('vector', kl_vector)

@tail_recursion
def shen_fillvector(KL_ARG_V1835_291, KL_ARG_V1836_292, KL_ARG_V1837_293, KL_ARG_V1838_294):
    global symdic
    return (shen_absvector_set(KL_ARG_V1835_291, KL_ARG_V1837_293, KL_ARG_V1838_294) if shen_eq(KL_ARG_V1837_293, KL_ARG_V1836_292) else (tail_call(shen_fillvector, [shen_absvector_set(KL_ARG_V1835_291, KL_ARG_V1836_292, KL_ARG_V1838_294), (1 + KL_ARG_V1836_292), KL_ARG_V1837_293, KL_ARG_V1838_294]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fillvector', shen_fillvector)

@tail_recursion
def kl_vectorx63(KL_ARG_V1840_295):
    global symdic
    return (shen_try_except((lambda : (shen_absvector_get(KL_ARG_V1840_295, 0) >= 0)), (lambda KL_ARG_E_296: False)) if shen_absvectorp(KL_ARG_V1840_295) else False)
shen_add_fun('vector?', kl_vectorx63)

@tail_recursion
def kl_vectorx45x62(KL_ARG_V1841_297, KL_ARG_V1842_298, KL_ARG_V1843_299):
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if shen_eq(KL_ARG_V1842_298, 0) else shen_absvector_set(KL_ARG_V1841_297, KL_ARG_V1842_298, KL_ARG_V1843_299))
shen_add_fun('vector->', kl_vectorx45x62)

@tail_recursion
def kl_x60x45vector(KL_ARG_V1844_300, KL_ARG_V1845_301):

    class KL_Context:
        KL_LOC_VectorElement_302 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('cannot access 0th element of a vector\r\n') if shen_eq(KL_ARG_V1845_301, 0) else [setattr(KL_CTX, 'KL_LOC_VectorElement_302', shen_absvector_get(KL_ARG_V1844_300, KL_ARG_V1845_301)), (shen_simple_error('vector element not found\r\n') if shen_eq(KL_CTX.KL_LOC_VectorElement_302, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_VectorElement_302)][(-1)])
shen_add_fun('<-vector', kl_x60x45vector)

@tail_recursion
def shen_posintx63(KL_ARG_V1846_303):
    global symdic
    return ((KL_ARG_V1846_303 >= 0) if tco_apply(kl_integerx63, [KL_ARG_V1846_303]) else False)
shen_add_fun('shen.posint?', shen_posintx63)

@tail_recursion
def kl_limit(KL_ARG_V1847_304):
    global symdic
    return shen_absvector_get(KL_ARG_V1847_304, 0)
shen_add_fun('limit', kl_limit)

@tail_recursion
def kl_symbolx63(KL_ARG_V1848_305):

    class KL_Context:
        KL_LOC_String_306 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (True if tco_apply(kl_booleanx63, [KL_ARG_V1848_305]) else (True if isinstance(KL_ARG_V1848_305, numbers.Number) else isinstance(KL_ARG_V1848_305, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_306', str(KL_ARG_V1848_305)), tco_apply(shen_analysex45symbolx63, [KL_CTX.KL_LOC_String_306])][(-1)]), (lambda KL_ARG_E_307: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('symbol?', kl_symbolx63)

@tail_recursion
def shen_analysex45symbolx63(KL_ARG_V1849_308):
    global symdic
    return ((tail_call(shen_alphanumsx63, [KL_ARG_V1849_308[1:]]) if tco_apply(shen_alphax63, [KL_ARG_V1849_308[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1849_308]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45symbolx63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-symbol?', shen_analysex45symbolx63)

@tail_recursion
def shen_alphax63(KL_ARG_V1850_309):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1850_309, ['A', ['B', ['C', ['D', ['E', ['F', ['G', ['H', ['I', ['J', ['K', ['L', ['M', ['N', ['O', ['P', ['Q', ['R', ['S', ['T', ['U', ['V', ['W', ['X', ['Y', ['Z', ['a', ['b', ['c', ['d', ['e', ['f', ['g', ['h', ['i', ['j', ['k', ['l', ['m', ['n', ['o', ['p', ['q', ['r', ['s', ['t', ['u', ['v', ['w', ['x', ['y', ['z', ['=', ['*', ['/', ['+', ['-', ['_', ['?', ['$', ['!', ['@', ['~', ['>', ['<', ['&', ['%', ['{', ['}', [':', [';', ['`', ['#', ["'", ['.', []]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_add_fun('shen.alpha?', shen_alphax63)

@tail_recursion
def shen_alphanumsx63(KL_ARG_V1851_310):
    global symdic
    return (True if shen_eq('', KL_ARG_V1851_310) else ((tail_call(shen_alphanumsx63, [KL_ARG_V1851_310[1:]]) if tco_apply(shen_alphanumx63, [KL_ARG_V1851_310[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1851_310]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_alphanumsx63]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.alphanums?', shen_alphanumsx63)

@tail_recursion
def shen_alphanumx63(KL_ARG_V1852_311):
    global symdic
    return (True if tco_apply(shen_alphax63, [KL_ARG_V1852_311]) else tail_call(shen_digitx63, [KL_ARG_V1852_311]))
shen_add_fun('shen.alphanum?', shen_alphanumx63)

@tail_recursion
def shen_digitx63(KL_ARG_V1853_312):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1853_312, ['1', ['2', ['3', ['4', ['5', ['6', ['7', ['8', ['9', ['0', []]]]]]]]]]]])
shen_add_fun('shen.digit?', shen_digitx63)

@tail_recursion
def kl_variablex63(KL_ARG_V1854_313):

    class KL_Context:
        KL_LOC_String_314 = None
    KL_CTX = KL_Context()
    global symdic
    return (False if (True if tco_apply(kl_booleanx63, [KL_ARG_V1854_313]) else (True if isinstance(KL_ARG_V1854_313, numbers.Number) else isinstance(KL_ARG_V1854_313, str))) else (shen_try_except((lambda : [setattr(KL_CTX, 'KL_LOC_String_314', str(KL_ARG_V1854_313)), tco_apply(shen_analysex45variablex63, [KL_CTX.KL_LOC_String_314])][(-1)]), (lambda KL_ARG_E_315: False)) if True else shen_simple_error('condition failure')))
shen_add_fun('variable?', kl_variablex63)

@tail_recursion
def shen_analysex45variablex63(KL_ARG_V1855_316):
    global symdic
    return ((tail_call(shen_alphanumsx63, [KL_ARG_V1855_316[1:]]) if tco_apply(shen_uppercasex63, [KL_ARG_V1855_316[0]]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V1855_316]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_analysex45variablex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.analyse-variable?', shen_analysex45variablex63)

@tail_recursion
def shen_uppercasex63(KL_ARG_V1856_317):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V1856_317, ['A', ['B', ['C', ['D', ['E', ['F', ['G', ['H', ['I', ['J', ['K', ['L', ['M', ['N', ['O', ['P', ['Q', ['R', ['S', ['T', ['U', ['V', ['W', ['X', ['Y', ['Z', []]]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_add_fun('shen.uppercase?', shen_uppercasex63)

@tail_recursion
def kl_gensym(KL_ARG_V1857_318):
    global symdic
    return tail_call(kl_concat, [KL_ARG_V1857_318, shen_set(symdic.symdic_shen_x42gensymx42, (1 + shen_get(symdic.symdic_shen_x42gensymx42)))])
shen_add_fun('gensym', kl_gensym)

@tail_recursion
def kl_concat(KL_ARG_V1858_319, KL_ARG_V1859_320):
    global symdic
    return shen_intern((str(KL_ARG_V1858_319) + str(KL_ARG_V1859_320)))
shen_add_fun('concat', kl_concat)

@tail_recursion
def kl_x64p(KL_ARG_V1860_321, KL_ARG_V1861_322):

    class KL_Context:
        KL_LOC_Vector_323 = None
        KL_LOC_Tag_324 = None
        KL_LOC_Fst_325 = None
        KL_LOC_Snd_326 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_323', shen_absvector(3)), [setattr(KL_CTX, 'KL_LOC_Tag_324', shen_absvector_set(KL_CTX.KL_LOC_Vector_323, 0, symdic.symdic_shen_tuple)), [setattr(KL_CTX, 'KL_LOC_Fst_325', shen_absvector_set(KL_CTX.KL_LOC_Vector_323, 1, KL_ARG_V1860_321)), [setattr(KL_CTX, 'KL_LOC_Snd_326', shen_absvector_set(KL_CTX.KL_LOC_Vector_323, 2, KL_ARG_V1861_322)), KL_CTX.KL_LOC_Vector_323][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('@p', kl_x64p)

@tail_recursion
def kl_fst(KL_ARG_V1862_327):
    global symdic
    return shen_absvector_get(KL_ARG_V1862_327, 1)
shen_add_fun('fst', kl_fst)

@tail_recursion
def kl_snd(KL_ARG_V1863_328):
    global symdic
    return shen_absvector_get(KL_ARG_V1863_328, 2)
shen_add_fun('snd', kl_snd)

@tail_recursion
def kl_tuplex63(KL_ARG_V1864_329):
    global symdic
    return shen_try_except((lambda : (shen_eq(symdic.symdic_shen_tuple, shen_absvector_get(KL_ARG_V1864_329, 0)) if shen_absvectorp(KL_ARG_V1864_329) else False)), (lambda KL_ARG_E_330: False))
shen_add_fun('tuple?', kl_tuplex63)

@tail_recursion
def kl_append(KL_ARG_V1865_331, KL_ARG_V1866_332):
    global symdic
    return (KL_ARG_V1866_332 if shen_eq([], KL_ARG_V1865_331) else ([KL_ARG_V1865_331[0], tco_apply(kl_append, [KL_ARG_V1865_331[1], KL_ARG_V1866_332])] if shen_consp(KL_ARG_V1865_331) else (tail_call(shen_sysx45error, [symdic.symdic_kl_append]) if True else shen_simple_error('condition failure'))))
shen_add_fun('append', kl_append)

@tail_recursion
def kl_x64v(KL_ARG_V1867_333, KL_ARG_V1868_334):

    class KL_Context:
        KL_LOC_Limit_335 = None
        KL_LOC_NewVector_336 = None
        KL_LOC_Xx43NewVector_337 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_335', tco_apply(kl_limit, [KL_ARG_V1868_334])), [setattr(KL_CTX, 'KL_LOC_NewVector_336', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_335 + 1)])), [setattr(KL_CTX, 'KL_LOC_Xx43NewVector_337', tco_apply(kl_vectorx45x62, [KL_CTX.KL_LOC_NewVector_336, 1, KL_ARG_V1867_333])), (KL_CTX.KL_LOC_Xx43NewVector_337 if shen_eq(KL_CTX.KL_LOC_Limit_335, 0) else tail_call(shen_x64vx45help, [KL_ARG_V1868_334, 1, KL_CTX.KL_LOC_Limit_335, KL_CTX.KL_LOC_Xx43NewVector_337]))][(-1)]][(-1)]][(-1)]
shen_add_fun('@v', kl_x64v)

@tail_recursion
def shen_x64vx45help(KL_ARG_V1869_338, KL_ARG_V1870_339, KL_ARG_V1871_340, KL_ARG_V1872_341):
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1869_338, KL_ARG_V1872_341, KL_ARG_V1871_340, (KL_ARG_V1871_340 + 1)]) if shen_eq(KL_ARG_V1871_340, KL_ARG_V1870_339) else (tail_call(shen_x64vx45help, [KL_ARG_V1869_338, (KL_ARG_V1870_339 + 1), KL_ARG_V1871_340, tco_apply(shen_copyfromvector, [KL_ARG_V1869_338, KL_ARG_V1872_341, KL_ARG_V1870_339, (KL_ARG_V1870_339 + 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.@v-help', shen_x64vx45help)

@tail_recursion
def shen_copyfromvector(KL_ARG_V1874_342, KL_ARG_V1875_343, KL_ARG_V1876_344, KL_ARG_V1877_345):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_vectorx45x62, [KL_ARG_V1875_343, KL_ARG_V1877_345, tco_apply(kl_x60x45vector, [KL_ARG_V1874_342, KL_ARG_V1876_344])])), (lambda KL_ARG_E_346: KL_ARG_V1875_343))
shen_add_fun('shen.copyfromvector', shen_copyfromvector)

@tail_recursion
def kl_hdv(KL_ARG_V1878_347):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1878_347, 1])), (lambda KL_ARG_E_348: shen_simple_error(('hdv needs a non-empty vector as an argument; not ' + tco_apply(shen_app, [KL_ARG_V1878_347, '\r\n', symdic.symdic_shen_s])))))
shen_add_fun('hdv', kl_hdv)

@tail_recursion
def kl_tlv(KL_ARG_V1879_349):

    class KL_Context:
        KL_LOC_Limit_350 = None
        KL_LOC_NewVector_351 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Limit_350', tco_apply(kl_limit, [KL_ARG_V1879_349])), (shen_simple_error('cannot take the tail of the empty vector\r\n') if shen_eq(KL_CTX.KL_LOC_Limit_350, 0) else (tail_call(kl_vector, [0]) if shen_eq(KL_CTX.KL_LOC_Limit_350, 1) else [setattr(KL_CTX, 'KL_LOC_NewVector_351', tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_350 - 1)])), tail_call(shen_tlvx45help, [KL_ARG_V1879_349, 2, KL_CTX.KL_LOC_Limit_350, tco_apply(kl_vector, [(KL_CTX.KL_LOC_Limit_350 - 1)])])][(-1)]))][(-1)]
shen_add_fun('tlv', kl_tlv)

@tail_recursion
def shen_tlvx45help(KL_ARG_V1880_352, KL_ARG_V1881_353, KL_ARG_V1882_354, KL_ARG_V1883_355):
    global symdic
    return (tail_call(shen_copyfromvector, [KL_ARG_V1880_352, KL_ARG_V1883_355, KL_ARG_V1882_354, (KL_ARG_V1882_354 - 1)]) if shen_eq(KL_ARG_V1882_354, KL_ARG_V1881_353) else (tail_call(shen_tlvx45help, [KL_ARG_V1880_352, (KL_ARG_V1881_353 + 1), KL_ARG_V1882_354, tco_apply(shen_copyfromvector, [KL_ARG_V1880_352, KL_ARG_V1883_355, KL_ARG_V1881_353, (KL_ARG_V1881_353 - 1)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tlv-help', shen_tlvx45help)

@tail_recursion
def kl_assoc(KL_ARG_V1893_356, KL_ARG_V1894_357):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1894_357) else (KL_ARG_V1894_357[0] if ((shen_eq(KL_ARG_V1894_357[0][0], KL_ARG_V1893_356) if shen_consp(KL_ARG_V1894_357[0]) else False) if shen_consp(KL_ARG_V1894_357) else False) else (tail_call(kl_assoc, [KL_ARG_V1893_356, KL_ARG_V1894_357[1]]) if shen_consp(KL_ARG_V1894_357) else (tail_call(shen_sysx45error, [symdic.symdic_kl_assoc]) if True else shen_simple_error('condition failure')))))
shen_add_fun('assoc', kl_assoc)

@tail_recursion
def kl_booleanx63(KL_ARG_V1900_358):
    global symdic
    return (True if shen_eq(True, KL_ARG_V1900_358) else (True if shen_eq(False, KL_ARG_V1900_358) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('boolean?', kl_booleanx63)

@tail_recursion
def kl_nl(KL_ARG_V1901_359):
    global symdic
    return (0 if shen_eq(0, KL_ARG_V1901_359) else ([tco_apply(shen_prhush, ['\r\n', tco_apply(kl_stoutput, [])]), tail_call(kl_nl, [(KL_ARG_V1901_359 - 1)])][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('nl', kl_nl)

@tail_recursion
def kl_difference(KL_ARG_V1904_360, KL_ARG_V1905_361):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1904_360) else ((tail_call(kl_difference, [KL_ARG_V1904_360[1], KL_ARG_V1905_361]) if tco_apply(kl_elementx63, [KL_ARG_V1904_360[0], KL_ARG_V1905_361]) else [KL_ARG_V1904_360[0], tco_apply(kl_difference, [KL_ARG_V1904_360[1], KL_ARG_V1905_361])]) if shen_consp(KL_ARG_V1904_360) else (tail_call(shen_sysx45error, [symdic.symdic_kl_difference]) if True else shen_simple_error('condition failure'))))
shen_add_fun('difference', kl_difference)

@tail_recursion
def kl_do(KL_ARG_V1906_362, KL_ARG_V1907_363):
    global symdic
    return KL_ARG_V1907_363
shen_add_fun('do', kl_do)

@tail_recursion
def kl_elementx63(KL_ARG_V1916_364, KL_ARG_V1917_365):
    global symdic
    return (False if shen_eq([], KL_ARG_V1917_365) else (True if (shen_eq(KL_ARG_V1917_365[0], KL_ARG_V1916_364) if shen_consp(KL_ARG_V1917_365) else False) else (tail_call(kl_elementx63, [KL_ARG_V1916_364, KL_ARG_V1917_365[1]]) if shen_consp(KL_ARG_V1917_365) else (tail_call(shen_sysx45error, [symdic.symdic_kl_elementx63]) if True else shen_simple_error('condition failure')))))
shen_add_fun('element?', kl_elementx63)

@tail_recursion
def kl_emptyx63(KL_ARG_V1923_366):
    global symdic
    return (True if shen_eq([], KL_ARG_V1923_366) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('empty?', kl_emptyx63)

@tail_recursion
def kl_fix(KL_ARG_V1924_367, KL_ARG_V1925_368):
    global symdic
    return tail_call(shen_fixx45help, [KL_ARG_V1924_367, KL_ARG_V1925_368, shen_apply(KL_ARG_V1924_367, [KL_ARG_V1925_368])])
shen_add_fun('fix', kl_fix)

@tail_recursion
def shen_fixx45help(KL_ARG_V1932_369, KL_ARG_V1933_370, KL_ARG_V1934_371):
    global symdic
    return (KL_ARG_V1934_371 if shen_eq(KL_ARG_V1934_371, KL_ARG_V1933_370) else (tail_call(shen_fixx45help, [KL_ARG_V1932_369, KL_ARG_V1934_371, shen_apply(KL_ARG_V1932_369, [KL_ARG_V1934_371])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.fix-help', shen_fixx45help)

@tail_recursion
def kl_put(KL_ARG_V1936_372, KL_ARG_V1937_373, KL_ARG_V1938_374, KL_ARG_V1939_375):

    class KL_Context:
        KL_LOC_N_376 = None
        KL_LOC_Entry_377 = None
        KL_LOC_Change_379 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_376', tco_apply(kl_hash, [KL_ARG_V1936_372, tco_apply(kl_limit, [KL_ARG_V1939_375])])), [setattr(KL_CTX, 'KL_LOC_Entry_377', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1939_375, KL_CTX.KL_LOC_N_376])), (lambda KL_ARG_E_378: []))), [setattr(KL_CTX, 'KL_LOC_Change_379', tco_apply(kl_vectorx45x62, [KL_ARG_V1939_375, KL_CTX.KL_LOC_N_376, tco_apply(shen_changex45pointerx45value, [KL_ARG_V1936_372, KL_ARG_V1937_373, KL_ARG_V1938_374, KL_CTX.KL_LOC_Entry_377])])), KL_ARG_V1938_374][(-1)]][(-1)]][(-1)]
shen_add_fun('put', kl_put)

@tail_recursion
def shen_changex45pointerx45value(KL_ARG_V1942_380, KL_ARG_V1943_381, KL_ARG_V1944_382, KL_ARG_V1945_383):
    global symdic
    return ([[[KL_ARG_V1942_380, [KL_ARG_V1943_381, []]], KL_ARG_V1944_382], []] if shen_eq([], KL_ARG_V1945_383) else ([[KL_ARG_V1945_383[0][0], KL_ARG_V1944_382], KL_ARG_V1945_383[1]] if ((((((shen_eq(KL_ARG_V1945_383[0][0][0], KL_ARG_V1942_380) if shen_eq(KL_ARG_V1945_383[0][0][1][0], KL_ARG_V1943_381) else False) if shen_eq([], KL_ARG_V1945_383[0][0][1][1]) else False) if shen_consp(KL_ARG_V1945_383[0][0][1]) else False) if shen_consp(KL_ARG_V1945_383[0][0]) else False) if shen_consp(KL_ARG_V1945_383[0]) else False) if shen_consp(KL_ARG_V1945_383) else False) else ([KL_ARG_V1945_383[0], tco_apply(shen_changex45pointerx45value, [KL_ARG_V1942_380, KL_ARG_V1943_381, KL_ARG_V1944_382, KL_ARG_V1945_383[1]])] if shen_consp(KL_ARG_V1945_383) else (tail_call(shen_sysx45error, [symdic.symdic_shen_changex45pointerx45value]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.change-pointer-value', shen_changex45pointerx45value)

@tail_recursion
def kl_get(KL_ARG_V1948_384, KL_ARG_V1949_385, KL_ARG_V1950_386):

    class KL_Context:
        KL_LOC_N_387 = None
        KL_LOC_Entry_388 = None
        KL_LOC_Result_390 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_N_387', tco_apply(kl_hash, [KL_ARG_V1948_384, tco_apply(kl_limit, [KL_ARG_V1950_386])])), [setattr(KL_CTX, 'KL_LOC_Entry_388', shen_try_except((lambda : tco_apply(kl_x60x45vector, [KL_ARG_V1950_386, KL_CTX.KL_LOC_N_387])), (lambda KL_ARG_E_389: shen_simple_error('pointer not found\r\n')))), [setattr(KL_CTX, 'KL_LOC_Result_390', tco_apply(kl_assoc, [[KL_ARG_V1948_384, [KL_ARG_V1949_385, []]], KL_CTX.KL_LOC_Entry_388])), (shen_simple_error('value not found\r\n') if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Result_390]) else KL_CTX.KL_LOC_Result_390[1])][(-1)]][(-1)]][(-1)]
shen_add_fun('get', kl_get)

@tail_recursion
def kl_hash(KL_ARG_V1951_391, KL_ARG_V1952_392):

    class KL_Context:
        KL_LOC_Hash_393 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Hash_393', tco_apply(shen_mod, [tco_apply(shen_sum, [tco_apply(kl_map, [(lambda KL_ARG_V1801_394: ord(KL_ARG_V1801_394)), tco_apply(kl_explode, [KL_ARG_V1951_391])])]), KL_ARG_V1952_392])), (1 if shen_eq(0, KL_CTX.KL_LOC_Hash_393) else KL_CTX.KL_LOC_Hash_393)][(-1)]
shen_add_fun('hash', kl_hash)

@tail_recursion
def shen_mod(KL_ARG_V1953_395, KL_ARG_V1954_396):
    global symdic
    return tail_call(shen_modh, [KL_ARG_V1953_395, tco_apply(shen_multiples, [KL_ARG_V1953_395, [KL_ARG_V1954_396, []]])])
shen_add_fun('shen.mod', shen_mod)

@tail_recursion
def shen_multiples(KL_ARG_V1955_397, KL_ARG_V1956_398):
    global symdic
    return (KL_ARG_V1956_398[1] if ((KL_ARG_V1956_398[0] > KL_ARG_V1955_397) if shen_consp(KL_ARG_V1956_398) else False) else (tail_call(shen_multiples, [KL_ARG_V1955_397, [(2 * KL_ARG_V1956_398[0]), KL_ARG_V1956_398]]) if shen_consp(KL_ARG_V1956_398) else (tail_call(shen_sysx45error, [symdic.symdic_shen_multiples]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.multiples', shen_multiples)

@tail_recursion
def shen_modh(KL_ARG_V1959_399, KL_ARG_V1960_400):
    global symdic
    return (0 if shen_eq(0, KL_ARG_V1959_399) else (KL_ARG_V1959_399 if shen_eq([], KL_ARG_V1960_400) else ((KL_ARG_V1959_399 if tco_apply(kl_emptyx63, [KL_ARG_V1960_400[1]]) else tail_call(shen_modh, [KL_ARG_V1959_399, KL_ARG_V1960_400[1]])) if ((KL_ARG_V1960_400[0] > KL_ARG_V1959_399) if shen_consp(KL_ARG_V1960_400) else False) else (tail_call(shen_modh, [(KL_ARG_V1959_399 - KL_ARG_V1960_400[0]), KL_ARG_V1960_400]) if shen_consp(KL_ARG_V1960_400) else (tail_call(shen_sysx45error, [symdic.symdic_shen_modh]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.modh', shen_modh)

@tail_recursion
def shen_sum(KL_ARG_V1961_401):
    global symdic
    return (0 if shen_eq([], KL_ARG_V1961_401) else ((KL_ARG_V1961_401[0] + tco_apply(shen_sum, [KL_ARG_V1961_401[1]])) if shen_consp(KL_ARG_V1961_401) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sum]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.sum', shen_sum)

@tail_recursion
def kl_head(KL_ARG_V1968_402):
    global symdic
    return (KL_ARG_V1968_402[0] if shen_consp(KL_ARG_V1968_402) else (shen_simple_error('head expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('head', kl_head)

@tail_recursion
def kl_tail(KL_ARG_V1975_403):
    global symdic
    return (KL_ARG_V1975_403[1] if shen_consp(KL_ARG_V1975_403) else (shen_simple_error('tail expects a non-empty list') if True else shen_simple_error('condition failure')))
shen_add_fun('tail', kl_tail)

@tail_recursion
def kl_hdstr(KL_ARG_V1976_404):
    global symdic
    return KL_ARG_V1976_404[0]
shen_add_fun('hdstr', kl_hdstr)

@tail_recursion
def kl_intersection(KL_ARG_V1979_405, KL_ARG_V1980_406):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1979_405) else (([KL_ARG_V1979_405[0], tco_apply(kl_intersection, [KL_ARG_V1979_405[1], KL_ARG_V1980_406])] if tco_apply(kl_elementx63, [KL_ARG_V1979_405[0], KL_ARG_V1980_406]) else tail_call(kl_intersection, [KL_ARG_V1979_405[1], KL_ARG_V1980_406])) if shen_consp(KL_ARG_V1979_405) else (tail_call(shen_sysx45error, [symdic.symdic_kl_intersection]) if True else shen_simple_error('condition failure'))))
shen_add_fun('intersection', kl_intersection)

@tail_recursion
def kl_reverse(KL_ARG_V1981_407):
    global symdic
    return tail_call(shen_reverse_help, [KL_ARG_V1981_407, []])
shen_add_fun('reverse', kl_reverse)

@tail_recursion
def shen_reverse_help(KL_ARG_V1982_408, KL_ARG_V1983_409):
    global symdic
    return (KL_ARG_V1983_409 if shen_eq([], KL_ARG_V1982_408) else (tail_call(shen_reverse_help, [KL_ARG_V1982_408[1], [KL_ARG_V1982_408[0], KL_ARG_V1983_409]]) if shen_consp(KL_ARG_V1982_408) else (tail_call(shen_sysx45error, [symdic.symdic_shen_reverse_help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.reverse_help', shen_reverse_help)

@tail_recursion
def kl_union(KL_ARG_V1984_410, KL_ARG_V1985_411):
    global symdic
    return (KL_ARG_V1985_411 if shen_eq([], KL_ARG_V1984_410) else ((tail_call(kl_union, [KL_ARG_V1984_410[1], KL_ARG_V1985_411]) if tco_apply(kl_elementx63, [KL_ARG_V1984_410[0], KL_ARG_V1985_411]) else [KL_ARG_V1984_410[0], tco_apply(kl_union, [KL_ARG_V1984_410[1], KL_ARG_V1985_411])]) if shen_consp(KL_ARG_V1984_410) else (tail_call(shen_sysx45error, [symdic.symdic_kl_union]) if True else shen_simple_error('condition failure'))))
shen_add_fun('union', kl_union)

@tail_recursion
def kl_yx45orx45nx63(KL_ARG_V1986_412):

    class KL_Context:
        KL_LOC_Message_413 = None
        KL_LOC_Yx45orx45N_414 = None
        KL_LOC_Input_415 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Message_413', tco_apply(shen_prhush, [tco_apply(shen_procx45nl, [KL_ARG_V1986_412]), tco_apply(kl_stoutput, [])])), [setattr(KL_CTX, 'KL_LOC_Yx45orx45N_414', tco_apply(shen_prhush, [' (y/n) ', tco_apply(kl_stoutput, [])])), [setattr(KL_CTX, 'KL_LOC_Input_415', tco_apply(shen_app, [tco_apply(kl_input, []), '', symdic.symdic_shen_s])), (True if shen_eq('y', KL_CTX.KL_LOC_Input_415) else (False if shen_eq('n', KL_CTX.KL_LOC_Input_415) else [tco_apply(shen_prhush, ['please answer y or n\r\n', tco_apply(kl_stoutput, [])]), tail_call(kl_yx45orx45nx63, [KL_ARG_V1986_412])][(-1)]))][(-1)]][(-1)]][(-1)]
shen_add_fun('y-or-n?', kl_yx45orx45nx63)

@tail_recursion
def kl_not(KL_ARG_V1987_416):
    global symdic
    return (False if KL_ARG_V1987_416 else True)
shen_add_fun('not', kl_not)

@tail_recursion
def kl_subst(KL_ARG_V1996_417, KL_ARG_V1997_418, KL_ARG_V1998_419):
    global symdic
    return (KL_ARG_V1996_417 if shen_eq(KL_ARG_V1998_419, KL_ARG_V1997_418) else ([tco_apply(kl_subst, [KL_ARG_V1996_417, KL_ARG_V1997_418, KL_ARG_V1998_419[0]]), tco_apply(kl_subst, [KL_ARG_V1996_417, KL_ARG_V1997_418, KL_ARG_V1998_419[1]])] if shen_consp(KL_ARG_V1998_419) else (KL_ARG_V1998_419 if True else shen_simple_error('condition failure'))))
shen_add_fun('subst', kl_subst)

@tail_recursion
def kl_explode(KL_ARG_V2000_420):
    global symdic
    return tail_call(shen_explodex45h, [tco_apply(shen_app, [KL_ARG_V2000_420, '', symdic.symdic_shen_a])])
shen_add_fun('explode', kl_explode)

@tail_recursion
def shen_explodex45h(KL_ARG_V2001_421):
    global symdic
    return ([] if shen_eq('', KL_ARG_V2001_421) else ([KL_ARG_V2001_421[0], tco_apply(shen_explodex45h, [KL_ARG_V2001_421[1:]])] if tco_apply(shen_x43stringx63, [KL_ARG_V2001_421]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explodex45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.explode-h', shen_explodex45h)

@tail_recursion
def kl_cd(KL_ARG_V2002_422):
    global symdic
    return shen_set(symdic.symdic_kl_x42homex45directoryx42, ('' if shen_eq(KL_ARG_V2002_422, '') else tco_apply(shen_app, [KL_ARG_V2002_422, '/', symdic.symdic_shen_a])))
shen_add_fun('cd', kl_cd)

@tail_recursion
def kl_map(KL_ARG_V2003_423, KL_ARG_V2004_424):
    global symdic
    return tail_call(shen_mapx45h, [KL_ARG_V2003_423, KL_ARG_V2004_424, []])
shen_add_fun('map', kl_map)

@tail_recursion
def shen_mapx45h(KL_ARG_V2007_425, KL_ARG_V2008_426, KL_ARG_V2009_427):
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V2009_427]) if shen_eq([], KL_ARG_V2008_426) else (tail_call(shen_mapx45h, [KL_ARG_V2007_425, KL_ARG_V2008_426[1], [shen_apply(KL_ARG_V2007_425, [KL_ARG_V2008_426[0]]), KL_ARG_V2009_427]]) if shen_consp(KL_ARG_V2008_426) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mapx45h]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.map-h', shen_mapx45h)

@tail_recursion
def kl_length(KL_ARG_V2010_428):
    global symdic
    return tail_call(shen_lengthx45h, [KL_ARG_V2010_428, 0])
shen_add_fun('length', kl_length)

@tail_recursion
def shen_lengthx45h(KL_ARG_V2011_429, KL_ARG_V2012_430):
    global symdic
    return (KL_ARG_V2012_430 if shen_eq([], KL_ARG_V2011_429) else (tail_call(shen_lengthx45h, [KL_ARG_V2011_429[1], (KL_ARG_V2012_430 + 1)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.length-h', shen_lengthx45h)

@tail_recursion
def kl_occurrences(KL_ARG_V2021_431, KL_ARG_V2022_432):
    global symdic
    return (1 if shen_eq(KL_ARG_V2022_432, KL_ARG_V2021_431) else ((tco_apply(kl_occurrences, [KL_ARG_V2021_431, KL_ARG_V2022_432[0]]) + tco_apply(kl_occurrences, [KL_ARG_V2021_431, KL_ARG_V2022_432[1]])) if shen_consp(KL_ARG_V2022_432) else (0 if True else shen_simple_error('condition failure'))))
shen_add_fun('occurrences', kl_occurrences)

@tail_recursion
def kl_nth(KL_ARG_V2030_433, KL_ARG_V2031_434):
    global symdic
    return (KL_ARG_V2031_434[0] if (shen_consp(KL_ARG_V2031_434) if shen_eq(1, KL_ARG_V2030_433) else False) else (tail_call(kl_nth, [(KL_ARG_V2030_433 - 1), KL_ARG_V2031_434[1]]) if shen_consp(KL_ARG_V2031_434) else (tail_call(shen_sysx45error, [symdic.symdic_kl_nth]) if True else shen_simple_error('condition failure'))))
shen_add_fun('nth', kl_nth)

@tail_recursion
def kl_integerx63(KL_ARG_V2032_435):

    class KL_Context:
        KL_LOC_Abs_436 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Abs_436', tco_apply(shen_abs, [KL_ARG_V2032_435])), tail_call(shen_integerx45testx63, [KL_CTX.KL_LOC_Abs_436, tco_apply(shen_magless, [KL_CTX.KL_LOC_Abs_436, 1])])][(-1)] if isinstance(KL_ARG_V2032_435, numbers.Number) else False)
shen_add_fun('integer?', kl_integerx63)

@tail_recursion
def shen_abs(KL_ARG_V2033_437):
    global symdic
    return (KL_ARG_V2033_437 if (KL_ARG_V2033_437 > 0) else (0 - KL_ARG_V2033_437))
shen_add_fun('shen.abs', shen_abs)

@tail_recursion
def shen_magless(KL_ARG_V2034_438, KL_ARG_V2035_439):

    class KL_Context:
        KL_LOC_Nx2_440 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Nx2_440', (KL_ARG_V2035_439 * 2)), (KL_ARG_V2035_439 if (KL_CTX.KL_LOC_Nx2_440 > KL_ARG_V2034_438) else tail_call(shen_magless, [KL_ARG_V2034_438, KL_CTX.KL_LOC_Nx2_440]))][(-1)]
shen_add_fun('shen.magless', shen_magless)

@tail_recursion
def shen_integerx45testx63(KL_ARG_V2039_441, KL_ARG_V2040_442):

    class KL_Context:
        KL_LOC_Absx45N_443 = None
    KL_CTX = KL_Context()
    global symdic
    return (True if shen_eq(0, KL_ARG_V2039_441) else (False if (1 > KL_ARG_V2039_441) else ([setattr(KL_CTX, 'KL_LOC_Absx45N_443', (KL_ARG_V2039_441 - KL_ARG_V2040_442)), (tail_call(kl_integerx63, [KL_ARG_V2039_441]) if (0 > KL_CTX.KL_LOC_Absx45N_443) else tail_call(shen_integerx45testx63, [KL_CTX.KL_LOC_Absx45N_443, KL_ARG_V2040_442]))][(-1)] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.integer-test?', shen_integerx45testx63)

@tail_recursion
def kl_mapcan(KL_ARG_V2043_444, KL_ARG_V2044_445):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2044_445) else (tail_call(kl_append, [shen_apply(KL_ARG_V2043_444, [KL_ARG_V2044_445[0]]), tco_apply(kl_mapcan, [KL_ARG_V2043_444, KL_ARG_V2044_445[1]])]) if shen_consp(KL_ARG_V2044_445) else (tail_call(shen_sysx45error, [symdic.symdic_kl_mapcan]) if True else shen_simple_error('condition failure'))))
shen_add_fun('mapcan', kl_mapcan)

@tail_recursion
def kl_readx45filex45asx45bytelist(KL_ARG_V2045_446):

    class KL_Context:
        KL_LOC_Stream_447 = None
        KL_LOC_Byte_448 = None
        KL_LOC_Bytes_449 = None
        KL_LOC_Close_450 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_447', shen_open(symdic.symdic_kl_file, KL_ARG_V2045_446, symdic.symdic_kl_in)), [setattr(KL_CTX, 'KL_LOC_Byte_448', shen_read_byte(KL_CTX.KL_LOC_Stream_447)), [setattr(KL_CTX, 'KL_LOC_Bytes_449', tco_apply(shen_readx45filex45asx45bytelistx45help, [KL_CTX.KL_LOC_Stream_447, KL_CTX.KL_LOC_Byte_448, []])), [setattr(KL_CTX, 'KL_LOC_Close_450', shen_close(KL_CTX.KL_LOC_Stream_447)), tail_call(kl_reverse, [KL_CTX.KL_LOC_Bytes_449])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('read-file-as-bytelist', kl_readx45filex45asx45bytelist)

@tail_recursion
def shen_readx45filex45asx45bytelistx45help(KL_ARG_V2046_451, KL_ARG_V2047_452, KL_ARG_V2048_453):
    global symdic
    return (KL_ARG_V2048_453 if shen_eq((-1), KL_ARG_V2047_452) else (tail_call(shen_readx45filex45asx45bytelistx45help, [KL_ARG_V2046_451, shen_read_byte(KL_ARG_V2046_451), [KL_ARG_V2047_452, KL_ARG_V2048_453]]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-file-as-bytelist-help', shen_readx45filex45asx45bytelistx45help)

@tail_recursion
def kl_readx45filex45asx45string(KL_ARG_V2049_454):

    class KL_Context:
        KL_LOC_Stream_455 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_455', shen_open(symdic.symdic_kl_file, KL_ARG_V2049_454, symdic.symdic_kl_in)), tail_call(shen_rfasx45h, [KL_CTX.KL_LOC_Stream_455, shen_read_byte(KL_CTX.KL_LOC_Stream_455), ''])][(-1)]
shen_add_fun('read-file-as-string', kl_readx45filex45asx45string)

@tail_recursion
def shen_rfasx45h(KL_ARG_V2050_456, KL_ARG_V2051_457, KL_ARG_V2052_458):
    global symdic
    return ([shen_close(KL_ARG_V2050_456), KL_ARG_V2052_458][(-1)] if shen_eq((-1), KL_ARG_V2051_457) else (tail_call(shen_rfasx45h, [KL_ARG_V2050_456, shen_read_byte(KL_ARG_V2050_456), (KL_ARG_V2052_458 + chr(KL_ARG_V2051_457))]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rfas-h', shen_rfasx45h)

@tail_recursion
def kl_x61x61(KL_ARG_V2061_459, KL_ARG_V2062_460):
    global symdic
    return (True if shen_eq(KL_ARG_V2062_460, KL_ARG_V2061_459) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('==', kl_x61x61)

@tail_recursion
def kl_abort():
    global symdic
    return shen_simple_error('')
shen_add_fun('abort', kl_abort)

@tail_recursion
def kl_read():
    global symdic
    return tco_apply(kl_lineread, [])[0]
shen_add_fun('read', kl_read)

@tail_recursion
def kl_input():
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_read, [])])
shen_add_fun('input', kl_input)

@tail_recursion
def kl_inputx43(KL_ARG_V2068_461, KL_ARG_V2069_462):

    class KL_Context:
        KL_LOC_Input_463 = None
        KL_LOC_Check_464 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Input_463', tco_apply(kl_read, [])), [setattr(KL_CTX, 'KL_LOC_Check_464', tco_apply(shen_typecheck, [KL_CTX.KL_LOC_Input_463, KL_ARG_V2069_462])), ([tco_apply(shen_prhush, [('input is not of type ' + tco_apply(shen_app, [KL_ARG_V2069_462, ': please re-enter ', symdic.symdic_shen_r])), tco_apply(kl_stoutput, [])]), tail_call(kl_inputx43, [symdic.symdic_kl_x58, KL_ARG_V2069_462])][(-1)] if shen_eq(False, KL_CTX.KL_LOC_Check_464) else tail_call(kl_eval, [KL_CTX.KL_LOC_Input_463]))][(-1)]][(-1)]
shen_add_fun('input+', kl_inputx43)

@tail_recursion
def readx43(KL_ARG_V2074_465, KL_ARG_V2075_466):

    class KL_Context:
        KL_LOC_Input_467 = None
        KL_LOC_Check_468 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Input_467', tco_apply(kl_read, [])), [setattr(KL_CTX, 'KL_LOC_Check_468', tco_apply(shen_typecheck, [tco_apply(shen_rcons_form, [KL_CTX.KL_LOC_Input_467]), KL_ARG_V2075_466])), ([tco_apply(shen_prhush, [('input is not of type ' + tco_apply(shen_app, [KL_ARG_V2075_466, ': please re-enter ', symdic.symdic_shen_r])), tco_apply(kl_stoutput, [])]), tail_call(readx43, [symdic.symdic_kl_x58, KL_ARG_V2075_466])][(-1)] if shen_eq(False, KL_CTX.KL_LOC_Check_468) else KL_CTX.KL_LOC_Input_467)][(-1)]][(-1)]
shen_add_fun('read+', readx43)

@tail_recursion
def kl_boundx63(KL_ARG_V2076_469):

    class KL_Context:
        KL_LOC_Val_470 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Val_470', shen_try_except((lambda : shen_get(KL_ARG_V2076_469)), (lambda KL_ARG_E_471: symdic.symdic_shen_thisx45symbolx45isx45unbound))), (False if shen_eq(KL_CTX.KL_LOC_Val_470, symdic.symdic_shen_thisx45symbolx45isx45unbound) else True)][(-1)] if tco_apply(kl_symbolx63, [KL_ARG_V2076_469]) else False)
shen_add_fun('bound?', kl_boundx63)

@tail_recursion
def shen_stringx45x62bytes(KL_ARG_V2077_472):
    global symdic
    return ([] if shen_eq('', KL_ARG_V2077_472) else ([ord(KL_ARG_V2077_472[0]), tco_apply(shen_stringx45x62bytes, [KL_ARG_V2077_472[1:]])] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.string->bytes', shen_stringx45x62bytes)

@tail_recursion
def kl_maxinferences(KL_ARG_V2078_473):
    global symdic
    return shen_set(symdic.symdic_shen_x42maxinferencesx42, KL_ARG_V2078_473)
shen_add_fun('maxinferences', kl_maxinferences)

@tail_recursion
def kl_inferences():
    global symdic
    return shen_get(symdic.symdic_shen_x42infsx42)
shen_add_fun('inferences', kl_inferences)

@tail_recursion
def kl_protect(KL_ARG_V2079_474):
    global symdic
    return KL_ARG_V2079_474
shen_add_fun('protect', kl_protect)

@tail_recursion
def kl_stoutput():
    global symdic
    return shen_get(symdic.symdic_x42stoutputx42)
shen_add_fun('stoutput', kl_stoutput)

@tail_recursion
def kl_stringx45x62symbol(KL_ARG_V2080_475):

    class KL_Context:
        KL_LOC_Symbol_476 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Symbol_476', shen_intern(KL_ARG_V2080_475)), (KL_CTX.KL_LOC_Symbol_476 if tco_apply(kl_symbolx63, [KL_CTX.KL_LOC_Symbol_476]) else shen_simple_error(('cannot intern ' + tco_apply(shen_app, [KL_ARG_V2080_475, ' to a symbol', symdic.symdic_shen_s]))))][(-1)]
shen_add_fun('string->symbol', kl_stringx45x62symbol)

@tail_recursion
def shen_optimise(KL_ARG_V2085_477):
    global symdic
    return (shen_set(symdic.symdic_shen_x42optimisex42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2085_477) else (shen_set(symdic.symdic_shen_x42optimisex42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2085_477) else (shen_simple_error('optimise expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.optimise', shen_optimise)


#============================== sequent.kl==============================



@tail_recursion
def shen_datatypex45error(KL_ARG_V1632_478):
    global symdic
    return (shen_simple_error(('datatype syntax error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V1632_478[0]]), '\r\n', symdic.symdic_shen_a]))) if ((shen_eq([], KL_ARG_V1632_478[1][1]) if shen_consp(KL_ARG_V1632_478[1]) else False) if shen_consp(KL_ARG_V1632_478) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_datatypex45error]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-error', shen_datatypex45error)

@tail_recursion
def shen_x60datatypex45rulesx62(KL_ARG_V1637_479):

    class KL_Context:
        KL_LOC_Result_480 = None
        KL_LOC_Parse_shen_x60datatypex45rulex62_481 = None
        KL_LOC_Parse_shen_x60datatypex45rulesx62_482 = None
        KL_LOC_Result_483 = None
        KL_LOC_Parse_x60ex62_484 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_480', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulex62_481', tco_apply(shen_x60datatypex45rulex62, [KL_ARG_V1637_479])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60datatypex45rulesx62_482', tco_apply(shen_x60datatypex45rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_481])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_482[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_481]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_482])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulesx62_482)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60datatypex45rulex62_481)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_483', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_484', tco_apply(kl_x60ex62, [KL_ARG_V1637_479])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_484[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_484)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_483, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_483)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_480, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_480)][(-1)]
shen_add_fun('shen.<datatype-rules>', shen_x60datatypex45rulesx62)

@tail_recursion
def shen_x60datatypex45rulex62(KL_ARG_V1642_485):

    class KL_Context:
        KL_LOC_Result_486 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_487 = None
        KL_LOC_Parse_shen_x60premisesx62_488 = None
        KL_LOC_Parse_shen_x60singleunderlinex62_489 = None
        KL_LOC_Parse_shen_x60conclusionx62_490 = None
        KL_LOC_Result_491 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_492 = None
        KL_LOC_Parse_shen_x60premisesx62_493 = None
        KL_LOC_Parse_shen_x60doubleunderlinex62_494 = None
        KL_LOC_Parse_shen_x60conclusionx62_495 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_486', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_487', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1642_485])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_488', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_487])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60singleunderlinex62_489', tco_apply(shen_x60singleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_488])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_490', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_489])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_490[0], tco_apply(shen_sequent, [symdic.symdic_shen_single, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_487]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_488]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_490]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_490)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60singleunderlinex62_489)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_488)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_487)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_491', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_492', tco_apply(shen_x60sidex45conditionsx62, [KL_ARG_V1642_485])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_493', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_492])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60doubleunderlinex62_494', tco_apply(shen_x60doubleunderlinex62, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_493])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60conclusionx62_495', tco_apply(shen_x60conclusionx62, [KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_494])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_495[0], tco_apply(shen_sequent, [symdic.symdic_shen_double, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_492]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_493]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_495]), []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60conclusionx62_495)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60doubleunderlinex62_494)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_493)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_492)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_491, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_491)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_486, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_486)][(-1)]
shen_add_fun('shen.<datatype-rule>', shen_x60datatypex45rulex62)

@tail_recursion
def shen_x60sidex45conditionsx62(KL_ARG_V1647_496):

    class KL_Context:
        KL_LOC_Result_497 = None
        KL_LOC_Parse_shen_x60sidex45conditionx62_498 = None
        KL_LOC_Parse_shen_x60sidex45conditionsx62_499 = None
        KL_LOC_Result_500 = None
        KL_LOC_Parse_x60ex62_501 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_497', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionx62_498', tco_apply(shen_x60sidex45conditionx62, [KL_ARG_V1647_496])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60sidex45conditionsx62_499', tco_apply(shen_x60sidex45conditionsx62, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_498])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_499[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_498]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_499])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionsx62_499)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60sidex45conditionx62_498)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_500', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_501', tco_apply(kl_x60ex62, [KL_ARG_V1647_496])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_501[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_501)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_500, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_500)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_497, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_497)][(-1)]
shen_add_fun('shen.<side-conditions>', shen_x60sidex45conditionsx62)

@tail_recursion
def shen_x60sidex45conditionx62(KL_ARG_V1652_502):

    class KL_Context:
        KL_LOC_Result_503 = None
        KL_LOC_Parse_shen_x60exprx62_504 = None
        KL_LOC_Result_505 = None
        KL_LOC_Parse_shen_x60variablex63x62_506 = None
        KL_LOC_Parse_shen_x60exprx62_507 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_503', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_504', tco_apply(shen_x60exprx62, [tco_apply(shen_pair, [KL_ARG_V1652_502[0][1], tco_apply(shen_hdtl, [KL_ARG_V1652_502])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_504[0], [symdic.symdic_kl_if, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_504]), []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_504)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_if, KL_ARG_V1652_502[0][0]) if shen_consp(KL_ARG_V1652_502[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_505', ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60variablex63x62_506', tco_apply(shen_x60variablex63x62, [tco_apply(shen_pair, [KL_ARG_V1652_502[0][1], tco_apply(shen_hdtl, [KL_ARG_V1652_502])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_507', tco_apply(shen_x60exprx62, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_506])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_507[0], [symdic.symdic_kl_let, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_506]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_507]), []]]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_507)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60variablex63x62_506)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_let, KL_ARG_V1652_502[0][0]) if shen_consp(KL_ARG_V1652_502[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_505, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_505)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_503, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_503)][(-1)]
shen_add_fun('shen.<side-condition>', shen_x60sidex45conditionx62)

@tail_recursion
def shen_x60variablex63x62(KL_ARG_V1657_508):

    class KL_Context:
        KL_LOC_Result_509 = None
        KL_LOC_Parse_X_510 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_509', ([setattr(KL_CTX, 'KL_LOC_Parse_X_510', KL_ARG_V1657_508[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1657_508[0][1], tco_apply(shen_hdtl, [KL_ARG_V1657_508])])[0], KL_CTX.KL_LOC_Parse_X_510]) if tco_apply(kl_variablex63, [KL_CTX.KL_LOC_Parse_X_510]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1657_508[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_509, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_509)][(-1)]
shen_add_fun('shen.<variable?>', shen_x60variablex63x62)

@tail_recursion
def shen_x60exprx62(KL_ARG_V1662_511):

    class KL_Context:
        KL_LOC_Result_512 = None
        KL_LOC_Parse_X_513 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_512', ([setattr(KL_CTX, 'KL_LOC_Parse_X_513', KL_ARG_V1662_511[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1662_511[0][1], tco_apply(shen_hdtl, [KL_ARG_V1662_511])])[0], tco_apply(shen_removex45bar, [KL_CTX.KL_LOC_Parse_X_513])]) if (not (True if tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_513, [symdic.symdic_kl_x62x62, [symdic.symdic_kl_x59, []]]]) else (True if tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_513]) else tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_513])))) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1662_511[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_512, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_512)][(-1)]
shen_add_fun('shen.<expr>', shen_x60exprx62)

@tail_recursion
def shen_removex45bar(KL_ARG_V1663_514):
    global symdic
    return ([KL_ARG_V1663_514[0], KL_ARG_V1663_514[1][1][0]] if ((((shen_eq(KL_ARG_V1663_514[1][0], symdic.symdic_kl_barx33) if shen_eq([], KL_ARG_V1663_514[1][1][1]) else False) if shen_consp(KL_ARG_V1663_514[1][1]) else False) if shen_consp(KL_ARG_V1663_514[1]) else False) if shen_consp(KL_ARG_V1663_514) else False) else ([tco_apply(shen_removex45bar, [KL_ARG_V1663_514[0]]), tco_apply(shen_removex45bar, [KL_ARG_V1663_514[1]])] if shen_consp(KL_ARG_V1663_514) else (KL_ARG_V1663_514 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.remove-bar', shen_removex45bar)

@tail_recursion
def shen_x60premisesx62(KL_ARG_V1668_515):

    class KL_Context:
        KL_LOC_Result_516 = None
        KL_LOC_Parse_shen_x60premisex62_517 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_518 = None
        KL_LOC_Parse_shen_x60premisesx62_519 = None
        KL_LOC_Result_520 = None
        KL_LOC_Parse_x60ex62_521 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_516', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisex62_517', tco_apply(shen_x60premisex62, [KL_ARG_V1668_515])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_518', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_517])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60premisesx62_519', tco_apply(shen_x60premisesx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_518])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_519[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisex62_517]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60premisesx62_519])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisesx62_519)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_518)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60premisex62_517)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_520', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_521', tco_apply(kl_x60ex62, [KL_ARG_V1668_515])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_521[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_521)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_520, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_520)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_516, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_516)][(-1)]
shen_add_fun('shen.<premises>', shen_x60premisesx62)

@tail_recursion
def shen_x60semicolonx45symbolx62(KL_ARG_V1673_522):

    class KL_Context:
        KL_LOC_Result_523 = None
        KL_LOC_Parse_X_524 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_523', ([setattr(KL_CTX, 'KL_LOC_Parse_X_524', KL_ARG_V1673_522[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1673_522[0][1], tco_apply(shen_hdtl, [KL_ARG_V1673_522])])[0], symdic.symdic_shen_skip]) if shen_eq(KL_CTX.KL_LOC_Parse_X_524, symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1673_522[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_523, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_523)][(-1)]
shen_add_fun('shen.<semicolon-symbol>', shen_x60semicolonx45symbolx62)

@tail_recursion
def shen_x60premisex62(KL_ARG_V1678_525):

    class KL_Context:
        KL_LOC_Result_526 = None
        KL_LOC_Result_527 = None
        KL_LOC_Parse_shen_x60formulaex62_528 = None
        KL_LOC_Parse_shen_x60formulax62_529 = None
        KL_LOC_Result_530 = None
        KL_LOC_Parse_shen_x60formulax62_531 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_526', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1678_525[0][1], tco_apply(shen_hdtl, [KL_ARG_V1678_525])])[0], symdic.symdic_kl_x33]) if (shen_eq(symdic.symdic_kl_x33, KL_ARG_V1678_525[0][0]) if shen_consp(KL_ARG_V1678_525[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_527', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_528', tco_apply(shen_x60formulaex62, [KL_ARG_V1678_525])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_529', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_529[0], tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_529])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_529)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x62x62, KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_528)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_530', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_531', tco_apply(shen_x60formulax62, [KL_ARG_V1678_525])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_531[0], tco_apply(shen_sequent, [[], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_531])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_531)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_530, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_530)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_527, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_527)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_526, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_526)][(-1)]
shen_add_fun('shen.<premise>', shen_x60premisex62)

@tail_recursion
def shen_x60conclusionx62(KL_ARG_V1683_532):

    class KL_Context:
        KL_LOC_Result_533 = None
        KL_LOC_Parse_shen_x60formulaex62_534 = None
        KL_LOC_Parse_shen_x60formulax62_535 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_536 = None
        KL_LOC_Result_537 = None
        KL_LOC_Parse_shen_x60formulax62_538 = None
        KL_LOC_Parse_shen_x60semicolonx45symbolx62_539 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_533', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_534', tco_apply(shen_x60formulaex62, [KL_ARG_V1683_532])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_535', tco_apply(shen_x60formulax62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_536', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_535])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_536[0], tco_apply(shen_sequent, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_535])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_536)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_535)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x62x62, KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_534)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_537', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_538', tco_apply(shen_x60formulax62, [KL_ARG_V1683_532])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx45symbolx62_539', tco_apply(shen_x60semicolonx45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_538])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_539[0], tco_apply(shen_sequent, [[], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_538])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx45symbolx62_539)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_538)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_537, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_537)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_533, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_533)][(-1)]
shen_add_fun('shen.<conclusion>', shen_x60conclusionx62)

@tail_recursion
def shen_sequent(KL_ARG_V1684_540, KL_ARG_V1685_541):
    global symdic
    return tail_call(kl_x64p, [KL_ARG_V1684_540, KL_ARG_V1685_541])
shen_add_fun('shen.sequent', shen_sequent)

@tail_recursion
def shen_x60formulaex62(KL_ARG_V1690_542):

    class KL_Context:
        KL_LOC_Result_543 = None
        KL_LOC_Parse_shen_x60formulax62_544 = None
        KL_LOC_Parse_shen_x60commax45symbolx62_545 = None
        KL_LOC_Parse_shen_x60formulaex62_546 = None
        KL_LOC_Result_547 = None
        KL_LOC_Parse_shen_x60formulax62_548 = None
        KL_LOC_Result_549 = None
        KL_LOC_Parse_x60ex62_550 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_543', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_544', tco_apply(shen_x60formulax62, [KL_ARG_V1690_542])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax45symbolx62_545', tco_apply(shen_x60commax45symbolx62, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_544])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulaex62_546', tco_apply(shen_x60formulaex62, [KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_545])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_546[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_544]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulaex62_546])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulaex62_546)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commax45symbolx62_545)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_544)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_547', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60formulax62_548', tco_apply(shen_x60formulax62, [KL_ARG_V1690_542])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_548[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60formulax62_548]), []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60formulax62_548)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_549', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_550', tco_apply(kl_x60ex62, [KL_ARG_V1690_542])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_550[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_550)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_549, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_549)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_547, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_547)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_543, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_543)][(-1)]
shen_add_fun('shen.<formulae>', shen_x60formulaex62)

@tail_recursion
def shen_x60commax45symbolx62(KL_ARG_V1695_551):

    class KL_Context:
        KL_LOC_Result_552 = None
        KL_LOC_Parse_X_553 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_552', ([setattr(KL_CTX, 'KL_LOC_Parse_X_553', KL_ARG_V1695_551[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1695_551[0][1], tco_apply(shen_hdtl, [KL_ARG_V1695_551])])[0], symdic.symdic_shen_skip]) if shen_eq(KL_CTX.KL_LOC_Parse_X_553, shen_intern(',')) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1695_551[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_552, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_552)][(-1)]
shen_add_fun('shen.<comma-symbol>', shen_x60commax45symbolx62)

@tail_recursion
def shen_x60formulax62(KL_ARG_V1700_554):

    class KL_Context:
        KL_LOC_Result_555 = None
        KL_LOC_Parse_shen_x60exprx62_556 = None
        KL_LOC_Parse_shen_x60typex62_557 = None
        KL_LOC_Result_558 = None
        KL_LOC_Parse_shen_x60exprx62_559 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_555', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_556', tco_apply(shen_x60exprx62, [KL_ARG_V1700_554])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60typex62_557', tco_apply(shen_x60typex62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_556[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_556])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60typex62_557[0], [tco_apply(shen_curry, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_556])]), [symdic.symdic_kl_x58, [tco_apply(shen_demodulate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60typex62_557])]), []]]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60typex62_557)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_Parse_shen_x60exprx62_556[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60exprx62_556[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_556)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_558', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_559', tco_apply(shen_x60exprx62, [KL_ARG_V1700_554])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_559[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_559])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_559)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_558, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_558)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_555, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_555)][(-1)]
shen_add_fun('shen.<formula>', shen_x60formulax62)

@tail_recursion
def shen_x60typex62(KL_ARG_V1705_560):

    class KL_Context:
        KL_LOC_Result_561 = None
        KL_LOC_Parse_shen_x60exprx62_562 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_561', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60exprx62_562', tco_apply(shen_x60exprx62, [KL_ARG_V1705_560])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_562[0], tco_apply(shen_curryx45type, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60exprx62_562])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60exprx62_562)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_561, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_561)][(-1)]
shen_add_fun('shen.<type>', shen_x60typex62)

@tail_recursion
def shen_x60doubleunderlinex62(KL_ARG_V1710_563):

    class KL_Context:
        KL_LOC_Result_564 = None
        KL_LOC_Parse_X_565 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_564', ([setattr(KL_CTX, 'KL_LOC_Parse_X_565', KL_ARG_V1710_563[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1710_563[0][1], tco_apply(shen_hdtl, [KL_ARG_V1710_563])])[0], KL_CTX.KL_LOC_Parse_X_565]) if tco_apply(shen_doubleunderlinex63, [KL_CTX.KL_LOC_Parse_X_565]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1710_563[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_564, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_564)][(-1)]
shen_add_fun('shen.<doubleunderline>', shen_x60doubleunderlinex62)

@tail_recursion
def shen_x60singleunderlinex62(KL_ARG_V1715_566):

    class KL_Context:
        KL_LOC_Result_567 = None
        KL_LOC_Parse_X_568 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_567', ([setattr(KL_CTX, 'KL_LOC_Parse_X_568', KL_ARG_V1715_566[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1715_566[0][1], tco_apply(shen_hdtl, [KL_ARG_V1715_566])])[0], KL_CTX.KL_LOC_Parse_X_568]) if tco_apply(shen_singleunderlinex63, [KL_CTX.KL_LOC_Parse_X_568]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1715_566[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_567, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_567)][(-1)]
shen_add_fun('shen.<singleunderline>', shen_x60singleunderlinex62)

@tail_recursion
def shen_singleunderlinex63(KL_ARG_V1716_569):
    global symdic
    return (tail_call(shen_shx63, [str(KL_ARG_V1716_569)]) if tco_apply(kl_symbolx63, [KL_ARG_V1716_569]) else False)
shen_add_fun('shen.singleunderline?', shen_singleunderlinex63)

@tail_recursion
def shen_shx63(KL_ARG_V1717_570):
    global symdic
    return (True if shen_eq('_', KL_ARG_V1717_570) else ((tail_call(shen_shx63, [KL_ARG_V1717_570[1:]]) if shen_eq(KL_ARG_V1717_570[0], '_') else False) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.sh?', shen_shx63)

@tail_recursion
def shen_doubleunderlinex63(KL_ARG_V1718_571):
    global symdic
    return (tail_call(shen_dhx63, [str(KL_ARG_V1718_571)]) if tco_apply(kl_symbolx63, [KL_ARG_V1718_571]) else False)
shen_add_fun('shen.doubleunderline?', shen_doubleunderlinex63)

@tail_recursion
def shen_dhx63(KL_ARG_V1719_572):
    global symdic
    return (True if shen_eq('=', KL_ARG_V1719_572) else ((tail_call(shen_dhx63, [KL_ARG_V1719_572[1:]]) if shen_eq(KL_ARG_V1719_572[0], '=') else False) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.dh?', shen_dhx63)

@tail_recursion
def shen_processx45datatype(KL_ARG_V1720_573, KL_ARG_V1721_574):
    global symdic
    return tail_call(shen_rememberx45datatype, [tco_apply(shen_sx45prolog, [tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1720_573, KL_ARG_V1721_574])])])
shen_add_fun('shen.process-datatype', shen_processx45datatype)

@tail_recursion
def shen_rememberx45datatype(KL_ARG_V1726_575):
    global symdic
    return ([shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_adjoin, [KL_ARG_V1726_575[0], shen_get(symdic.symdic_shen_x42datatypesx42)])), [shen_set(symdic.symdic_shen_x42alldatatypesx42, tco_apply(kl_adjoin, [KL_ARG_V1726_575[0], shen_get(symdic.symdic_shen_x42alldatatypesx42)])), KL_ARG_V1726_575[0]][(-1)]][(-1)] if shen_consp(KL_ARG_V1726_575) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rememberx45datatype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remember-datatype', shen_rememberx45datatype)

@tail_recursion
def shen_rulesx45x62hornx45clauses(KL_ARG_V1729_576, KL_ARG_V1730_577):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1730_577) else ([tco_apply(shen_rulex45x62hornx45clause, [KL_ARG_V1729_576, tco_apply(kl_snd, [KL_ARG_V1730_577[0]])]), tco_apply(shen_rulesx45x62hornx45clauses, [KL_ARG_V1729_576, KL_ARG_V1730_577[1]])] if ((shen_eq(symdic.symdic_shen_single, tco_apply(kl_fst, [KL_ARG_V1730_577[0]])) if tco_apply(kl_tuplex63, [KL_ARG_V1730_577[0]]) else False) if shen_consp(KL_ARG_V1730_577) else False) else (tail_call(shen_rulesx45x62hornx45clauses, [KL_ARG_V1729_576, tco_apply(kl_append, [tco_apply(shen_doublex45x62singles, [tco_apply(kl_snd, [KL_ARG_V1730_577[0]])]), KL_ARG_V1730_577[1]])]) if ((shen_eq(symdic.symdic_shen_double, tco_apply(kl_fst, [KL_ARG_V1730_577[0]])) if tco_apply(kl_tuplex63, [KL_ARG_V1730_577[0]]) else False) if shen_consp(KL_ARG_V1730_577) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulesx45x62hornx45clauses]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.rules->horn-clauses', shen_rulesx45x62hornx45clauses)

@tail_recursion
def shen_doublex45x62singles(KL_ARG_V1731_578):
    global symdic
    return [tco_apply(shen_rightx45rule, [KL_ARG_V1731_578]), [tco_apply(shen_leftx45rule, [KL_ARG_V1731_578]), []]]
shen_add_fun('shen.double->singles', shen_doublex45x62singles)

@tail_recursion
def shen_rightx45rule(KL_ARG_V1732_579):
    global symdic
    return tail_call(kl_x64p, [symdic.symdic_shen_single, KL_ARG_V1732_579])
shen_add_fun('shen.right-rule', shen_rightx45rule)

@tail_recursion
def shen_leftx45rule(KL_ARG_V1733_580):

    class KL_Context:
        KL_LOC_Q_581 = None
        KL_LOC_NewConclusion_582 = None
        KL_LOC_NewPremises_583 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Q_581', tco_apply(kl_gensym, [symdic.symdic_Qv])), [setattr(KL_CTX, 'KL_LOC_NewConclusion_582', tco_apply(kl_x64p, [[tco_apply(kl_snd, [KL_ARG_V1733_580[1][1][0]]), []], KL_CTX.KL_LOC_Q_581])), [setattr(KL_CTX, 'KL_LOC_NewPremises_583', [tco_apply(kl_x64p, [tco_apply(kl_map, [symdic.symdic_shen_rightx45x62left, KL_ARG_V1733_580[1][0]]), KL_CTX.KL_LOC_Q_581]), []]), tail_call(kl_x64p, [symdic.symdic_shen_single, [KL_ARG_V1733_580[0], [KL_CTX.KL_LOC_NewPremises_583, [KL_CTX.KL_LOC_NewConclusion_582, []]]]])][(-1)]][(-1)]][(-1)] if (((((shen_eq([], KL_ARG_V1733_580[1][1][1]) if shen_eq([], tco_apply(kl_fst, [KL_ARG_V1733_580[1][1][0]])) else False) if tco_apply(kl_tuplex63, [KL_ARG_V1733_580[1][1][0]]) else False) if shen_consp(KL_ARG_V1733_580[1][1]) else False) if shen_consp(KL_ARG_V1733_580[1]) else False) if shen_consp(KL_ARG_V1733_580) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_leftx45rule]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.left-rule', shen_leftx45rule)

@tail_recursion
def shen_rightx45x62left(KL_ARG_V1738_584):
    global symdic
    return (tail_call(kl_snd, [KL_ARG_V1738_584]) if (shen_eq([], tco_apply(kl_fst, [KL_ARG_V1738_584])) if tco_apply(kl_tuplex63, [KL_ARG_V1738_584]) else False) else (shen_simple_error('syntax error with ==========\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.right->left', shen_rightx45x62left)

@tail_recursion
def shen_rulex45x62hornx45clause(KL_ARG_V1739_585, KL_ARG_V1740_586):
    global symdic
    return ([tco_apply(shen_rulex45x62hornx45clausex45head, [KL_ARG_V1739_585, tco_apply(kl_snd, [KL_ARG_V1740_586[1][1][0]])]), [symdic.symdic_kl_x58x45, [tco_apply(shen_rulex45x62hornx45clausex45body, [KL_ARG_V1740_586[0], KL_ARG_V1740_586[1][0], tco_apply(kl_fst, [KL_ARG_V1740_586[1][1][0]])]), []]]] if ((((shen_eq([], KL_ARG_V1740_586[1][1][1]) if tco_apply(kl_tuplex63, [KL_ARG_V1740_586[1][1][0]]) else False) if shen_consp(KL_ARG_V1740_586[1][1]) else False) if shen_consp(KL_ARG_V1740_586[1]) else False) if shen_consp(KL_ARG_V1740_586) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_rulex45x62hornx45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rule->horn-clause', shen_rulex45x62hornx45clause)

@tail_recursion
def shen_rulex45x62hornx45clausex45head(KL_ARG_V1741_587, KL_ARG_V1742_588):
    global symdic
    return [KL_ARG_V1741_587, [tco_apply(shen_modex45ify, [KL_ARG_V1742_588]), [symdic.symdic_Context_1957, []]]]
shen_add_fun('shen.rule->horn-clause-head', shen_rulex45x62hornx45clausex45head)

@tail_recursion
def shen_modex45ify(KL_ARG_V1743_589):
    global symdic
    return ([symdic.symdic_kl_mode, [[KL_ARG_V1743_589[0], [symdic.symdic_kl_x58, [[symdic.symdic_kl_mode, [KL_ARG_V1743_589[1][1][0], [symdic.symdic_kl_x43, []]]], []]]], [symdic.symdic_kl_x45, []]]] if ((((shen_eq([], KL_ARG_V1743_589[1][1][1]) if shen_consp(KL_ARG_V1743_589[1][1]) else False) if shen_eq(symdic.symdic_kl_x58, KL_ARG_V1743_589[1][0]) else False) if shen_consp(KL_ARG_V1743_589[1]) else False) if shen_consp(KL_ARG_V1743_589) else False) else (KL_ARG_V1743_589 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mode-ify', shen_modex45ify)

@tail_recursion
def shen_rulex45x62hornx45clausex45body(KL_ARG_V1744_590, KL_ARG_V1745_591, KL_ARG_V1746_592):

    class KL_Context:
        KL_LOC_Variables_593 = None
        KL_LOC_Predicates_594 = None
        KL_LOC_SearchLiterals_596 = None
        KL_LOC_SearchClauses_597 = None
        KL_LOC_SideLiterals_598 = None
        KL_LOC_PremissLiterals_599 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Variables_593', tco_apply(kl_map, [symdic.symdic_shen_extract_vars, KL_ARG_V1746_592])), [setattr(KL_CTX, 'KL_LOC_Predicates_594', tco_apply(kl_map, [(lambda KL_ARG_X_595: tail_call(kl_gensym, [symdic.symdic_shen_cl])), KL_ARG_V1746_592])), [setattr(KL_CTX, 'KL_LOC_SearchLiterals_596', tco_apply(shen_constructx45searchx45literals, [KL_CTX.KL_LOC_Predicates_594, KL_CTX.KL_LOC_Variables_593, symdic.symdic_Context_1957, symdic.symdic_Context1_1957])), [setattr(KL_CTX, 'KL_LOC_SearchClauses_597', tco_apply(shen_constructx45searchx45clauses, [KL_CTX.KL_LOC_Predicates_594, KL_ARG_V1746_592, KL_CTX.KL_LOC_Variables_593])), [setattr(KL_CTX, 'KL_LOC_SideLiterals_598', tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1744_590])), [setattr(KL_CTX, 'KL_LOC_PremissLiterals_599', tco_apply(kl_map, [(lambda KL_ARG_X_600: tail_call(shen_constructx45premissx45literal, [KL_ARG_X_600, tco_apply(kl_emptyx63, [KL_ARG_V1746_592])])), KL_ARG_V1745_591])), tail_call(kl_append, [KL_CTX.KL_LOC_SearchLiterals_596, tco_apply(kl_append, [KL_CTX.KL_LOC_SideLiterals_598, KL_CTX.KL_LOC_PremissLiterals_599])])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.rule->horn-clause-body', shen_rulex45x62hornx45clausex45body)

@tail_recursion
def shen_constructx45searchx45literals(KL_ARG_V1751_601, KL_ARG_V1752_602, KL_ARG_V1753_603, KL_ARG_V1754_604):
    global symdic
    return ([] if (shen_eq([], KL_ARG_V1752_602) if shen_eq([], KL_ARG_V1751_601) else False) else (tail_call(shen_cslx45help, [KL_ARG_V1751_601, KL_ARG_V1752_602, KL_ARG_V1753_603, KL_ARG_V1754_604]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.construct-search-literals', shen_constructx45searchx45literals)

@tail_recursion
def shen_cslx45help(KL_ARG_V1757_605, KL_ARG_V1758_606, KL_ARG_V1759_607, KL_ARG_V1760_608):
    global symdic
    return ([[symdic.symdic_kl_bind, [symdic.symdic_ContextOut_1957, [KL_ARG_V1759_607, []]]], []] if (shen_eq([], KL_ARG_V1758_606) if shen_eq([], KL_ARG_V1757_605) else False) else ([[KL_ARG_V1757_605[0], [KL_ARG_V1759_607, [KL_ARG_V1760_608, KL_ARG_V1758_606[0]]]], tco_apply(shen_cslx45help, [KL_ARG_V1757_605[1], KL_ARG_V1758_606[1], KL_ARG_V1760_608, tco_apply(kl_gensym, [symdic.symdic_Context])])] if (shen_consp(KL_ARG_V1758_606) if shen_consp(KL_ARG_V1757_605) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cslx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.csl-help', shen_cslx45help)

@tail_recursion
def shen_constructx45searchx45clauses(KL_ARG_V1761_609, KL_ARG_V1762_610, KL_ARG_V1763_611):
    global symdic
    return (symdic.symdic_shen_skip if ((shen_eq([], KL_ARG_V1763_611) if shen_eq([], KL_ARG_V1762_610) else False) if shen_eq([], KL_ARG_V1761_609) else False) else ([tco_apply(shen_constructx45searchx45clause, [KL_ARG_V1761_609[0], KL_ARG_V1762_610[0], KL_ARG_V1763_611[0]]), tail_call(shen_constructx45searchx45clauses, [KL_ARG_V1761_609[1], KL_ARG_V1762_610[1], KL_ARG_V1763_611[1]])][(-1)] if ((shen_consp(KL_ARG_V1763_611) if shen_consp(KL_ARG_V1762_610) else False) if shen_consp(KL_ARG_V1761_609) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45searchx45clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-search-clauses', shen_constructx45searchx45clauses)

@tail_recursion
def shen_constructx45searchx45clause(KL_ARG_V1764_612, KL_ARG_V1765_613, KL_ARG_V1766_614):
    global symdic
    return tail_call(shen_sx45prolog, [[tco_apply(shen_constructx45basex45searchx45clause, [KL_ARG_V1764_612, KL_ARG_V1765_613, KL_ARG_V1766_614]), [tco_apply(shen_constructx45recursivex45searchx45clause, [KL_ARG_V1764_612, KL_ARG_V1765_613, KL_ARG_V1766_614]), []]]])
shen_add_fun('shen.construct-search-clause', shen_constructx45searchx45clause)

@tail_recursion
def shen_constructx45basex45searchx45clause(KL_ARG_V1767_615, KL_ARG_V1768_616, KL_ARG_V1769_617):
    global symdic
    return [[KL_ARG_V1767_615, [[tco_apply(shen_modex45ify, [KL_ARG_V1768_616]), symdic.symdic_In_1957], [symdic.symdic_In_1957, KL_ARG_V1769_617]]], [symdic.symdic_kl_x58x45, [[], []]]]
shen_add_fun('shen.construct-base-search-clause', shen_constructx45basex45searchx45clause)

@tail_recursion
def shen_constructx45recursivex45searchx45clause(KL_ARG_V1770_618, KL_ARG_V1771_619, KL_ARG_V1772_620):
    global symdic
    return [[KL_ARG_V1770_618, [[symdic.symdic_Assumption_1957, symdic.symdic_Assumptions_1957], [[symdic.symdic_Assumption_1957, symdic.symdic_Out_1957], KL_ARG_V1772_620]]], [symdic.symdic_kl_x58x45, [[[KL_ARG_V1770_618, [symdic.symdic_Assumptions_1957, [symdic.symdic_Out_1957, KL_ARG_V1772_620]]], []], []]]]
shen_add_fun('shen.construct-recursive-search-clause', shen_constructx45recursivex45searchx45clause)

@tail_recursion
def shen_constructx45sidex45literals(KL_ARG_V1777_621):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1777_621) else ([[symdic.symdic_kl_when, KL_ARG_V1777_621[0][1]], tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1777_621[1]])] if ((((shen_eq([], KL_ARG_V1777_621[0][1][1]) if shen_consp(KL_ARG_V1777_621[0][1]) else False) if shen_eq(symdic.symdic_kl_if, KL_ARG_V1777_621[0][0]) else False) if shen_consp(KL_ARG_V1777_621[0]) else False) if shen_consp(KL_ARG_V1777_621) else False) else ([[symdic.symdic_kl_is, KL_ARG_V1777_621[0][1]], tco_apply(shen_constructx45sidex45literals, [KL_ARG_V1777_621[1]])] if (((((shen_eq([], KL_ARG_V1777_621[0][1][1][1]) if shen_consp(KL_ARG_V1777_621[0][1][1]) else False) if shen_consp(KL_ARG_V1777_621[0][1]) else False) if shen_eq(symdic.symdic_kl_let, KL_ARG_V1777_621[0][0]) else False) if shen_consp(KL_ARG_V1777_621[0]) else False) if shen_consp(KL_ARG_V1777_621) else False) else (tail_call(shen_constructx45sidex45literals, [KL_ARG_V1777_621[1]]) if shen_consp(KL_ARG_V1777_621) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45sidex45literals]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.construct-side-literals', shen_constructx45sidex45literals)

@tail_recursion
def shen_constructx45premissx45literal(KL_ARG_V1782_622, KL_ARG_V1783_623):
    global symdic
    return ([symdic.symdic_shen_tx42, [tco_apply(shen_recursive_cons_form, [tco_apply(kl_snd, [KL_ARG_V1782_622])]), [tco_apply(shen_constructx45context, [KL_ARG_V1783_623, tco_apply(kl_fst, [KL_ARG_V1782_622])]), []]]] if tco_apply(kl_tuplex63, [KL_ARG_V1782_622]) else ([symdic.symdic_kl_cut, [symdic.symdic_Throwcontrol, []]] if shen_eq(symdic.symdic_kl_x33, KL_ARG_V1782_622) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45premissx45literal]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.construct-premiss-literal', shen_constructx45premissx45literal)

@tail_recursion
def shen_constructx45context(KL_ARG_V1784_624, KL_ARG_V1785_625):
    global symdic
    return (symdic.symdic_Context_1957 if (shen_eq([], KL_ARG_V1785_625) if shen_eq(True, KL_ARG_V1784_624) else False) else (symdic.symdic_ContextOut_1957 if (shen_eq([], KL_ARG_V1785_625) if shen_eq(False, KL_ARG_V1784_624) else False) else ([symdic.symdic_kl_cons, [tco_apply(shen_recursive_cons_form, [KL_ARG_V1785_625[0]]), [tco_apply(shen_constructx45context, [KL_ARG_V1784_624, KL_ARG_V1785_625[1]]), []]]] if shen_consp(KL_ARG_V1785_625) else (tail_call(shen_sysx45error, [symdic.symdic_shen_constructx45context]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.construct-context', shen_constructx45context)

@tail_recursion
def shen_recursive_cons_form(KL_ARG_V1786_626):
    global symdic
    return ([symdic.symdic_kl_cons, [tco_apply(shen_recursive_cons_form, [KL_ARG_V1786_626[0]]), [tco_apply(shen_recursive_cons_form, [KL_ARG_V1786_626[1]]), []]]] if shen_consp(KL_ARG_V1786_626) else (KL_ARG_V1786_626 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_cons_form', shen_recursive_cons_form)

@tail_recursion
def kl_preclude(KL_ARG_V1787_627):
    global symdic
    return tail_call(shen_precludex45h, [tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1787_627])])
shen_add_fun('preclude', kl_preclude)

@tail_recursion
def shen_precludex45h(KL_ARG_V1788_628):

    class KL_Context:
        KL_LOC_FilterDatatypes_629 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_FilterDatatypes_629', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V1788_628]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]
shen_add_fun('shen.preclude-h', shen_precludex45h)

@tail_recursion
def kl_include(KL_ARG_V1789_630):
    global symdic
    return tail_call(shen_includex45h, [tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1789_630])])
shen_add_fun('include', kl_include)

@tail_recursion
def shen_includex45h(KL_ARG_V1790_631):

    class KL_Context:
        KL_LOC_ValidTypes_632 = None
        KL_LOC_NewDatatypes_633 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_ValidTypes_632', tco_apply(kl_intersection, [KL_ARG_V1790_631, shen_get(symdic.symdic_shen_x42alldatatypesx42)])), [setattr(KL_CTX, 'KL_LOC_NewDatatypes_633', shen_set(symdic.symdic_shen_x42datatypesx42, tco_apply(kl_union, [KL_CTX.KL_LOC_ValidTypes_632, shen_get(symdic.symdic_shen_x42datatypesx42)]))), shen_get(symdic.symdic_shen_x42datatypesx42)][(-1)]][(-1)]
shen_add_fun('shen.include-h', shen_includex45h)

@tail_recursion
def kl_precludex45allx45but(KL_ARG_V1791_634):
    global symdic
    return tail_call(shen_precludex45h, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1791_634])])])
shen_add_fun('preclude-all-but', kl_precludex45allx45but)

@tail_recursion
def kl_includex45allx45but(KL_ARG_V1792_635):
    global symdic
    return tail_call(shen_includex45h, [tco_apply(kl_difference, [shen_get(symdic.symdic_shen_x42alldatatypesx42), tco_apply(kl_map, [symdic.symdic_shen_internx45type, KL_ARG_V1792_635])])])
shen_add_fun('include-all-but', kl_includex45allx45but)

@tail_recursion
def shen_synonymsx45help(KL_ARG_V1797_636):
    global symdic
    return (symdic.symdic_kl_synonyms if shen_eq([], KL_ARG_V1797_636) else ([tco_apply(shen_pushnew, [[KL_ARG_V1797_636[0], tco_apply(shen_curryx45type, [KL_ARG_V1797_636[1][0]])], symdic.symdic_shen_x42synonymsx42]), tail_call(shen_synonymsx45help, [KL_ARG_V1797_636[1][1]])][(-1)] if (shen_consp(KL_ARG_V1797_636[1]) if shen_consp(KL_ARG_V1797_636) else False) else (shen_simple_error(('odd number of synonyms\r\n' + '')) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.synonyms-help', shen_synonymsx45help)

@tail_recursion
def shen_pushnew(KL_ARG_V1798_637, KL_ARG_V1799_638):
    global symdic
    return (shen_get(KL_ARG_V1799_638) if tco_apply(kl_elementx63, [KL_ARG_V1798_637, shen_get(KL_ARG_V1799_638)]) else shen_set(KL_ARG_V1799_638, [KL_ARG_V1798_637, shen_get(KL_ARG_V1799_638)]))
shen_add_fun('shen.pushnew', shen_pushnew)


#============================== yacc.kl==============================



@tail_recursion
def shen_yacc(KL_ARG_V2150_639):
    global symdic
    return (tail_call(shen_yacc, [[symdic.symdic_kl_defcc, [KL_ARG_V2150_639[1][0], KL_ARG_V2150_639[1][1][1][1][1][1][1]]]]) if ((((((((((shen_eq(symdic.symdic_kl_x125, KL_ARG_V2150_639[1][1][1][1][1][1][0]) if shen_consp(KL_ARG_V2150_639[1][1][1][1][1][1]) else False) if shen_consp(KL_ARG_V2150_639[1][1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_x61x61x62, KL_ARG_V2150_639[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V2150_639[1][1][1][1]) else False) if shen_consp(KL_ARG_V2150_639[1][1][1]) else False) if shen_eq(symdic.symdic_kl_x123, KL_ARG_V2150_639[1][1][0]) else False) if shen_consp(KL_ARG_V2150_639[1][1]) else False) if shen_consp(KL_ARG_V2150_639[1]) else False) if shen_eq(symdic.symdic_kl_defcc, KL_ARG_V2150_639[0]) else False) if shen_consp(KL_ARG_V2150_639) else False) else (tail_call(shen_yaccx45x62shen, [KL_ARG_V2150_639[1][0], KL_ARG_V2150_639[1][1]]) if ((shen_consp(KL_ARG_V2150_639[1]) if shen_eq(symdic.symdic_kl_defcc, KL_ARG_V2150_639[0]) else False) if shen_consp(KL_ARG_V2150_639) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_yacc]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.yacc', shen_yacc)

@tail_recursion
def shen_yaccx45x62shen(KL_ARG_V2151_640, KL_ARG_V2152_641):
    global symdic
    return [symdic.symdic_kl_define, [KL_ARG_V2151_640, tco_apply(shen_yacc_cases, [tco_apply(kl_map, [symdic.symdic_shen_cc_body, tco_apply(shen_split_cc_rules, [KL_ARG_V2152_641, []])])])]]
shen_add_fun('shen.yacc->shen', shen_yaccx45x62shen)

@tail_recursion
def shen_yacc_cases(KL_ARG_V2153_642):
    global symdic
    return tail_call(kl_append, [tco_apply(kl_mapcan, [(lambda KL_ARG_Case_643: [symdic.symdic_Stream, [symdic.symdic_kl_x60x45, [KL_ARG_Case_643, []]]]), KL_ARG_V2153_642]), [symdic.symdic_kl__, [symdic.symdic_kl_x45x62, [[symdic.symdic_kl_fail, []], []]]]])
shen_add_fun('shen.yacc_cases', shen_yacc_cases)

@tail_recursion
def shen_first_n(KL_ARG_V2158_644, KL_ARG_V2159_645):
    global symdic
    return ([] if shen_eq(0, KL_ARG_V2158_644) else ([] if shen_eq([], KL_ARG_V2159_645) else ([KL_ARG_V2159_645[0], tco_apply(shen_first_n, [(KL_ARG_V2158_644 - 1), KL_ARG_V2159_645[1]])] if shen_consp(KL_ARG_V2159_645) else (tail_call(shen_sysx45error, [symdic.symdic_shen_first_n]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.first_n', shen_first_n)

@tail_recursion
def shen_split_cc_rules(KL_ARG_V2160_646, KL_ARG_V2161_647):
    global symdic
    return ([] if (shen_eq([], KL_ARG_V2161_647) if shen_eq([], KL_ARG_V2160_646) else False) else ([tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2161_647]), []]), []] if shen_eq([], KL_ARG_V2160_646) else ([tco_apply(shen_split_cc_rule, [tco_apply(kl_reverse, [KL_ARG_V2161_647]), []]), tco_apply(shen_split_cc_rules, [KL_ARG_V2160_646[1], []])] if (shen_eq(symdic.symdic_kl_x59, KL_ARG_V2160_646[0]) if shen_consp(KL_ARG_V2160_646) else False) else (tail_call(shen_split_cc_rules, [KL_ARG_V2160_646[1], [KL_ARG_V2160_646[0], KL_ARG_V2161_647]]) if shen_consp(KL_ARG_V2160_646) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rules]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rules', shen_split_cc_rules)

@tail_recursion
def shen_split_cc_rule(KL_ARG_V2162_648, KL_ARG_V2163_649):
    global symdic
    return ([tco_apply(kl_reverse, [KL_ARG_V2163_649]), KL_ARG_V2162_648[1]] if (((shen_eq([], KL_ARG_V2162_648[1][1]) if shen_consp(KL_ARG_V2162_648[1]) else False) if shen_eq(symdic.symdic_kl_x58x61, KL_ARG_V2162_648[0]) else False) if shen_consp(KL_ARG_V2162_648) else False) else ([tco_apply(kl_reverse, [KL_ARG_V2163_649]), [[symdic.symdic_kl_where, [KL_ARG_V2162_648[1][1][1][0], [KL_ARG_V2162_648[1][0], []]]], []]] if ((((((shen_eq([], KL_ARG_V2162_648[1][1][1][1]) if shen_consp(KL_ARG_V2162_648[1][1][1]) else False) if shen_eq(symdic.symdic_kl_where, KL_ARG_V2162_648[1][1][0]) else False) if shen_consp(KL_ARG_V2162_648[1][1]) else False) if shen_consp(KL_ARG_V2162_648[1]) else False) if shen_eq(symdic.symdic_kl_x58x61, KL_ARG_V2162_648[0]) else False) if shen_consp(KL_ARG_V2162_648) else False) else ([tco_apply(shen_prhush, ['warning: ', tco_apply(kl_stoutput, [])]), [tco_apply(kl_map, [(lambda KL_ARG_X_650: tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_X_650, ' ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])])), tco_apply(kl_reverse, [KL_ARG_V2163_649])]), [tco_apply(shen_prhush, ['has no semantics.\r\n', tco_apply(kl_stoutput, [])]), tail_call(shen_split_cc_rule, [[symdic.symdic_kl_x58x61, [tco_apply(shen_default_semantics, [tco_apply(kl_reverse, [KL_ARG_V2163_649])]), []]], KL_ARG_V2163_649])][(-1)]][(-1)]][(-1)] if shen_eq([], KL_ARG_V2162_648) else (tail_call(shen_split_cc_rule, [KL_ARG_V2162_648[1], [KL_ARG_V2162_648[0], KL_ARG_V2163_649]]) if shen_consp(KL_ARG_V2162_648) else (tail_call(shen_sysx45error, [symdic.symdic_shen_split_cc_rule]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.split_cc_rule', shen_split_cc_rule)

@tail_recursion
def shen_default_semantics(KL_ARG_V2164_651):
    global symdic
    return ([] if shen_eq([], KL_ARG_V2164_651) else ([symdic.symdic_kl_append, [KL_ARG_V2164_651[0], [tco_apply(shen_default_semantics, [KL_ARG_V2164_651[1]]), []]]] if (tco_apply(shen_grammar_symbolx63, [KL_ARG_V2164_651[0]]) if shen_consp(KL_ARG_V2164_651) else False) else ([symdic.symdic_kl_cons, [KL_ARG_V2164_651[0], [tco_apply(shen_default_semantics, [KL_ARG_V2164_651[1]]), []]]] if shen_consp(KL_ARG_V2164_651) else (tail_call(shen_sysx45error, [symdic.symdic_shen_default_semantics]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.default_semantics', shen_default_semantics)

@tail_recursion
def shen_cc_body(KL_ARG_V2165_652):
    global symdic
    return (tail_call(shen_syntax, [KL_ARG_V2165_652[0], symdic.symdic_Stream, KL_ARG_V2165_652[1][0]]) if ((shen_eq([], KL_ARG_V2165_652[1][1]) if shen_consp(KL_ARG_V2165_652[1]) else False) if shen_consp(KL_ARG_V2165_652) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cc_body]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cc_body', shen_cc_body)

@tail_recursion
def shen_syntax(KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655):
    global symdic
    return ([symdic.symdic_kl_if, [tco_apply(shen_semantics, [KL_ARG_V2168_655[1][0]]), [[symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [KL_ARG_V2167_654, []]], [tco_apply(shen_semantics, [KL_ARG_V2168_655[1][1][0]]), []]]], [[symdic.symdic_kl_fail, []], []]]]] if (((((shen_eq([], KL_ARG_V2168_655[1][1][1]) if shen_consp(KL_ARG_V2168_655[1][1]) else False) if shen_consp(KL_ARG_V2168_655[1]) else False) if shen_eq(symdic.symdic_kl_where, KL_ARG_V2168_655[0]) else False) if shen_consp(KL_ARG_V2168_655) else False) if shen_eq([], KL_ARG_V2166_653) else False) else ([symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [KL_ARG_V2167_654, []]], [tco_apply(shen_semantics, [KL_ARG_V2168_655]), []]]] if shen_eq([], KL_ARG_V2166_653) else ((tail_call(shen_recursive_descent, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_grammar_symbolx63, [KL_ARG_V2166_653[0]]) else (tail_call(shen_variablex45match, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(kl_variablex63, [KL_ARG_V2166_653[0]]) else (tail_call(shen_check_stream, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_terminalx63, [KL_ARG_V2166_653[0]]) else (tail_call(shen_jump_stream, [KL_ARG_V2166_653, KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_jump_streamx63, [KL_ARG_V2166_653[0]]) else (tail_call(shen_list_stream, [tco_apply(shen_decons, [KL_ARG_V2166_653[0]]), KL_ARG_V2166_653[1], KL_ARG_V2167_654, KL_ARG_V2168_655]) if tco_apply(shen_list_streamx63, [KL_ARG_V2166_653[0]]) else shen_simple_error(tco_apply(shen_app, [KL_ARG_V2166_653[0], ' is not legal syntax\r\n', symdic.symdic_shen_a]))))))) if shen_consp(KL_ARG_V2166_653) else (tail_call(shen_sysx45error, [symdic.symdic_shen_syntax]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.syntax', shen_syntax)

@tail_recursion
def shen_list_streamx63(KL_ARG_V2177_656):
    global symdic
    return (True if shen_consp(KL_ARG_V2177_656) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list_stream?', shen_list_streamx63)

@tail_recursion
def shen_decons(KL_ARG_V2178_657):
    global symdic
    return ([KL_ARG_V2178_657[1][0], tco_apply(shen_decons, [KL_ARG_V2178_657[1][1][0]])] if ((((shen_eq([], KL_ARG_V2178_657[1][1][1]) if shen_consp(KL_ARG_V2178_657[1][1]) else False) if shen_consp(KL_ARG_V2178_657[1]) else False) if shen_eq(symdic.symdic_kl_cons, KL_ARG_V2178_657[0]) else False) if shen_consp(KL_ARG_V2178_657) else False) else (KL_ARG_V2178_657 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons', shen_decons)

@tail_recursion
def shen_list_stream(KL_ARG_V2179_658, KL_ARG_V2180_659, KL_ARG_V2181_660, KL_ARG_V2182_661):

    class KL_Context:
        KL_LOC_Test_662 = None
        KL_LOC_Action_663 = None
        KL_LOC_Else_664 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Test_662', [symdic.symdic_kl_and, [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2181_660, []]], []]], [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2181_660, []]], []]], []]], []]]]), [setattr(KL_CTX, 'KL_LOC_Action_663', [symdic.symdic_shen_sndx45orx45fail, [tco_apply(shen_syntax, [KL_ARG_V2179_658, [symdic.symdic_shen_pair, [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2181_660, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2181_660, []]], []]]], [symdic.symdic_shen_leavex33, [tco_apply(shen_syntax, [KL_ARG_V2180_659, [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2181_660, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2181_660, []]], []]]], KL_ARG_V2182_661]), []]]]), []]]), [setattr(KL_CTX, 'KL_LOC_Else_664', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_662, [KL_CTX.KL_LOC_Action_663, [KL_CTX.KL_LOC_Else_664, []]]]]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.list_stream', shen_list_stream)

@tail_recursion
def shen_sndx45orx45fail(KL_ARG_V2189_665):
    global symdic
    return (KL_ARG_V2189_665[1][0] if ((shen_eq([], KL_ARG_V2189_665[1][1]) if shen_consp(KL_ARG_V2189_665[1]) else False) if shen_consp(KL_ARG_V2189_665) else False) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.snd-or-fail', shen_sndx45orx45fail)

@tail_recursion
def shen_grammar_symbolx63(KL_ARG_V2190_666):

    class KL_Context:
        KL_LOC_Cs_667 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Cs_667', tco_apply(shen_stripx45pathname, [tco_apply(kl_explode, [KL_ARG_V2190_666])])), (shen_eq(tco_apply(kl_reverse, [KL_CTX.KL_LOC_Cs_667])[0], '>') if shen_eq(KL_CTX.KL_LOC_Cs_667[0], '<') else False)][(-1)] if tco_apply(kl_symbolx63, [KL_ARG_V2190_666]) else False)
shen_add_fun('shen.grammar_symbol?', shen_grammar_symbolx63)

@tail_recursion
def shen_stripx45pathname(KL_ARG_V2195_668):
    global symdic
    return (KL_ARG_V2195_668 if (not tco_apply(kl_elementx63, ['.', KL_ARG_V2195_668])) else (tail_call(shen_stripx45pathname, [KL_ARG_V2195_668[1]]) if shen_consp(KL_ARG_V2195_668) else (tail_call(shen_sysx45error, [symdic.symdic_shen_stripx45pathname]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.strip-pathname', shen_stripx45pathname)

@tail_recursion
def shen_recursive_descent(KL_ARG_V2196_669, KL_ARG_V2197_670, KL_ARG_V2198_671):

    class KL_Context:
        KL_LOC_Test_672 = None
        KL_LOC_Action_673 = None
        KL_LOC_Else_674 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_672', [KL_ARG_V2196_669[0], [KL_ARG_V2197_670, []]]), [setattr(KL_CTX, 'KL_LOC_Action_673', tco_apply(shen_syntax, [KL_ARG_V2196_669[1], tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2196_669[0]]), KL_ARG_V2198_671])), [setattr(KL_CTX, 'KL_LOC_Else_674', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_let, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2196_669[0]]), [KL_CTX.KL_LOC_Test_672, [[symdic.symdic_kl_if, [[symdic.symdic_kl_not, [[symdic.symdic_kl_x61, [[symdic.symdic_kl_fail, []], [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2196_669[0]]), []]]], []]], [KL_CTX.KL_LOC_Action_673, [KL_CTX.KL_LOC_Else_674, []]]]], []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2196_669) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursive_descent]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.recursive_descent', shen_recursive_descent)

@tail_recursion
def shen_variablex45match(KL_ARG_V2199_675, KL_ARG_V2200_676, KL_ARG_V2201_677):

    class KL_Context:
        KL_LOC_Test_678 = None
        KL_LOC_Action_679 = None
        KL_LOC_Else_680 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_678', [symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2200_676, []]], []]]), [setattr(KL_CTX, 'KL_LOC_Action_679', [symdic.symdic_kl_let, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2199_675[0]]), [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2200_676, []]], []]], [tco_apply(shen_syntax, [KL_ARG_V2199_675[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2200_676, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2200_676, []]], []]]], KL_ARG_V2201_677]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Else_680', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_678, [KL_CTX.KL_LOC_Action_679, [KL_CTX.KL_LOC_Else_680, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2199_675) else (tail_call(shen_sysx45error, [symdic.symdic_shen_variablex45match]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.variable-match', shen_variablex45match)

@tail_recursion
def shen_terminalx63(KL_ARG_V2210_681):
    global symdic
    return (False if shen_consp(KL_ARG_V2210_681) else (False if tco_apply(kl_variablex63, [KL_ARG_V2210_681]) else (True if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.terminal?', shen_terminalx63)

@tail_recursion
def shen_jump_streamx63(KL_ARG_V2215_682):
    global symdic
    return (True if shen_eq(KL_ARG_V2215_682, symdic.symdic_kl__) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream?', shen_jump_streamx63)

@tail_recursion
def shen_check_stream(KL_ARG_V2216_683, KL_ARG_V2217_684, KL_ARG_V2218_685):

    class KL_Context:
        KL_LOC_Test_686 = None
        KL_LOC_Action_687 = None
        KL_LOC_Else_688 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_686', [symdic.symdic_kl_and, [[symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2217_684, []]], []]], [[symdic.symdic_kl_x61, [KL_ARG_V2216_683[0], [[symdic.symdic_kl_hd, [[symdic.symdic_kl_hd, [KL_ARG_V2217_684, []]], []]], []]]], []]]]), [setattr(KL_CTX, 'KL_LOC_Action_687', tco_apply(shen_syntax, [KL_ARG_V2216_683[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2217_684, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2217_684, []]], []]]], KL_ARG_V2218_685])), [setattr(KL_CTX, 'KL_LOC_Else_688', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_686, [KL_CTX.KL_LOC_Action_687, [KL_CTX.KL_LOC_Else_688, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2216_683) else (tail_call(shen_sysx45error, [symdic.symdic_shen_check_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check_stream', shen_check_stream)

@tail_recursion
def shen_jump_stream(KL_ARG_V2219_689, KL_ARG_V2220_690, KL_ARG_V2221_691):

    class KL_Context:
        KL_LOC_Test_692 = None
        KL_LOC_Action_693 = None
        KL_LOC_Else_694 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Test_692', [symdic.symdic_kl_consx63, [[symdic.symdic_kl_hd, [KL_ARG_V2220_690, []]], []]]), [setattr(KL_CTX, 'KL_LOC_Action_693', tco_apply(shen_syntax, [KL_ARG_V2219_689[1], [symdic.symdic_shen_pair, [[symdic.symdic_kl_tl, [[symdic.symdic_kl_hd, [KL_ARG_V2220_690, []]], []]], [[symdic.symdic_shen_hdtl, [KL_ARG_V2220_690, []]], []]]], KL_ARG_V2221_691])), [setattr(KL_CTX, 'KL_LOC_Else_694', [symdic.symdic_kl_fail, []]), [symdic.symdic_kl_if, [KL_CTX.KL_LOC_Test_692, [KL_CTX.KL_LOC_Action_693, [KL_CTX.KL_LOC_Else_694, []]]]]][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2219_689) else (tail_call(shen_sysx45error, [symdic.symdic_shen_jump_stream]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.jump_stream', shen_jump_stream)

@tail_recursion
def shen_semantics(KL_ARG_V2222_695):
    global symdic
    return (KL_ARG_V2222_695[1][0] if (((shen_eq([], KL_ARG_V2222_695[1][1]) if shen_consp(KL_ARG_V2222_695[1]) else False) if shen_eq(symdic.symdic_shen_leavex33, KL_ARG_V2222_695[0]) else False) if shen_consp(KL_ARG_V2222_695) else False) else ([] if shen_eq([], KL_ARG_V2222_695) else ([symdic.symdic_shen_hdtl, [tco_apply(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2222_695]), []]] if tco_apply(shen_grammar_symbolx63, [KL_ARG_V2222_695]) else (tail_call(kl_concat, [symdic.symdic_Parse_, KL_ARG_V2222_695]) if tco_apply(kl_variablex63, [KL_ARG_V2222_695]) else (tail_call(kl_map, [symdic.symdic_shen_semantics, KL_ARG_V2222_695]) if shen_consp(KL_ARG_V2222_695) else (KL_ARG_V2222_695 if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.semantics', shen_semantics)

@tail_recursion
def kl_fail():
    global symdic
    return symdic.symdic_shen_failx33
shen_add_fun('fail', kl_fail)

@tail_recursion
def shen_pair(KL_ARG_V2223_696, KL_ARG_V2224_697):
    global symdic
    return [KL_ARG_V2223_696, [KL_ARG_V2224_697, []]]
shen_add_fun('shen.pair', shen_pair)

@tail_recursion
def shen_hdtl(KL_ARG_V2225_698):
    global symdic
    return KL_ARG_V2225_698[1][0]
shen_add_fun('shen.hdtl', shen_hdtl)

@tail_recursion
def x60x33x62(KL_ARG_V2232_699):
    global symdic
    return ([[], [KL_ARG_V2232_699[0], []]] if ((shen_eq([], KL_ARG_V2232_699[1][1]) if shen_consp(KL_ARG_V2232_699[1]) else False) if shen_consp(KL_ARG_V2232_699) else False) else (tail_call(kl_fail, []) if True else shen_simple_error('condition failure')))
shen_add_fun('<!>', x60x33x62)

@tail_recursion
def kl_x60ex62(KL_ARG_V2237_700):
    global symdic
    return ([KL_ARG_V2237_700[0], [[], []]] if ((shen_eq([], KL_ARG_V2237_700[1][1]) if shen_consp(KL_ARG_V2237_700[1]) else False) if shen_consp(KL_ARG_V2237_700) else False) else (tail_call(shen_sysx45error, [symdic.symdic_kl_x60ex62]) if True else shen_simple_error('condition failure')))
shen_add_fun('<e>', kl_x60ex62)


#============================== reader.kl==============================



@tail_recursion
def kl_lineread():
    global symdic
    return tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), []])
shen_add_fun('lineread', kl_lineread)

@tail_recursion
def shen_linereadx45loop(KL_ARG_V1329_701, KL_ARG_V1330_702):

    class KL_Context:
        KL_LOC_Line_703 = None
    KL_CTX = KL_Context()
    global symdic
    return (shen_simple_error('line read aborted') if shen_eq(KL_ARG_V1329_701, tco_apply(shen_hat, [])) else ([setattr(KL_CTX, 'KL_LOC_Line_703', tco_apply(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_ARG_V1330_702, (lambda KL_ARG_E_704: symdic.symdic_shen_nextline)])), (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1330_702, [KL_ARG_V1329_701, []]])]) if (True if shen_eq(KL_CTX.KL_LOC_Line_703, symdic.symdic_shen_nextline) else tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Line_703])) else KL_CTX.KL_LOC_Line_703)][(-1)] if tco_apply(kl_elementx63, [KL_ARG_V1329_701, [tco_apply(shen_newline, []), [tco_apply(shen_carriagex45return, []), []]]]) else (tail_call(shen_linereadx45loop, [shen_read_byte(tco_apply(kl_stinput, [])), tco_apply(kl_append, [KL_ARG_V1330_702, [KL_ARG_V1329_701, []]])]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lineread-loop', shen_linereadx45loop)

@tail_recursion
def kl_readx45file(KL_ARG_V1331_705):

    class KL_Context:
        KL_LOC_Bytelist_706 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Bytelist_706', tco_apply(kl_readx45filex45asx45bytelist, [KL_ARG_V1331_705])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Bytelist_706, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-file', kl_readx45file)

@tail_recursion
def shen_readx45error(KL_ARG_V1338_707):
    global symdic
    return (shen_simple_error(('read error here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_compressx4550, [50, KL_ARG_V1338_707[0]]), '\r\n', symdic.symdic_shen_a]))) if (((shen_eq([], KL_ARG_V1338_707[1][1]) if shen_consp(KL_ARG_V1338_707[1]) else False) if shen_consp(KL_ARG_V1338_707[0]) else False) if shen_consp(KL_ARG_V1338_707) else False) else (shen_simple_error('read error\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.read-error', shen_readx45error)

@tail_recursion
def shen_compressx4550(KL_ARG_V1343_708, KL_ARG_V1344_709):
    global symdic
    return ('' if shen_eq([], KL_ARG_V1344_709) else ('' if shen_eq(0, KL_ARG_V1343_708) else ((chr(KL_ARG_V1344_709[0]) + tco_apply(shen_compressx4550, [(KL_ARG_V1343_708 - 1), KL_ARG_V1344_709[1]])) if shen_consp(KL_ARG_V1344_709) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compressx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.compress-50', shen_compressx4550)

@tail_recursion
def shen_x60st_inputx62(KL_ARG_V1349_710):

    class KL_Context:
        KL_LOC_Result_711 = None
        KL_LOC_Parse_shen_x60lsbx62_712 = None
        KL_LOC_Parse_shen_x60st_input1x62_713 = None
        KL_LOC_Parse_shen_x60rsbx62_714 = None
        KL_LOC_Parse_shen_x60st_input2x62_715 = None
        KL_LOC_Result_716 = None
        KL_LOC_Parse_shen_x60lrbx62_717 = None
        KL_LOC_Parse_shen_x60st_input1x62_718 = None
        KL_LOC_Parse_shen_x60rrbx62_719 = None
        KL_LOC_Parse_shen_x60st_input2x62_720 = None
        KL_LOC_Result_721 = None
        KL_LOC_Parse_shen_x60lcurlyx62_722 = None
        KL_LOC_Parse_shen_x60st_inputx62_723 = None
        KL_LOC_Result_724 = None
        KL_LOC_Parse_shen_x60rcurlyx62_725 = None
        KL_LOC_Parse_shen_x60st_inputx62_726 = None
        KL_LOC_Result_727 = None
        KL_LOC_Parse_shen_x60barx62_728 = None
        KL_LOC_Parse_shen_x60st_inputx62_729 = None
        KL_LOC_Result_730 = None
        KL_LOC_Parse_shen_x60semicolonx62_731 = None
        KL_LOC_Parse_shen_x60st_inputx62_732 = None
        KL_LOC_Result_733 = None
        KL_LOC_Parse_shen_x60colonx62_734 = None
        KL_LOC_Parse_shen_x60equalx62_735 = None
        KL_LOC_Parse_shen_x60st_inputx62_736 = None
        KL_LOC_Result_737 = None
        KL_LOC_Parse_shen_x60colonx62_738 = None
        KL_LOC_Parse_shen_x60minusx62_739 = None
        KL_LOC_Parse_shen_x60st_inputx62_740 = None
        KL_LOC_Result_741 = None
        KL_LOC_Parse_shen_x60colonx62_742 = None
        KL_LOC_Parse_shen_x60st_inputx62_743 = None
        KL_LOC_Result_744 = None
        KL_LOC_Parse_shen_x60commax62_745 = None
        KL_LOC_Parse_shen_x60st_inputx62_746 = None
        KL_LOC_Result_747 = None
        KL_LOC_Parse_shen_x60commentx62_748 = None
        KL_LOC_Parse_shen_x60st_inputx62_749 = None
        KL_LOC_Result_750 = None
        KL_LOC_Parse_shen_x60atomx62_751 = None
        KL_LOC_Parse_shen_x60st_inputx62_752 = None
        KL_LOC_Result_753 = None
        KL_LOC_Parse_shen_x60whitespacesx62_754 = None
        KL_LOC_Parse_shen_x60st_inputx62_755 = None
        KL_LOC_Result_756 = None
        KL_LOC_Parse_x60ex62_757 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_711', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lsbx62_712', tco_apply(shen_x60lsbx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_713', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lsbx62_712])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rsbx62_714', tco_apply(shen_x60rsbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_713])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_715', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rsbx62_714])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_715[0], [tco_apply(kl_macroexpand, [tco_apply(shen_cons_form, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_713])])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_715])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_715)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rsbx62_714)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_713)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lsbx62_712)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_716', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lrbx62_717', tco_apply(shen_x60lrbx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input1x62_718', tco_apply(shen_x60st_input1x62, [KL_CTX.KL_LOC_Parse_shen_x60lrbx62_717])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rrbx62_719', tco_apply(shen_x60rrbx62, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_718])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_input2x62_720', tco_apply(shen_x60st_input2x62, [KL_CTX.KL_LOC_Parse_shen_x60rrbx62_719])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_720[0], tco_apply(shen_packagex45macro, [tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_718])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_720])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input2x62_720)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rrbx62_719)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_input1x62_718)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lrbx62_717)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_721', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60lcurlyx62_722', tco_apply(shen_x60lcurlyx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_723', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_722])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_723[0], [symdic.symdic_kl_x123, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_723])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_723)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60lcurlyx62_722)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_724', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rcurlyx62_725', tco_apply(shen_x60rcurlyx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_726', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_725])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_726[0], [symdic.symdic_kl_x125, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_726])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_726)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rcurlyx62_725)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_727', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60barx62_728', tco_apply(shen_x60barx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_729', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60barx62_728])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_729[0], [symdic.symdic_kl_barx33, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_729])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_729)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60barx62_728)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_730', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60semicolonx62_731', tco_apply(shen_x60semicolonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_732', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_731])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_732[0], [symdic.symdic_kl_x59, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_732])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_732)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60semicolonx62_731)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_733', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_734', tco_apply(shen_x60colonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60equalx62_735', tco_apply(shen_x60equalx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_734])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_736', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60equalx62_735])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_736[0], [symdic.symdic_kl_x58x61, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_736])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_736)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60equalx62_735)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_734)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_737', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_738', tco_apply(shen_x60colonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_739', tco_apply(shen_x60minusx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_738])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_740', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_739])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740[0], [symdic.symdic_kl_x58x45, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_740)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_739)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_738)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_741', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60colonx62_742', tco_apply(shen_x60colonx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_743', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60colonx62_742])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_743[0], [symdic.symdic_kl_x58, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_743])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_743)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60colonx62_742)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_744', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commax62_745', tco_apply(shen_x60commax62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_746', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commax62_745])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_746[0], [shen_intern(','), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_746])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_746)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commax62_745)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_747', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_748', tco_apply(shen_x60commentx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_749', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_748])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_749[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_749])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_749)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commentx62_748)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_750', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60atomx62_751', tco_apply(shen_x60atomx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_752', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_751])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_752[0], [tco_apply(kl_macroexpand, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60atomx62_751])]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_752])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_752)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60atomx62_751)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_753', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_754', tco_apply(shen_x60whitespacesx62, [KL_ARG_V1349_710])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_755', tco_apply(shen_x60st_inputx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_754])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_755[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_755])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_755)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_754)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_756', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_757', tco_apply(kl_x60ex62, [KL_ARG_V1349_710])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_757[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_757)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_756, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_756)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_753, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_753)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_750, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_750)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_747, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_747)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_744, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_744)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_741, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_741)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_737, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_737)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_733, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_733)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_730, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_730)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_727, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_727)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_724, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_724)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_721, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_721)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_716, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_716)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_711, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_711)][(-1)]
shen_add_fun('shen.<st_input>', shen_x60st_inputx62)

@tail_recursion
def shen_x60lsbx62(KL_ARG_V1354_758):

    class KL_Context:
        KL_LOC_Result_759 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_759', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1354_758[0][1], tco_apply(shen_hdtl, [KL_ARG_V1354_758])])[0], symdic.symdic_shen_skip]) if (shen_eq(91, KL_ARG_V1354_758[0][0]) if shen_consp(KL_ARG_V1354_758[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_759, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_759)][(-1)]
shen_add_fun('shen.<lsb>', shen_x60lsbx62)

@tail_recursion
def shen_x60rsbx62(KL_ARG_V1359_760):

    class KL_Context:
        KL_LOC_Result_761 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_761', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1359_760[0][1], tco_apply(shen_hdtl, [KL_ARG_V1359_760])])[0], symdic.symdic_shen_skip]) if (shen_eq(93, KL_ARG_V1359_760[0][0]) if shen_consp(KL_ARG_V1359_760[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_761, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_761)][(-1)]
shen_add_fun('shen.<rsb>', shen_x60rsbx62)

@tail_recursion
def shen_x60lcurlyx62(KL_ARG_V1364_762):

    class KL_Context:
        KL_LOC_Result_763 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_763', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1364_762[0][1], tco_apply(shen_hdtl, [KL_ARG_V1364_762])])[0], symdic.symdic_shen_skip]) if (shen_eq(123, KL_ARG_V1364_762[0][0]) if shen_consp(KL_ARG_V1364_762[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_763, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_763)][(-1)]
shen_add_fun('shen.<lcurly>', shen_x60lcurlyx62)

@tail_recursion
def shen_x60rcurlyx62(KL_ARG_V1369_764):

    class KL_Context:
        KL_LOC_Result_765 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_765', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1369_764[0][1], tco_apply(shen_hdtl, [KL_ARG_V1369_764])])[0], symdic.symdic_shen_skip]) if (shen_eq(125, KL_ARG_V1369_764[0][0]) if shen_consp(KL_ARG_V1369_764[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_765, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_765)][(-1)]
shen_add_fun('shen.<rcurly>', shen_x60rcurlyx62)

@tail_recursion
def shen_x60barx62(KL_ARG_V1374_766):

    class KL_Context:
        KL_LOC_Result_767 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_767', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1374_766[0][1], tco_apply(shen_hdtl, [KL_ARG_V1374_766])])[0], symdic.symdic_shen_skip]) if (shen_eq(124, KL_ARG_V1374_766[0][0]) if shen_consp(KL_ARG_V1374_766[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_767, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_767)][(-1)]
shen_add_fun('shen.<bar>', shen_x60barx62)

@tail_recursion
def shen_x60semicolonx62(KL_ARG_V1379_768):

    class KL_Context:
        KL_LOC_Result_769 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_769', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1379_768[0][1], tco_apply(shen_hdtl, [KL_ARG_V1379_768])])[0], symdic.symdic_shen_skip]) if (shen_eq(59, KL_ARG_V1379_768[0][0]) if shen_consp(KL_ARG_V1379_768[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_769, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_769)][(-1)]
shen_add_fun('shen.<semicolon>', shen_x60semicolonx62)

@tail_recursion
def shen_x60colonx62(KL_ARG_V1384_770):

    class KL_Context:
        KL_LOC_Result_771 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_771', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1384_770[0][1], tco_apply(shen_hdtl, [KL_ARG_V1384_770])])[0], symdic.symdic_shen_skip]) if (shen_eq(58, KL_ARG_V1384_770[0][0]) if shen_consp(KL_ARG_V1384_770[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_771, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_771)][(-1)]
shen_add_fun('shen.<colon>', shen_x60colonx62)

@tail_recursion
def shen_x60commax62(KL_ARG_V1389_772):

    class KL_Context:
        KL_LOC_Result_773 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_773', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1389_772[0][1], tco_apply(shen_hdtl, [KL_ARG_V1389_772])])[0], symdic.symdic_shen_skip]) if (shen_eq(44, KL_ARG_V1389_772[0][0]) if shen_consp(KL_ARG_V1389_772[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_773, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_773)][(-1)]
shen_add_fun('shen.<comma>', shen_x60commax62)

@tail_recursion
def shen_x60equalx62(KL_ARG_V1394_774):

    class KL_Context:
        KL_LOC_Result_775 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_775', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1394_774[0][1], tco_apply(shen_hdtl, [KL_ARG_V1394_774])])[0], symdic.symdic_shen_skip]) if (shen_eq(61, KL_ARG_V1394_774[0][0]) if shen_consp(KL_ARG_V1394_774[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_775, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_775)][(-1)]
shen_add_fun('shen.<equal>', shen_x60equalx62)

@tail_recursion
def shen_x60minusx62(KL_ARG_V1399_776):

    class KL_Context:
        KL_LOC_Result_777 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_777', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1399_776[0][1], tco_apply(shen_hdtl, [KL_ARG_V1399_776])])[0], symdic.symdic_shen_skip]) if (shen_eq(45, KL_ARG_V1399_776[0][0]) if shen_consp(KL_ARG_V1399_776[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_777, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_777)][(-1)]
shen_add_fun('shen.<minus>', shen_x60minusx62)

@tail_recursion
def shen_x60lrbx62(KL_ARG_V1404_778):

    class KL_Context:
        KL_LOC_Result_779 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_779', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1404_778[0][1], tco_apply(shen_hdtl, [KL_ARG_V1404_778])])[0], symdic.symdic_shen_skip]) if (shen_eq(40, KL_ARG_V1404_778[0][0]) if shen_consp(KL_ARG_V1404_778[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_779, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_779)][(-1)]
shen_add_fun('shen.<lrb>', shen_x60lrbx62)

@tail_recursion
def shen_x60rrbx62(KL_ARG_V1409_780):

    class KL_Context:
        KL_LOC_Result_781 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_781', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1409_780[0][1], tco_apply(shen_hdtl, [KL_ARG_V1409_780])])[0], symdic.symdic_shen_skip]) if (shen_eq(41, KL_ARG_V1409_780[0][0]) if shen_consp(KL_ARG_V1409_780[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_781, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_781)][(-1)]
shen_add_fun('shen.<rrb>', shen_x60rrbx62)

@tail_recursion
def shen_x60atomx62(KL_ARG_V1414_782):

    class KL_Context:
        KL_LOC_Result_783 = None
        KL_LOC_Parse_shen_x60strx62_784 = None
        KL_LOC_Result_785 = None
        KL_LOC_Parse_shen_x60numberx62_786 = None
        KL_LOC_Result_787 = None
        KL_LOC_Parse_shen_x60symx62_788 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_783', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strx62_784', tco_apply(shen_x60strx62, [KL_ARG_V1414_782])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60strx62_784[0], tco_apply(shen_controlx45chars, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strx62_784])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strx62_784)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_785', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_786', tco_apply(shen_x60numberx62, [KL_ARG_V1414_782])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_786[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_786])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_786)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_787', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60symx62_788', tco_apply(shen_x60symx62, [KL_ARG_V1414_782])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60symx62_788[0], ([symdic.symdic_kl_vector, [0, []]] if shen_eq(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_788]), '<>') else shen_intern(tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60symx62_788])))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60symx62_788)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_787, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_787)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_785, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_785)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_783, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_783)][(-1)]
shen_add_fun('shen.<atom>', shen_x60atomx62)

@tail_recursion
def shen_controlx45chars(KL_ARG_V1415_789):

    class KL_Context:
        KL_LOC_CodePoint_790 = None
        KL_LOC_AfterCodePoint_791 = None
    KL_CTX = KL_Context()
    global symdic
    return ('' if shen_eq([], KL_ARG_V1415_789) else ([setattr(KL_CTX, 'KL_LOC_CodePoint_790', tco_apply(shen_codex45point, [KL_ARG_V1415_789[1][1]])), [setattr(KL_CTX, 'KL_LOC_AfterCodePoint_791', tco_apply(shen_afterx45codepoint, [KL_ARG_V1415_789[1][1]])), tail_call(kl_x64s, [chr(tco_apply(shen_decimalise, [KL_CTX.KL_LOC_CodePoint_790])), tco_apply(shen_controlx45chars, [KL_CTX.KL_LOC_AfterCodePoint_791])])][(-1)]][(-1)] if (((shen_eq('#', KL_ARG_V1415_789[1][0]) if shen_consp(KL_ARG_V1415_789[1]) else False) if shen_eq('c', KL_ARG_V1415_789[0]) else False) if shen_consp(KL_ARG_V1415_789) else False) else (tail_call(kl_x64s, [KL_ARG_V1415_789[0], tco_apply(shen_controlx45chars, [KL_ARG_V1415_789[1]])]) if shen_consp(KL_ARG_V1415_789) else (tail_call(shen_sysx45error, [symdic.symdic_shen_controlx45chars]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.control-chars', shen_controlx45chars)

@tail_recursion
def shen_codex45point(KL_ARG_V1418_792):
    global symdic
    return ('' if (shen_eq(';', KL_ARG_V1418_792[0]) if shen_consp(KL_ARG_V1418_792) else False) else ([KL_ARG_V1418_792[0], tco_apply(shen_codex45point, [KL_ARG_V1418_792[1]])] if (tco_apply(kl_elementx63, [KL_ARG_V1418_792[0], ['0', ['1', ['2', ['3', ['4', ['5', ['6', ['7', ['8', ['9', ['0', []]]]]]]]]]]]]) if shen_consp(KL_ARG_V1418_792) else False) else (shen_simple_error(('code point parse error ' + tco_apply(shen_app, [KL_ARG_V1418_792, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.code-point', shen_codex45point)

@tail_recursion
def shen_afterx45codepoint(KL_ARG_V1423_793):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1423_793) else (KL_ARG_V1423_793[1] if (shen_eq(';', KL_ARG_V1423_793[0]) if shen_consp(KL_ARG_V1423_793) else False) else (tail_call(shen_afterx45codepoint, [KL_ARG_V1423_793[1]]) if shen_consp(KL_ARG_V1423_793) else (tail_call(shen_sysx45error, [symdic.symdic_shen_afterx45codepoint]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.after-codepoint', shen_afterx45codepoint)

@tail_recursion
def shen_decimalise(KL_ARG_V1424_794):
    global symdic
    return tail_call(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_digitsx45x62integers, [KL_ARG_V1424_794])]), 0])
shen_add_fun('shen.decimalise', shen_decimalise)

@tail_recursion
def shen_digitsx45x62integers(KL_ARG_V1429_795):
    global symdic
    return ([0, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('0', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([1, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('1', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([2, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('2', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([3, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('3', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([4, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('4', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([5, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('5', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([6, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('6', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([7, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('7', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([8, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('8', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([9, tco_apply(shen_digitsx45x62integers, [KL_ARG_V1429_795[1]])] if (shen_eq('9', KL_ARG_V1429_795[0]) if shen_consp(KL_ARG_V1429_795) else False) else ([] if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.digits->integers', shen_digitsx45x62integers)

@tail_recursion
def shen_x60symx62(KL_ARG_V1434_796):

    class KL_Context:
        KL_LOC_Result_797 = None
        KL_LOC_Parse_shen_x60alphax62_798 = None
        KL_LOC_Parse_shen_x60alphanumsx62_799 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_797', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_798', tco_apply(shen_x60alphax62, [KL_ARG_V1434_796])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_799', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_798])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_799[0], tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_798]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_799])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_799)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphax62_798)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_797, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_797)][(-1)]
shen_add_fun('shen.<sym>', shen_x60symx62)

@tail_recursion
def shen_x60alphanumsx62(KL_ARG_V1439_800):

    class KL_Context:
        KL_LOC_Result_801 = None
        KL_LOC_Parse_shen_x60alphanumx62_802 = None
        KL_LOC_Parse_shen_x60alphanumsx62_803 = None
        KL_LOC_Result_804 = None
        KL_LOC_Parse_x60ex62_805 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_801', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumx62_802', tco_apply(shen_x60alphanumx62, [KL_ARG_V1439_800])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphanumsx62_803', tco_apply(shen_x60alphanumsx62, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_802])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_803[0], tco_apply(kl_x64s, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_802]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_803])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumsx62_803)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphanumx62_802)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_804', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_805', tco_apply(kl_x60ex62, [KL_ARG_V1439_800])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_805[0], '']) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_805)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_804, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_804)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_801, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_801)][(-1)]
shen_add_fun('shen.<alphanums>', shen_x60alphanumsx62)

@tail_recursion
def shen_x60alphanumx62(KL_ARG_V1444_806):

    class KL_Context:
        KL_LOC_Result_807 = None
        KL_LOC_Parse_shen_x60alphax62_808 = None
        KL_LOC_Result_809 = None
        KL_LOC_Parse_shen_x60numx62_810 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_807', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60alphax62_808', tco_apply(shen_x60alphax62, [KL_ARG_V1444_806])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_808[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60alphax62_808])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60alphax62_808)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_809', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numx62_810', tco_apply(shen_x60numx62, [KL_ARG_V1444_806])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numx62_810[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numx62_810])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numx62_810)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_809, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_809)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_807, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_807)][(-1)]
shen_add_fun('shen.<alphanum>', shen_x60alphanumx62)

@tail_recursion
def shen_x60numx62(KL_ARG_V1449_811):

    class KL_Context:
        KL_LOC_Result_812 = None
        KL_LOC_Parse_Byte_813 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_812', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_813', KL_ARG_V1449_811[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1449_811[0][1], tco_apply(shen_hdtl, [KL_ARG_V1449_811])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_813)]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_Byte_813]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1449_811[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_812, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_812)][(-1)]
shen_add_fun('shen.<num>', shen_x60numx62)

@tail_recursion
def shen_numbytex63(KL_ARG_V1454_814):
    global symdic
    return (True if shen_eq(48, KL_ARG_V1454_814) else (True if shen_eq(49, KL_ARG_V1454_814) else (True if shen_eq(50, KL_ARG_V1454_814) else (True if shen_eq(51, KL_ARG_V1454_814) else (True if shen_eq(52, KL_ARG_V1454_814) else (True if shen_eq(53, KL_ARG_V1454_814) else (True if shen_eq(54, KL_ARG_V1454_814) else (True if shen_eq(55, KL_ARG_V1454_814) else (True if shen_eq(56, KL_ARG_V1454_814) else (True if shen_eq(57, KL_ARG_V1454_814) else (False if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.numbyte?', shen_numbytex63)

@tail_recursion
def shen_x60alphax62(KL_ARG_V1459_815):

    class KL_Context:
        KL_LOC_Result_816 = None
        KL_LOC_Parse_Byte_817 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_816', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_817', KL_ARG_V1459_815[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1459_815[0][1], tco_apply(shen_hdtl, [KL_ARG_V1459_815])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_817)]) if tco_apply(shen_symbolx45codex63, [KL_CTX.KL_LOC_Parse_Byte_817]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1459_815[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_816, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_816)][(-1)]
shen_add_fun('shen.<alpha>', shen_x60alphax62)

@tail_recursion
def shen_symbolx45codex63(KL_ARG_V1460_818):
    global symdic
    return (True if shen_eq(KL_ARG_V1460_818, 126) else (True if ((KL_ARG_V1460_818 < 123) if (KL_ARG_V1460_818 > 94) else False) else (True if ((KL_ARG_V1460_818 < 91) if (KL_ARG_V1460_818 > 59) else False) else (True if (((not shen_eq(KL_ARG_V1460_818, 44)) if (KL_ARG_V1460_818 < 58) else False) if (KL_ARG_V1460_818 > 41) else False) else (True if ((KL_ARG_V1460_818 < 40) if (KL_ARG_V1460_818 > 34) else False) else shen_eq(KL_ARG_V1460_818, 33))))))
shen_add_fun('shen.symbol-code?', shen_symbolx45codex63)

@tail_recursion
def shen_x60strx62(KL_ARG_V1465_819):

    class KL_Context:
        KL_LOC_Result_820 = None
        KL_LOC_Parse_shen_x60dbqx62_821 = None
        KL_LOC_Parse_shen_x60strcontentsx62_822 = None
        KL_LOC_Parse_shen_x60dbqx62_823 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_820', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_821', tco_apply(shen_x60dbqx62, [KL_ARG_V1465_819])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_822', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60dbqx62_821])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60dbqx62_823', tco_apply(shen_x60dbqx62, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_822])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60dbqx62_823[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_822])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60dbqx62_823)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_822)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60dbqx62_821)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_820, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_820)][(-1)]
shen_add_fun('shen.<str>', shen_x60strx62)

@tail_recursion
def shen_x60dbqx62(KL_ARG_V1470_824):

    class KL_Context:
        KL_LOC_Result_825 = None
        KL_LOC_Parse_Byte_826 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_825', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_826', KL_ARG_V1470_824[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1470_824[0][1], tco_apply(shen_hdtl, [KL_ARG_V1470_824])])[0], KL_CTX.KL_LOC_Parse_Byte_826]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_826, 34) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1470_824[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_825, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_825)][(-1)]
shen_add_fun('shen.<dbq>', shen_x60dbqx62)

@tail_recursion
def shen_x60strcontentsx62(KL_ARG_V1475_827):

    class KL_Context:
        KL_LOC_Result_828 = None
        KL_LOC_Parse_shen_x60strcx62_829 = None
        KL_LOC_Parse_shen_x60strcontentsx62_830 = None
        KL_LOC_Result_831 = None
        KL_LOC_Parse_x60ex62_832 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_828', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcx62_829', tco_apply(shen_x60strcx62, [KL_ARG_V1475_827])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60strcontentsx62_830', tco_apply(shen_x60strcontentsx62, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_829])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcx62_829]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcontentsx62_830)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60strcx62_829)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_831', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_832', tco_apply(kl_x60ex62, [KL_ARG_V1475_827])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_832[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_832)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_831, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_831)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_828, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_828)][(-1)]
shen_add_fun('shen.<strcontents>', shen_x60strcontentsx62)

@tail_recursion
def shen_x60bytex62(KL_ARG_V1480_833):

    class KL_Context:
        KL_LOC_Result_834 = None
        KL_LOC_Parse_Byte_835 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_834', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_835', KL_ARG_V1480_833[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1480_833[0][1], tco_apply(shen_hdtl, [KL_ARG_V1480_833])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_835)])][(-1)] if shen_consp(KL_ARG_V1480_833[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_834, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_834)][(-1)]
shen_add_fun('shen.<byte>', shen_x60bytex62)

@tail_recursion
def shen_x60strcx62(KL_ARG_V1485_836):

    class KL_Context:
        KL_LOC_Result_837 = None
        KL_LOC_Parse_Byte_838 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_837', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_838', KL_ARG_V1485_836[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1485_836[0][1], tco_apply(shen_hdtl, [KL_ARG_V1485_836])])[0], chr(KL_CTX.KL_LOC_Parse_Byte_838)]) if (not shen_eq(KL_CTX.KL_LOC_Parse_Byte_838, 34)) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1485_836[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_837, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_837)][(-1)]
shen_add_fun('shen.<strc>', shen_x60strcx62)

@tail_recursion
def shen_x60numberx62(KL_ARG_V1490_839):

    class KL_Context:
        KL_LOC_Result_840 = None
        KL_LOC_Parse_shen_x60minusx62_841 = None
        KL_LOC_Parse_shen_x60numberx62_842 = None
        KL_LOC_Result_843 = None
        KL_LOC_Parse_shen_x60plusx62_844 = None
        KL_LOC_Parse_shen_x60numberx62_845 = None
        KL_LOC_Result_846 = None
        KL_LOC_Parse_shen_x60predigitsx62_847 = None
        KL_LOC_Parse_shen_x60stopx62_848 = None
        KL_LOC_Parse_shen_x60postdigitsx62_849 = None
        KL_LOC_Parse_shen_x60Ex62_850 = None
        KL_LOC_Parse_shen_x60log10x62_851 = None
        KL_LOC_Result_852 = None
        KL_LOC_Parse_shen_x60digitsx62_853 = None
        KL_LOC_Parse_shen_x60Ex62_854 = None
        KL_LOC_Parse_shen_x60log10x62_855 = None
        KL_LOC_Result_856 = None
        KL_LOC_Parse_shen_x60predigitsx62_857 = None
        KL_LOC_Parse_shen_x60stopx62_858 = None
        KL_LOC_Parse_shen_x60postdigitsx62_859 = None
        KL_LOC_Result_860 = None
        KL_LOC_Parse_shen_x60digitsx62_861 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_840', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_841', tco_apply(shen_x60minusx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_842', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_841])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_842[0], (0 - tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_842]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_842)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_841)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_843', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60plusx62_844', tco_apply(shen_x60plusx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60numberx62_845', tco_apply(shen_x60numberx62, [KL_CTX.KL_LOC_Parse_shen_x60plusx62_844])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_845[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60numberx62_845])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60numberx62_845)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60plusx62_844)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_846', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_847', tco_apply(shen_x60predigitsx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_848', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_847])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_849', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_848])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_850', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_849])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_851', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_850])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_851[0], (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_851])]) * (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_847])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_849]), 1])))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60log10x62_851)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60Ex62_850)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_849)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60stopx62_848)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_847)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_852', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_853', tco_apply(shen_x60digitsx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60Ex62_854', tco_apply(shen_x60Ex62, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_853])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60log10x62_855', tco_apply(shen_x60log10x62, [KL_CTX.KL_LOC_Parse_shen_x60Ex62_854])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_855[0], (tco_apply(shen_expt, [10, tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60log10x62_855])]) * tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_853])]), 0]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60log10x62_855)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60Ex62_854)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_853)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_856', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predigitsx62_857', tco_apply(shen_x60predigitsx62, [KL_ARG_V1490_839])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60stopx62_858', tco_apply(shen_x60stopx62, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_857])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60postdigitsx62_859', tco_apply(shen_x60postdigitsx62, [KL_CTX.KL_LOC_Parse_shen_x60stopx62_858])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_859[0], (tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_857])]), 0]) + tco_apply(shen_post, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_859]), 1]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60postdigitsx62_859)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60stopx62_858)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predigitsx62_857)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_860', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_861', tco_apply(shen_x60digitsx62, [KL_ARG_V1490_839])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861[0], tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861])]), 0])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_861)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_860, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_860)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_856, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_856)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_852, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_852)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_846, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_846)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_843, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_843)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_840, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_840)][(-1)]
shen_add_fun('shen.<number>', shen_x60numberx62)

@tail_recursion
def shen_x60Ex62(KL_ARG_V1495_862):

    class KL_Context:
        KL_LOC_Result_863 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_863', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1495_862[0][1], tco_apply(shen_hdtl, [KL_ARG_V1495_862])])[0], symdic.symdic_shen_skip]) if (shen_eq(101, KL_ARG_V1495_862[0][0]) if shen_consp(KL_ARG_V1495_862[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_863, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_863)][(-1)]
shen_add_fun('shen.<E>', shen_x60Ex62)

@tail_recursion
def shen_x60log10x62(KL_ARG_V1500_864):

    class KL_Context:
        KL_LOC_Result_865 = None
        KL_LOC_Parse_shen_x60minusx62_866 = None
        KL_LOC_Parse_shen_x60digitsx62_867 = None
        KL_LOC_Result_868 = None
        KL_LOC_Parse_shen_x60digitsx62_869 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_865', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60minusx62_866', tco_apply(shen_x60minusx62, [KL_ARG_V1500_864])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_867', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60minusx62_866])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_867[0], (0 - tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_867])]), 0]))]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_867)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60minusx62_866)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_868', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_869', tco_apply(shen_x60digitsx62, [KL_ARG_V1500_864])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869[0], tco_apply(shen_pre, [tco_apply(kl_reverse, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869])]), 0])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_869)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_868, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_868)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_865, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_865)][(-1)]
shen_add_fun('shen.<log10>', shen_x60log10x62)

@tail_recursion
def shen_x60plusx62(KL_ARG_V1505_870):

    class KL_Context:
        KL_LOC_Result_871 = None
        KL_LOC_Parse_Byte_872 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_871', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_872', KL_ARG_V1505_870[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1505_870[0][1], tco_apply(shen_hdtl, [KL_ARG_V1505_870])])[0], KL_CTX.KL_LOC_Parse_Byte_872]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_872, 43) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1505_870[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_871, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_871)][(-1)]
shen_add_fun('shen.<plus>', shen_x60plusx62)

@tail_recursion
def shen_x60stopx62(KL_ARG_V1510_873):

    class KL_Context:
        KL_LOC_Result_874 = None
        KL_LOC_Parse_Byte_875 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_874', ([setattr(KL_CTX, 'KL_LOC_Parse_Byte_875', KL_ARG_V1510_873[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1510_873[0][1], tco_apply(shen_hdtl, [KL_ARG_V1510_873])])[0], KL_CTX.KL_LOC_Parse_Byte_875]) if shen_eq(KL_CTX.KL_LOC_Parse_Byte_875, 46) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1510_873[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_874, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_874)][(-1)]
shen_add_fun('shen.<stop>', shen_x60stopx62)

@tail_recursion
def shen_x60predigitsx62(KL_ARG_V1515_876):

    class KL_Context:
        KL_LOC_Result_877 = None
        KL_LOC_Parse_shen_x60digitsx62_878 = None
        KL_LOC_Result_879 = None
        KL_LOC_Parse_x60ex62_880 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_877', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_878', tco_apply(shen_x60digitsx62, [KL_ARG_V1515_876])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_878[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_878])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_878)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_879', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_880', tco_apply(kl_x60ex62, [KL_ARG_V1515_876])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_880[0], []]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_880)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_879, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_879)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_877, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_877)][(-1)]
shen_add_fun('shen.<predigits>', shen_x60predigitsx62)

@tail_recursion
def shen_x60postdigitsx62(KL_ARG_V1520_881):

    class KL_Context:
        KL_LOC_Result_882 = None
        KL_LOC_Parse_shen_x60digitsx62_883 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_882', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_883', tco_apply(shen_x60digitsx62, [KL_ARG_V1520_881])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_883[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_883])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_883)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_882, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_882)][(-1)]
shen_add_fun('shen.<postdigits>', shen_x60postdigitsx62)

@tail_recursion
def shen_x60digitsx62(KL_ARG_V1525_884):

    class KL_Context:
        KL_LOC_Result_885 = None
        KL_LOC_Parse_shen_x60digitx62_886 = None
        KL_LOC_Parse_shen_x60digitsx62_887 = None
        KL_LOC_Result_888 = None
        KL_LOC_Parse_shen_x60digitx62_889 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_885', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_886', tco_apply(shen_x60digitx62, [KL_ARG_V1525_884])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitsx62_887', tco_apply(shen_x60digitsx62, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_886])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_887[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_886]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitsx62_887])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitsx62_887)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitx62_886)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_888', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60digitx62_889', tco_apply(shen_x60digitx62, [KL_ARG_V1525_884])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_889[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60digitx62_889]), []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60digitx62_889)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_888, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_888)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_885, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_885)][(-1)]
shen_add_fun('shen.<digits>', shen_x60digitsx62)

@tail_recursion
def shen_x60digitx62(KL_ARG_V1530_890):

    class KL_Context:
        KL_LOC_Result_891 = None
        KL_LOC_Parse_X_892 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_891', ([setattr(KL_CTX, 'KL_LOC_Parse_X_892', KL_ARG_V1530_890[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1530_890[0][1], tco_apply(shen_hdtl, [KL_ARG_V1530_890])])[0], tco_apply(shen_bytex45x62digit, [KL_CTX.KL_LOC_Parse_X_892])]) if tco_apply(shen_numbytex63, [KL_CTX.KL_LOC_Parse_X_892]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1530_890[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_891, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_891)][(-1)]
shen_add_fun('shen.<digit>', shen_x60digitx62)

@tail_recursion
def shen_bytex45x62digit(KL_ARG_V1531_893):
    global symdic
    return (0 if shen_eq(48, KL_ARG_V1531_893) else (1 if shen_eq(49, KL_ARG_V1531_893) else (2 if shen_eq(50, KL_ARG_V1531_893) else (3 if shen_eq(51, KL_ARG_V1531_893) else (4 if shen_eq(52, KL_ARG_V1531_893) else (5 if shen_eq(53, KL_ARG_V1531_893) else (6 if shen_eq(54, KL_ARG_V1531_893) else (7 if shen_eq(55, KL_ARG_V1531_893) else (8 if shen_eq(56, KL_ARG_V1531_893) else (9 if shen_eq(57, KL_ARG_V1531_893) else (tail_call(shen_sysx45error, [symdic.symdic_shen_bytex45x62digit]) if True else shen_simple_error('condition failure'))))))))))))
shen_add_fun('shen.byte->digit', shen_bytex45x62digit)

@tail_recursion
def shen_pre(KL_ARG_V1534_894, KL_ARG_V1535_895):
    global symdic
    return (0 if shen_eq([], KL_ARG_V1534_894) else (((tco_apply(shen_expt, [10, KL_ARG_V1535_895]) * KL_ARG_V1534_894[0]) + tco_apply(shen_pre, [KL_ARG_V1534_894[1], (KL_ARG_V1535_895 + 1)])) if shen_consp(KL_ARG_V1534_894) else (tail_call(shen_sysx45error, [symdic.symdic_shen_pre]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.pre', shen_pre)

@tail_recursion
def shen_post(KL_ARG_V1538_896, KL_ARG_V1539_897):
    global symdic
    return (0 if shen_eq([], KL_ARG_V1538_896) else (((tco_apply(shen_expt, [10, (0 - KL_ARG_V1539_897)]) * KL_ARG_V1538_896[0]) + tco_apply(shen_post, [KL_ARG_V1538_896[1], (KL_ARG_V1539_897 + 1)])) if shen_consp(KL_ARG_V1538_896) else (tail_call(shen_sysx45error, [symdic.symdic_shen_post]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.post', shen_post)

@tail_recursion
def shen_expt(KL_ARG_V1542_898, KL_ARG_V1543_899):
    global symdic
    return (1 if shen_eq(0, KL_ARG_V1543_899) else ((KL_ARG_V1542_898 * tco_apply(shen_expt, [KL_ARG_V1542_898, (KL_ARG_V1543_899 - 1)])) if (KL_ARG_V1543_899 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1542_898, (KL_ARG_V1543_899 + 1)]) / KL_ARG_V1542_898)) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.expt', shen_expt)

@tail_recursion
def shen_x60st_input1x62(KL_ARG_V1548_900):

    class KL_Context:
        KL_LOC_Result_901 = None
        KL_LOC_Parse_shen_x60st_inputx62_902 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_901', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_902', tco_apply(shen_x60st_inputx62, [KL_ARG_V1548_900])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_902[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_902])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_902)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_901, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_901)][(-1)]
shen_add_fun('shen.<st_input1>', shen_x60st_input1x62)

@tail_recursion
def shen_x60st_input2x62(KL_ARG_V1553_903):

    class KL_Context:
        KL_LOC_Result_904 = None
        KL_LOC_Parse_shen_x60st_inputx62_905 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_904', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60st_inputx62_905', tco_apply(shen_x60st_inputx62, [KL_ARG_V1553_903])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_905[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_905])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60st_inputx62_905)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_904, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_904)][(-1)]
shen_add_fun('shen.<st_input2>', shen_x60st_input2x62)

@tail_recursion
def shen_x60commentx62(KL_ARG_V1558_906):

    class KL_Context:
        KL_LOC_Result_907 = None
        KL_LOC_Parse_shen_x60singlelinex62_908 = None
        KL_LOC_Result_909 = None
        KL_LOC_Parse_shen_x60multilinex62_910 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_907', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60singlelinex62_908', tco_apply(shen_x60singlelinex62, [KL_ARG_V1558_906])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60singlelinex62_908[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60singlelinex62_908)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_909', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60multilinex62_910', tco_apply(shen_x60multilinex62, [KL_ARG_V1558_906])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60multilinex62_910[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60multilinex62_910)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_909, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_909)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_907, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_907)][(-1)]
shen_add_fun('shen.<comment>', shen_x60commentx62)

@tail_recursion
def shen_x60singlelinex62(KL_ARG_V1563_911):

    class KL_Context:
        KL_LOC_Result_912 = None
        KL_LOC_Parse_shen_x60backslashx62_913 = None
        KL_LOC_Parse_shen_x60backslashx62_914 = None
        KL_LOC_Parse_shen_x60anysinglex62_915 = None
        KL_LOC_Parse_shen_x60returnx62_916 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_912', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_913', tco_apply(shen_x60backslashx62, [KL_ARG_V1563_911])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_914', tco_apply(shen_x60backslashx62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_913])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anysinglex62_915', tco_apply(shen_x60anysinglex62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_914])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60returnx62_916', tco_apply(shen_x60returnx62, [KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_915])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60returnx62_916[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60returnx62_916)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_915)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_914)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_913)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_912, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_912)][(-1)]
shen_add_fun('shen.<singleline>', shen_x60singlelinex62)

@tail_recursion
def shen_x60backslashx62(KL_ARG_V1568_917):

    class KL_Context:
        KL_LOC_Result_918 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_918', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1568_917[0][1], tco_apply(shen_hdtl, [KL_ARG_V1568_917])])[0], symdic.symdic_shen_skip]) if (shen_eq(92, KL_ARG_V1568_917[0][0]) if shen_consp(KL_ARG_V1568_917[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_918, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_918)][(-1)]
shen_add_fun('shen.<backslash>', shen_x60backslashx62)

@tail_recursion
def shen_x60anysinglex62(KL_ARG_V1573_919):

    class KL_Context:
        KL_LOC_Result_920 = None
        KL_LOC_Parse_shen_x60nonx45returnx62_921 = None
        KL_LOC_Parse_shen_x60anysinglex62_922 = None
        KL_LOC_Result_923 = None
        KL_LOC_Parse_x60ex62_924 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_920', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60nonx45returnx62_921', tco_apply(shen_x60nonx45returnx62, [KL_ARG_V1573_919])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anysinglex62_922', tco_apply(shen_x60anysinglex62, [KL_CTX.KL_LOC_Parse_shen_x60nonx45returnx62_921])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_922[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anysinglex62_922)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60nonx45returnx62_921)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_923', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_924', tco_apply(kl_x60ex62, [KL_ARG_V1573_919])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_924[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_924)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_923, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_923)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_920, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_920)][(-1)]
shen_add_fun('shen.<anysingle>', shen_x60anysinglex62)

@tail_recursion
def shen_x60nonx45returnx62(KL_ARG_V1578_925):

    class KL_Context:
        KL_LOC_Result_926 = None
        KL_LOC_Parse_X_927 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_926', ([setattr(KL_CTX, 'KL_LOC_Parse_X_927', KL_ARG_V1578_925[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1578_925[0][1], tco_apply(shen_hdtl, [KL_ARG_V1578_925])])[0], symdic.symdic_shen_skip]) if (not tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_927, [10, [13, []]]])) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1578_925[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_926, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_926)][(-1)]
shen_add_fun('shen.<non-return>', shen_x60nonx45returnx62)

@tail_recursion
def shen_x60returnx62(KL_ARG_V1583_928):

    class KL_Context:
        KL_LOC_Result_929 = None
        KL_LOC_Parse_X_930 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_929', ([setattr(KL_CTX, 'KL_LOC_Parse_X_930', KL_ARG_V1583_928[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1583_928[0][1], tco_apply(shen_hdtl, [KL_ARG_V1583_928])])[0], symdic.symdic_shen_skip]) if tco_apply(kl_elementx63, [KL_CTX.KL_LOC_Parse_X_930, [10, [13, []]]]) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1583_928[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_929, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_929)][(-1)]
shen_add_fun('shen.<return>', shen_x60returnx62)

@tail_recursion
def shen_x60multilinex62(KL_ARG_V1588_931):

    class KL_Context:
        KL_LOC_Result_932 = None
        KL_LOC_Parse_shen_x60backslashx62_933 = None
        KL_LOC_Parse_shen_x60timesx62_934 = None
        KL_LOC_Parse_shen_x60anymultix62_935 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_932', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_933', tco_apply(shen_x60backslashx62, [KL_ARG_V1588_931])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_934', tco_apply(shen_x60timesx62, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_933])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_935', tco_apply(shen_x60anymultix62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_934])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anymultix62_935[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anymultix62_935)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60timesx62_934)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_933)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_932, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_932)][(-1)]
shen_add_fun('shen.<multiline>', shen_x60multilinex62)

@tail_recursion
def shen_x60timesx62(KL_ARG_V1593_936):

    class KL_Context:
        KL_LOC_Result_937 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_937', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1593_936[0][1], tco_apply(shen_hdtl, [KL_ARG_V1593_936])])[0], symdic.symdic_shen_skip]) if (shen_eq(42, KL_ARG_V1593_936[0][0]) if shen_consp(KL_ARG_V1593_936[0]) else False) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_937, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_937)][(-1)]
shen_add_fun('shen.<times>', shen_x60timesx62)

@tail_recursion
def shen_x60anymultix62(KL_ARG_V1598_938):

    class KL_Context:
        KL_LOC_Result_939 = None
        KL_LOC_Parse_shen_x60commentx62_940 = None
        KL_LOC_Parse_shen_x60anymultix62_941 = None
        KL_LOC_Result_942 = None
        KL_LOC_Parse_shen_x60timesx62_943 = None
        KL_LOC_Parse_shen_x60backslashx62_944 = None
        KL_LOC_Result_945 = None
        KL_LOC_Parse_X_946 = None
        KL_LOC_Parse_shen_x60anymultix62_947 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_939', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60commentx62_940', tco_apply(shen_x60commentx62, [KL_ARG_V1598_938])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_941', tco_apply(shen_x60anymultix62, [KL_CTX.KL_LOC_Parse_shen_x60commentx62_940])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anymultix62_941[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anymultix62_941)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60commentx62_940)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_942', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60timesx62_943', tco_apply(shen_x60timesx62, [KL_ARG_V1598_938])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60backslashx62_944', tco_apply(shen_x60backslashx62, [KL_CTX.KL_LOC_Parse_shen_x60timesx62_943])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60backslashx62_944[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60backslashx62_944)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60timesx62_943)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_945', ([setattr(KL_CTX, 'KL_LOC_Parse_X_946', KL_ARG_V1598_938[0][0]), [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60anymultix62_947', tco_apply(shen_x60anymultix62, [tco_apply(shen_pair, [KL_ARG_V1598_938[0][1], tco_apply(shen_hdtl, [KL_ARG_V1598_938])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60anymultix62_947[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60anymultix62_947)) else tco_apply(kl_fail, []))][(-1)]][(-1)] if shen_consp(KL_ARG_V1598_938[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_945, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_945)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_942, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_942)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_939, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_939)][(-1)]
shen_add_fun('shen.<anymulti>', shen_x60anymultix62)

@tail_recursion
def shen_x60whitespacesx62(KL_ARG_V1603_948):

    class KL_Context:
        KL_LOC_Result_949 = None
        KL_LOC_Parse_shen_x60whitespacex62_950 = None
        KL_LOC_Parse_shen_x60whitespacesx62_951 = None
        KL_LOC_Result_952 = None
        KL_LOC_Parse_shen_x60whitespacex62_953 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_949', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_950', tco_apply(shen_x60whitespacex62, [KL_ARG_V1603_948])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacesx62_951', tco_apply(shen_x60whitespacesx62, [KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_950])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_951[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacesx62_951)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_950)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_952', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60whitespacex62_953', tco_apply(shen_x60whitespacex62, [KL_ARG_V1603_948])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_953[0], symdic.symdic_shen_skip]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60whitespacex62_953)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_952, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_952)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_949, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_949)][(-1)]
shen_add_fun('shen.<whitespaces>', shen_x60whitespacesx62)

@tail_recursion
def shen_x60whitespacex62(KL_ARG_V1608_954):

    class KL_Context:
        KL_LOC_Result_955 = None
        KL_LOC_Parse_X_956 = None
        KL_LOC_Parse_Case_957 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_955', ([setattr(KL_CTX, 'KL_LOC_Parse_X_956', KL_ARG_V1608_954[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V1608_954[0][1], tco_apply(shen_hdtl, [KL_ARG_V1608_954])])[0], symdic.symdic_shen_skip]) if [setattr(KL_CTX, 'KL_LOC_Parse_Case_957', KL_CTX.KL_LOC_Parse_X_956), (True if shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 32) else (True if shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 13) else (True if shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 10) else shen_eq(KL_CTX.KL_LOC_Parse_Case_957, 9))))][(-1)] else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V1608_954[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_955, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_955)][(-1)]
shen_add_fun('shen.<whitespace>', shen_x60whitespacex62)

@tail_recursion
def shen_cons_form(KL_ARG_V1609_958):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1609_958) else ([symdic.symdic_kl_cons, [KL_ARG_V1609_958[0], KL_ARG_V1609_958[1][1]]] if ((((shen_eq(KL_ARG_V1609_958[1][0], symdic.symdic_kl_barx33) if shen_eq([], KL_ARG_V1609_958[1][1][1]) else False) if shen_consp(KL_ARG_V1609_958[1][1]) else False) if shen_consp(KL_ARG_V1609_958[1]) else False) if shen_consp(KL_ARG_V1609_958) else False) else ([symdic.symdic_kl_cons, [KL_ARG_V1609_958[0], [tco_apply(shen_cons_form, [KL_ARG_V1609_958[1]]), []]]] if shen_consp(KL_ARG_V1609_958) else (tail_call(shen_sysx45error, [symdic.symdic_shen_cons_form]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cons_form', shen_cons_form)

@tail_recursion
def shen_packagex45macro(KL_ARG_V1612_959, KL_ARG_V1613_960):

    class KL_Context:
        KL_LOC_ListofExceptions_961 = None
        KL_LOC_Record_962 = None
        KL_LOC_PackageNameDot_963 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_append, [tco_apply(kl_explode, [KL_ARG_V1612_959[1][0]]), KL_ARG_V1613_960]) if (((shen_eq([], KL_ARG_V1612_959[1][1]) if shen_consp(KL_ARG_V1612_959[1]) else False) if shen_eq(symdic.symdic_kl_x36, KL_ARG_V1612_959[0]) else False) if shen_consp(KL_ARG_V1612_959) else False) else (tail_call(kl_append, [KL_ARG_V1612_959[1][1][1], KL_ARG_V1613_960]) if ((((shen_consp(KL_ARG_V1612_959[1][1]) if shen_eq(symdic.symdic_kl_null, KL_ARG_V1612_959[1][0]) else False) if shen_consp(KL_ARG_V1612_959[1]) else False) if shen_eq(symdic.symdic_kl_package, KL_ARG_V1612_959[0]) else False) if shen_consp(KL_ARG_V1612_959) else False) else ([setattr(KL_CTX, 'KL_LOC_ListofExceptions_961', tco_apply(shen_evalx45withoutx45macros, [KL_ARG_V1612_959[1][1][0]])), [setattr(KL_CTX, 'KL_LOC_Record_962', tco_apply(shen_recordx45exceptions, [KL_CTX.KL_LOC_ListofExceptions_961, KL_ARG_V1612_959[1][0]])), [setattr(KL_CTX, 'KL_LOC_PackageNameDot_963', shen_intern((str(KL_ARG_V1612_959[1][0]) + '.'))), tail_call(kl_append, [tco_apply(shen_packageh, [KL_CTX.KL_LOC_PackageNameDot_963, KL_CTX.KL_LOC_ListofExceptions_961, KL_ARG_V1612_959[1][1][1]]), KL_ARG_V1613_960])][(-1)]][(-1)]][(-1)] if (((shen_consp(KL_ARG_V1612_959[1][1]) if shen_consp(KL_ARG_V1612_959[1]) else False) if shen_eq(symdic.symdic_kl_package, KL_ARG_V1612_959[0]) else False) if shen_consp(KL_ARG_V1612_959) else False) else ([KL_ARG_V1612_959, KL_ARG_V1613_960] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.package-macro', shen_packagex45macro)

@tail_recursion
def shen_recordx45exceptions(KL_ARG_V1614_964, KL_ARG_V1615_965):

    class KL_Context:
        KL_LOC_CurrExceptions_966 = None
        KL_LOC_AllExceptions_968 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_CurrExceptions_966', shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V1615_965, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_967: []))), [setattr(KL_CTX, 'KL_LOC_AllExceptions_968', tco_apply(kl_union, [KL_ARG_V1614_964, KL_CTX.KL_LOC_CurrExceptions_966])), tail_call(kl_put, [KL_ARG_V1615_965, symdic.symdic_shen_externalx45symbols, KL_CTX.KL_LOC_AllExceptions_968, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('shen.record-exceptions', shen_recordx45exceptions)

@tail_recursion
def shen_packageh(KL_ARG_V1624_969, KL_ARG_V1625_970, KL_ARG_V1626_971):
    global symdic
    return ([tco_apply(shen_packageh, [KL_ARG_V1624_969, KL_ARG_V1625_970, KL_ARG_V1626_971[0]]), tco_apply(shen_packageh, [KL_ARG_V1624_969, KL_ARG_V1625_970, KL_ARG_V1626_971[1]])] if shen_consp(KL_ARG_V1626_971) else (KL_ARG_V1626_971 if (True if tco_apply(shen_sysfuncx63, [KL_ARG_V1626_971]) else (True if tco_apply(kl_variablex63, [KL_ARG_V1626_971]) else (True if tco_apply(kl_elementx63, [KL_ARG_V1626_971, KL_ARG_V1625_970]) else (True if tco_apply(shen_doubleunderlinex63, [KL_ARG_V1626_971]) else tco_apply(shen_singleunderlinex63, [KL_ARG_V1626_971]))))) else (tail_call(kl_concat, [KL_ARG_V1624_969, KL_ARG_V1626_971]) if ((not tco_apply(shen_prefixx63, [['s', ['h', ['e', ['n', ['.', []]]]]], tco_apply(kl_explode, [KL_ARG_V1626_971])])) if tco_apply(kl_symbolx63, [KL_ARG_V1626_971]) else False) else (KL_ARG_V1626_971 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.packageh', shen_packageh)

@tail_recursion
def kl_readx45fromx45string(KL_ARG_V1627_972):

    class KL_Context:
        KL_LOC_Ns_973 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Ns_973', tco_apply(kl_map, [(lambda KL_ARG_V1327_974: ord(KL_ARG_V1327_974)), tco_apply(kl_explode, [KL_ARG_V1627_972])])), tail_call(kl_compile, [symdic.symdic_shen_x60st_inputx62, KL_CTX.KL_LOC_Ns_973, symdic.symdic_shen_readx45error])][(-1)]
shen_add_fun('read-from-string', kl_readx45fromx45string)


#============================== prolog.kl==============================



@tail_recursion
def shen_x60defprologx62(KL_ARG_V927_975):

    class KL_Context:
        KL_LOC_Result_976 = None
        KL_LOC_Parse_shen_x60predicatex42x62_977 = None
        KL_LOC_Parse_shen_x60clausesx42x62_978 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_976', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60predicatex42x62_977', tco_apply(shen_x60predicatex42x62, [KL_ARG_V927_975])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_978', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_977])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_978[0], tco_apply(shen_prologx45x62shen, [tco_apply(kl_map, [(lambda KL_ARG_Parse_X_979: tail_call(shen_insertx45predicate, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_977]), KL_ARG_Parse_X_979])), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_978])])])[0]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_978)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60predicatex42x62_977)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_976, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_976)][(-1)]
shen_add_fun('shen.<defprolog>', shen_x60defprologx62)

@tail_recursion
def shen_prologx45error(KL_ARG_V934_980, KL_ARG_V935_981):
    global symdic
    return (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V934_980, (' here:\r\n\r\n ' + tco_apply(shen_app, [tco_apply(shen_nextx4550, [50, KL_ARG_V935_981[0]]), '\r\n', symdic.symdic_shen_a])), symdic.symdic_shen_a]))) if ((shen_eq([], KL_ARG_V935_981[1][1]) if shen_consp(KL_ARG_V935_981[1]) else False) if shen_consp(KL_ARG_V935_981) else False) else (shen_simple_error(('prolog syntax error in ' + tco_apply(shen_app, [KL_ARG_V934_980, '\r\n', symdic.symdic_shen_a]))) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-error', shen_prologx45error)

@tail_recursion
def shen_nextx4550(KL_ARG_V940_982, KL_ARG_V941_983):
    global symdic
    return ('' if shen_eq([], KL_ARG_V941_983) else ('' if shen_eq(0, KL_ARG_V940_982) else ((tco_apply(shen_deconsx45string, [KL_ARG_V941_983[0]]) + tco_apply(shen_nextx4550, [(KL_ARG_V940_982 - 1), KL_ARG_V941_983[1]])) if shen_consp(KL_ARG_V941_983) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nextx4550]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.next-50', shen_nextx4550)

@tail_recursion
def shen_deconsx45string(KL_ARG_V942_984):
    global symdic
    return (tail_call(shen_app, [tco_apply(shen_evalx45cons, [KL_ARG_V942_984]), ' ', symdic.symdic_shen_s]) if ((((shen_eq([], KL_ARG_V942_984[1][1][1]) if shen_consp(KL_ARG_V942_984[1][1]) else False) if shen_consp(KL_ARG_V942_984[1]) else False) if shen_eq(symdic.symdic_kl_cons, KL_ARG_V942_984[0]) else False) if shen_consp(KL_ARG_V942_984) else False) else (tail_call(shen_app, [KL_ARG_V942_984, ' ', symdic.symdic_shen_r]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.decons-string', shen_deconsx45string)

@tail_recursion
def shen_insertx45predicate(KL_ARG_V943_985, KL_ARG_V944_986):
    global symdic
    return ([[KL_ARG_V943_985, KL_ARG_V944_986[0]], [symdic.symdic_kl_x58x45, KL_ARG_V944_986[1]]] if ((shen_eq([], KL_ARG_V944_986[1][1]) if shen_consp(KL_ARG_V944_986[1]) else False) if shen_consp(KL_ARG_V944_986) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45predicate]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.insert-predicate', shen_insertx45predicate)

@tail_recursion
def shen_x60predicatex42x62(KL_ARG_V949_987):

    class KL_Context:
        KL_LOC_Result_988 = None
        KL_LOC_Parse_X_989 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_988', ([setattr(KL_CTX, 'KL_LOC_Parse_X_989', KL_ARG_V949_987[0][0]), tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V949_987[0][1], tco_apply(shen_hdtl, [KL_ARG_V949_987])])[0], KL_CTX.KL_LOC_Parse_X_989])][(-1)] if shen_consp(KL_ARG_V949_987[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_988, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_988)][(-1)]
shen_add_fun('shen.<predicate*>', shen_x60predicatex42x62)

@tail_recursion
def shen_x60clausesx42x62(KL_ARG_V954_990):

    class KL_Context:
        KL_LOC_Result_991 = None
        KL_LOC_Parse_shen_x60clausex42x62_992 = None
        KL_LOC_Parse_shen_x60clausesx42x62_993 = None
        KL_LOC_Result_994 = None
        KL_LOC_Parse_x60ex62_995 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_991', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausex42x62_992', tco_apply(shen_x60clausex42x62, [KL_ARG_V954_990])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60clausesx42x62_993', tco_apply(shen_x60clausesx42x62, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_992])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_993[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_992]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_993])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausesx42x62_993)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60clausex42x62_992)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_994', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_995', tco_apply(kl_x60ex62, [KL_ARG_V954_990])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_995[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_995]), []])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_995)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_994, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_994)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_991, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_991)][(-1)]
shen_add_fun('shen.<clauses*>', shen_x60clausesx42x62)

@tail_recursion
def shen_x60clausex42x62(KL_ARG_V959_996):

    class KL_Context:
        KL_LOC_Result_997 = None
        KL_LOC_Parse_shen_x60headx42x62_998 = None
        KL_LOC_Parse_shen_x60bodyx42x62_999 = None
        KL_LOC_Parse_shen_x60endx42x62_1000 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_997', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_998', tco_apply(shen_x60headx42x62, [KL_ARG_V959_996])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_999', tco_apply(shen_x60bodyx42x62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998])])])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60endx42x62_1000', tco_apply(shen_x60endx42x62, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_999])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60endx42x62_1000[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998]), [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_999]), []]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60endx42x62_1000)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_999)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45x45, KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60headx42x62_998)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_997, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_997)][(-1)]
shen_add_fun('shen.<clause*>', shen_x60clausex42x62)

@tail_recursion
def shen_x60headx42x62(KL_ARG_V964_1001):

    class KL_Context:
        KL_LOC_Result_1002 = None
        KL_LOC_Parse_shen_x60termx42x62_1003 = None
        KL_LOC_Parse_shen_x60headx42x62_1004 = None
        KL_LOC_Result_1005 = None
        KL_LOC_Parse_x60ex62_1006 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1002', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60termx42x62_1003', tco_apply(shen_x60termx42x62, [KL_ARG_V964_1001])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60headx42x62_1004', tco_apply(shen_x60headx42x62, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1003])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1004[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1003]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1004])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60headx42x62_1004)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60termx42x62_1003)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1005', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_1006', tco_apply(kl_x60ex62, [KL_ARG_V964_1001])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_1006[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_1006]), []])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_1006)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1005, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1005)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1002, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1002)][(-1)]
shen_add_fun('shen.<head*>', shen_x60headx42x62)

@tail_recursion
def shen_x60termx42x62(KL_ARG_V969_1007):

    class KL_Context:
        KL_LOC_Result_1008 = None
        KL_LOC_Parse_X_1009 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1008', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1009', KL_ARG_V969_1007[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V969_1007[0][1], tco_apply(shen_hdtl, [KL_ARG_V969_1007])])[0], tco_apply(shen_evalx45cons, [KL_CTX.KL_LOC_Parse_X_1009])]) if (tco_apply(shen_legitimatex45termx63, [KL_CTX.KL_LOC_Parse_X_1009]) if (not shen_eq(symdic.symdic_kl_x60x45x45, KL_CTX.KL_LOC_Parse_X_1009)) else False) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V969_1007[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1008, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1008)][(-1)]
shen_add_fun('shen.<term*>', shen_x60termx42x62)

@tail_recursion
def shen_legitimatex45termx63(KL_ARG_V974_1010):
    global symdic
    return ((tail_call(shen_legitimatex45termx63, [KL_ARG_V974_1010[1][1][0]]) if tco_apply(shen_legitimatex45termx63, [KL_ARG_V974_1010[1][0]]) else False) if ((((shen_eq([], KL_ARG_V974_1010[1][1][1]) if shen_consp(KL_ARG_V974_1010[1][1]) else False) if shen_consp(KL_ARG_V974_1010[1]) else False) if shen_eq(symdic.symdic_kl_cons, KL_ARG_V974_1010[0]) else False) if shen_consp(KL_ARG_V974_1010) else False) else (tail_call(shen_legitimatex45termx63, [KL_ARG_V974_1010[1][0]]) if (((((shen_eq([], KL_ARG_V974_1010[1][1][1]) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V974_1010[1][1][0]) else False) if shen_consp(KL_ARG_V974_1010[1][1]) else False) if shen_consp(KL_ARG_V974_1010[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V974_1010[0]) else False) if shen_consp(KL_ARG_V974_1010) else False) else (tail_call(shen_legitimatex45termx63, [KL_ARG_V974_1010[1][0]]) if (((((shen_eq([], KL_ARG_V974_1010[1][1][1]) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V974_1010[1][1][0]) else False) if shen_consp(KL_ARG_V974_1010[1][1]) else False) if shen_consp(KL_ARG_V974_1010[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V974_1010[0]) else False) if shen_consp(KL_ARG_V974_1010) else False) else (False if shen_consp(KL_ARG_V974_1010) else (True if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.legitimate-term?', shen_legitimatex45termx63)

@tail_recursion
def shen_evalx45cons(KL_ARG_V975_1011):
    global symdic
    return ([tco_apply(shen_evalx45cons, [KL_ARG_V975_1011[1][0]]), tco_apply(shen_evalx45cons, [KL_ARG_V975_1011[1][1][0]])] if ((((shen_eq([], KL_ARG_V975_1011[1][1][1]) if shen_consp(KL_ARG_V975_1011[1][1]) else False) if shen_consp(KL_ARG_V975_1011[1]) else False) if shen_eq(symdic.symdic_kl_cons, KL_ARG_V975_1011[0]) else False) if shen_consp(KL_ARG_V975_1011) else False) else ([symdic.symdic_kl_mode, [tco_apply(shen_evalx45cons, [KL_ARG_V975_1011[1][0]]), KL_ARG_V975_1011[1][1]]] if ((((shen_eq([], KL_ARG_V975_1011[1][1][1]) if shen_consp(KL_ARG_V975_1011[1][1]) else False) if shen_consp(KL_ARG_V975_1011[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V975_1011[0]) else False) if shen_consp(KL_ARG_V975_1011) else False) else (KL_ARG_V975_1011 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.eval-cons', shen_evalx45cons)

@tail_recursion
def shen_x60bodyx42x62(KL_ARG_V980_1012):

    class KL_Context:
        KL_LOC_Result_1013 = None
        KL_LOC_Parse_shen_x60literalx42x62_1014 = None
        KL_LOC_Parse_shen_x60bodyx42x62_1015 = None
        KL_LOC_Result_1016 = None
        KL_LOC_Parse_x60ex62_1017 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1013', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60literalx42x62_1014', tco_apply(shen_x60literalx42x62, [KL_ARG_V980_1012])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60bodyx42x62_1015', tco_apply(shen_x60bodyx42x62, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1014])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1015[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1014]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1015])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60bodyx42x62_1015)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60literalx42x62_1014)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1016', [setattr(KL_CTX, 'KL_LOC_Parse_x60ex62_1017', tco_apply(kl_x60ex62, [KL_ARG_V980_1012])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60ex62_1017[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_x60ex62_1017]), []])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60ex62_1017)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1016, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1016)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1013, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1013)][(-1)]
shen_add_fun('shen.<body*>', shen_x60bodyx42x62)

@tail_recursion
def shen_x60literalx42x62(KL_ARG_V985_1018):

    class KL_Context:
        KL_LOC_Result_1019 = None
        KL_LOC_Result_1020 = None
        KL_LOC_Parse_X_1021 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1019', (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V985_1018[0][1], tco_apply(shen_hdtl, [KL_ARG_V985_1018])])[0], [symdic.symdic_kl_cut, [shen_intern('Throwcontrol'), []]]]) if (shen_eq(symdic.symdic_kl_x33, KL_ARG_V985_1018[0][0]) if shen_consp(KL_ARG_V985_1018[0]) else False) else tco_apply(kl_fail, []))), ([setattr(KL_CTX, 'KL_LOC_Result_1020', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1021', KL_ARG_V985_1018[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V985_1018[0][1], tco_apply(shen_hdtl, [KL_ARG_V985_1018])])[0], KL_CTX.KL_LOC_Parse_X_1021]) if shen_consp(KL_CTX.KL_LOC_Parse_X_1021) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V985_1018[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1020, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1020)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1019, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1019)][(-1)]
shen_add_fun('shen.<literal*>', shen_x60literalx42x62)

@tail_recursion
def shen_x60endx42x62(KL_ARG_V990_1022):

    class KL_Context:
        KL_LOC_Result_1023 = None
        KL_LOC_Parse_X_1024 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1023', ([setattr(KL_CTX, 'KL_LOC_Parse_X_1024', KL_ARG_V990_1022[0][0]), (tco_apply(shen_pair, [tco_apply(shen_pair, [KL_ARG_V990_1022[0][1], tco_apply(shen_hdtl, [KL_ARG_V990_1022])])[0], KL_CTX.KL_LOC_Parse_X_1024]) if shen_eq(KL_CTX.KL_LOC_Parse_X_1024, symdic.symdic_kl_x59) else tco_apply(kl_fail, []))][(-1)] if shen_consp(KL_ARG_V990_1022[0]) else tco_apply(kl_fail, []))), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1023, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1023)][(-1)]
shen_add_fun('shen.<end*>', shen_x60endx42x62)

@tail_recursion
def kl_cut(KL_ARG_V991_1025, KL_ARG_V992_1026, KL_ARG_V993_1027):

    class KL_Context:
        KL_LOC_Result_1028 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1028', tco_apply(kl_thaw, [KL_ARG_V993_1027])), (KL_ARG_V991_1025 if shen_eq(KL_CTX.KL_LOC_Result_1028, False) else KL_CTX.KL_LOC_Result_1028)][(-1)]
shen_add_fun('cut', kl_cut)

@tail_recursion
def shen_insert_modes(KL_ARG_V994_1029):
    global symdic
    return (KL_ARG_V994_1029 if ((((shen_eq([], KL_ARG_V994_1029[1][1][1]) if shen_consp(KL_ARG_V994_1029[1][1]) else False) if shen_consp(KL_ARG_V994_1029[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V994_1029[0]) else False) if shen_consp(KL_ARG_V994_1029) else False) else ([] if shen_eq([], KL_ARG_V994_1029) else ([[symdic.symdic_kl_mode, [KL_ARG_V994_1029[0], [symdic.symdic_kl_x43, []]]], [symdic.symdic_kl_mode, [tco_apply(shen_insert_modes, [KL_ARG_V994_1029[1]]), [symdic.symdic_kl_x45, []]]]] if shen_consp(KL_ARG_V994_1029) else (KL_ARG_V994_1029 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert_modes', shen_insert_modes)

@tail_recursion
def shen_sx45prolog(KL_ARG_V995_1030):
    global symdic
    return tail_call(kl_map, [(lambda KL_ARG_V921_1031: tail_call(kl_eval, [KL_ARG_V921_1031])), tco_apply(shen_prologx45x62shen, [KL_ARG_V995_1030])])
shen_add_fun('shen.s-prolog', shen_sx45prolog)

@tail_recursion
def shen_prologx45x62shen(KL_ARG_V996_1032):
    global symdic
    return tail_call(kl_map, [symdic.symdic_shen_compile_prolog_procedure, tco_apply(shen_group_clauses, [tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_clause, tco_apply(kl_mapcan, [symdic.symdic_shen_head_abstraction, KL_ARG_V996_1032])])])])
shen_add_fun('shen.prolog->shen', shen_prologx45x62shen)

@tail_recursion
def shen_sx45prolog_clause(KL_ARG_V997_1033):
    global symdic
    return ([KL_ARG_V997_1033[0], [symdic.symdic_kl_x58x45, [tco_apply(kl_map, [symdic.symdic_shen_sx45prolog_literal, KL_ARG_V997_1033[1][1][0]]), []]]] if ((((shen_eq([], KL_ARG_V997_1033[1][1][1]) if shen_consp(KL_ARG_V997_1033[1][1]) else False) if shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V997_1033[1][0]) else False) if shen_consp(KL_ARG_V997_1033[1]) else False) if shen_consp(KL_ARG_V997_1033) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.s-prolog_clause', shen_sx45prolog_clause)

@tail_recursion
def shen_head_abstraction(KL_ARG_V998_1034):

    class KL_Context:
        KL_LOC_Terms_1035 = None
        KL_LOC_XTerms_1037 = None
        KL_LOC_Literal_1038 = None
        KL_LOC_Clause_1039 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V998_1034, []] if ((((((tco_apply(shen_complexity_head, [KL_ARG_V998_1034[0]]) < shen_get(symdic.symdic_shen_x42maxcomplexityx42)) if shen_eq([], KL_ARG_V998_1034[1][1][1]) else False) if shen_consp(KL_ARG_V998_1034[1][1]) else False) if shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V998_1034[1][0]) else False) if shen_consp(KL_ARG_V998_1034[1]) else False) if shen_consp(KL_ARG_V998_1034) else False) else ([setattr(KL_CTX, 'KL_LOC_Terms_1035', tco_apply(kl_map, [(lambda KL_ARG_Y_1036: tail_call(kl_gensym, [symdic.symdic_V])), KL_ARG_V998_1034[0][1]])), [setattr(KL_CTX, 'KL_LOC_XTerms_1037', tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [KL_ARG_V998_1034[0][1]])])), [setattr(KL_CTX, 'KL_LOC_Literal_1038', [symdic.symdic_kl_unify, [tco_apply(shen_cons_form, [KL_CTX.KL_LOC_Terms_1035]), [KL_CTX.KL_LOC_XTerms_1037, []]]]), [setattr(KL_CTX, 'KL_LOC_Clause_1039', [[KL_ARG_V998_1034[0][0], KL_CTX.KL_LOC_Terms_1035], [symdic.symdic_kl_x58x45, [[KL_CTX.KL_LOC_Literal_1038, KL_ARG_V998_1034[1][1][0]], []]]]), [KL_CTX.KL_LOC_Clause_1039, []]][(-1)]][(-1)]][(-1)]][(-1)] if (((((shen_eq([], KL_ARG_V998_1034[1][1][1]) if shen_consp(KL_ARG_V998_1034[1][1]) else False) if shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V998_1034[1][0]) else False) if shen_consp(KL_ARG_V998_1034[1]) else False) if shen_consp(KL_ARG_V998_1034[0]) else False) if shen_consp(KL_ARG_V998_1034) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_head_abstraction]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.head_abstraction', shen_head_abstraction)

@tail_recursion
def shen_complexity_head(KL_ARG_V1003_1040):
    global symdic
    return (tail_call(shen_product, [tco_apply(kl_map, [symdic.symdic_shen_complexity, KL_ARG_V1003_1040[1]])]) if shen_consp(KL_ARG_V1003_1040) else (tail_call(shen_sysx45error, [symdic.symdic_shen_complexity_head]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.complexity_head', shen_complexity_head)

@tail_recursion
def shen_complexity(KL_ARG_V1011_1041):
    global symdic
    return (tail_call(shen_complexity, [KL_ARG_V1011_1041[1][0]]) if (((((((((shen_eq([], KL_ARG_V1011_1041[1][1][1]) if shen_consp(KL_ARG_V1011_1041[1][1]) else False) if shen_eq([], KL_ARG_V1011_1041[1][0][1][1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1][0][1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1][0][1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1011_1041[1][0][0]) else False) if shen_consp(KL_ARG_V1011_1041[1][0]) else False) if shen_consp(KL_ARG_V1011_1041[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1011_1041[0]) else False) if shen_consp(KL_ARG_V1011_1041) else False) else ((2 * (tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V1011_1041[1][0][0], KL_ARG_V1011_1041[1][1]]]]) * tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V1011_1041[1][0][1], KL_ARG_V1011_1041[1][1]]]]))) if ((((((shen_eq([], KL_ARG_V1011_1041[1][1][1]) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1011_1041[1][1][0]) else False) if shen_consp(KL_ARG_V1011_1041[1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1][0]) else False) if shen_consp(KL_ARG_V1011_1041[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1011_1041[0]) else False) if shen_consp(KL_ARG_V1011_1041) else False) else ((tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V1011_1041[1][0][0], KL_ARG_V1011_1041[1][1]]]]) * tco_apply(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V1011_1041[1][0][1], KL_ARG_V1011_1041[1][1]]]])) if ((((((shen_eq([], KL_ARG_V1011_1041[1][1][1]) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1011_1041[1][1][0]) else False) if shen_consp(KL_ARG_V1011_1041[1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1][0]) else False) if shen_consp(KL_ARG_V1011_1041[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1011_1041[0]) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (1 if (((((tco_apply(kl_variablex63, [KL_ARG_V1011_1041[1][0]]) if shen_eq([], KL_ARG_V1011_1041[1][1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1011_1041[0]) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (2 if (((((shen_eq([], KL_ARG_V1011_1041[1][1][1]) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1011_1041[1][1][0]) else False) if shen_consp(KL_ARG_V1011_1041[1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1011_1041[0]) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (1 if (((((shen_eq([], KL_ARG_V1011_1041[1][1][1]) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1011_1041[1][1][0]) else False) if shen_consp(KL_ARG_V1011_1041[1][1]) else False) if shen_consp(KL_ARG_V1011_1041[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1011_1041[0]) else False) if shen_consp(KL_ARG_V1011_1041) else False) else (tail_call(shen_complexity, [[symdic.symdic_kl_mode, [KL_ARG_V1011_1041, [symdic.symdic_kl_x43, []]]]]) if True else shen_simple_error('condition failure'))))))))
shen_add_fun('shen.complexity', shen_complexity)

@tail_recursion
def shen_product(KL_ARG_V1012_1042):
    global symdic
    return (1 if shen_eq([], KL_ARG_V1012_1042) else ((KL_ARG_V1012_1042[0] * tco_apply(shen_product, [KL_ARG_V1012_1042[1]])) if shen_consp(KL_ARG_V1012_1042) else (tail_call(shen_sysx45error, [symdic.symdic_shen_product]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.product', shen_product)

@tail_recursion
def shen_sx45prolog_literal(KL_ARG_V1013_1043):
    global symdic
    return ([symdic.symdic_kl_bind, [KL_ARG_V1013_1043[1][0], [tco_apply(shen_insert_deref, [KL_ARG_V1013_1043[1][1][0]]), []]]] if ((((shen_eq([], KL_ARG_V1013_1043[1][1][1]) if shen_consp(KL_ARG_V1013_1043[1][1]) else False) if shen_consp(KL_ARG_V1013_1043[1]) else False) if shen_eq(symdic.symdic_kl_is, KL_ARG_V1013_1043[0]) else False) if shen_consp(KL_ARG_V1013_1043) else False) else ([symdic.symdic_kl_fwhen, [tco_apply(shen_insert_deref, [KL_ARG_V1013_1043[1][0]]), []]] if (((shen_eq([], KL_ARG_V1013_1043[1][1]) if shen_consp(KL_ARG_V1013_1043[1]) else False) if shen_eq(symdic.symdic_kl_when, KL_ARG_V1013_1043[0]) else False) if shen_consp(KL_ARG_V1013_1043) else False) else ([symdic.symdic_kl_bind, [KL_ARG_V1013_1043[1][0], [tco_apply(shen_insert_lazyderef, [KL_ARG_V1013_1043[1][1][0]]), []]]] if ((((shen_eq([], KL_ARG_V1013_1043[1][1][1]) if shen_consp(KL_ARG_V1013_1043[1][1]) else False) if shen_consp(KL_ARG_V1013_1043[1]) else False) if shen_eq(symdic.symdic_kl_bind, KL_ARG_V1013_1043[0]) else False) if shen_consp(KL_ARG_V1013_1043) else False) else ([symdic.symdic_kl_fwhen, [tco_apply(shen_insert_lazyderef, [KL_ARG_V1013_1043[1][0]]), []]] if (((shen_eq([], KL_ARG_V1013_1043[1][1]) if shen_consp(KL_ARG_V1013_1043[1]) else False) if shen_eq(symdic.symdic_kl_fwhen, KL_ARG_V1013_1043[0]) else False) if shen_consp(KL_ARG_V1013_1043) else False) else ([tco_apply(shen_m_prolog_to_sx45prolog_predicate, [KL_ARG_V1013_1043[0]]), KL_ARG_V1013_1043[1]] if shen_consp(KL_ARG_V1013_1043) else (tail_call(shen_sysx45error, [symdic.symdic_shen_sx45prolog_literal]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.s-prolog_literal', shen_sx45prolog_literal)

@tail_recursion
def shen_insert_deref(KL_ARG_V1014_1044):
    global symdic
    return ([symdic.symdic_shen_deref, [KL_ARG_V1014_1044, [symdic.symdic_ProcessN, []]]] if tco_apply(kl_variablex63, [KL_ARG_V1014_1044]) else ([tco_apply(shen_insert_deref, [KL_ARG_V1014_1044[0]]), tco_apply(shen_insert_deref, [KL_ARG_V1014_1044[1]])] if shen_consp(KL_ARG_V1014_1044) else (KL_ARG_V1014_1044 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_deref', shen_insert_deref)

@tail_recursion
def shen_insert_lazyderef(KL_ARG_V1015_1045):
    global symdic
    return ([symdic.symdic_shen_lazyderef, [KL_ARG_V1015_1045, [symdic.symdic_ProcessN, []]]] if tco_apply(kl_variablex63, [KL_ARG_V1015_1045]) else ([tco_apply(shen_insert_lazyderef, [KL_ARG_V1015_1045[0]]), tco_apply(shen_insert_lazyderef, [KL_ARG_V1015_1045[1]])] if shen_consp(KL_ARG_V1015_1045) else (KL_ARG_V1015_1045 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.insert_lazyderef', shen_insert_lazyderef)

@tail_recursion
def shen_m_prolog_to_sx45prolog_predicate(KL_ARG_V1016_1046):
    global symdic
    return (symdic.symdic_kl_unify if shen_eq(symdic.symdic_kl_x61, KL_ARG_V1016_1046) else (symdic.symdic_kl_unifyx33 if shen_eq(symdic.symdic_kl_x61x33, KL_ARG_V1016_1046) else (symdic.symdic_kl_identical if shen_eq(symdic.symdic_kl_x61x61, KL_ARG_V1016_1046) else (KL_ARG_V1016_1046 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.m_prolog_to_s-prolog_predicate', shen_m_prolog_to_sx45prolog_predicate)

@tail_recursion
def shen_group_clauses(KL_ARG_V1017_1047):

    class KL_Context:
        KL_LOC_Group_1048 = None
        KL_LOC_Rest_1050 = None
    KL_CTX = KL_Context()
    global symdic
    return ([] if shen_eq([], KL_ARG_V1017_1047) else ([setattr(KL_CTX, 'KL_LOC_Group_1048', tco_apply(shen_collect, [(lambda KL_ARG_X_1049: tail_call(shen_same_predicatex63, [KL_ARG_V1017_1047[0], KL_ARG_X_1049])), KL_ARG_V1017_1047])), [setattr(KL_CTX, 'KL_LOC_Rest_1050', tco_apply(kl_difference, [KL_ARG_V1017_1047, KL_CTX.KL_LOC_Group_1048])), [KL_CTX.KL_LOC_Group_1048, tco_apply(shen_group_clauses, [KL_CTX.KL_LOC_Rest_1050])]][(-1)]][(-1)] if shen_consp(KL_ARG_V1017_1047) else (tail_call(shen_sysx45error, [symdic.symdic_shen_group_clauses]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.group_clauses', shen_group_clauses)

@tail_recursion
def shen_collect(KL_ARG_V1020_1051, KL_ARG_V1021_1052):
    global symdic
    return ([] if shen_eq([], KL_ARG_V1021_1052) else (([KL_ARG_V1021_1052[0], tco_apply(shen_collect, [KL_ARG_V1020_1051, KL_ARG_V1021_1052[1]])] if shen_apply(KL_ARG_V1020_1051, [KL_ARG_V1021_1052[0]]) else tail_call(shen_collect, [KL_ARG_V1020_1051, KL_ARG_V1021_1052[1]])) if shen_consp(KL_ARG_V1021_1052) else (tail_call(shen_sysx45error, [symdic.symdic_shen_collect]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.collect', shen_collect)

@tail_recursion
def shen_same_predicatex63(KL_ARG_V1038_1053, KL_ARG_V1039_1054):
    global symdic
    return (shen_eq(KL_ARG_V1038_1053[0][0], KL_ARG_V1039_1054[0][0]) if (((shen_consp(KL_ARG_V1039_1054[0]) if shen_consp(KL_ARG_V1039_1054) else False) if shen_consp(KL_ARG_V1038_1053[0]) else False) if shen_consp(KL_ARG_V1038_1053) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_same_predicatex63]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.same_predicate?', shen_same_predicatex63)

@tail_recursion
def shen_compile_prolog_procedure(KL_ARG_V1040_1055):

    class KL_Context:
        KL_LOC_F_1056 = None
        KL_LOC_Shen_1057 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_F_1056', tco_apply(shen_procedure_name, [KL_ARG_V1040_1055])), [setattr(KL_CTX, 'KL_LOC_Shen_1057', tco_apply(shen_clausesx45tox45shen, [KL_CTX.KL_LOC_F_1056, KL_ARG_V1040_1055])), KL_CTX.KL_LOC_Shen_1057][(-1)]][(-1)]
shen_add_fun('shen.compile_prolog_procedure', shen_compile_prolog_procedure)

@tail_recursion
def shen_procedure_name(KL_ARG_V1053_1058):
    global symdic
    return (KL_ARG_V1053_1058[0][0][0] if ((shen_consp(KL_ARG_V1053_1058[0][0]) if shen_consp(KL_ARG_V1053_1058[0]) else False) if shen_consp(KL_ARG_V1053_1058) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procedure_name]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.procedure_name', shen_procedure_name)

@tail_recursion
def shen_clausesx45tox45shen(KL_ARG_V1054_1059, KL_ARG_V1055_1060):

    class KL_Context:
        KL_LOC_Linear_1061 = None
        KL_LOC_Arity_1062 = None
        KL_LOC_Parameters_1064 = None
        KL_LOC_AUM_instructions_1065 = None
        KL_LOC_Code_1067 = None
        KL_LOC_ShenDef_1068 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Linear_1061', tco_apply(kl_map, [symdic.symdic_shen_linearisex45clause, KL_ARG_V1055_1060])), [setattr(KL_CTX, 'KL_LOC_Arity_1062', tco_apply(shen_prologx45aritycheck, [KL_ARG_V1054_1059, tco_apply(kl_map, [(lambda KL_ARG_V922_1063: tail_call(kl_head, [KL_ARG_V922_1063])), KL_ARG_V1055_1060])])), [setattr(KL_CTX, 'KL_LOC_Parameters_1064', tco_apply(shen_parameters, [KL_CTX.KL_LOC_Arity_1062])), [setattr(KL_CTX, 'KL_LOC_AUM_instructions_1065', tco_apply(kl_map, [(lambda KL_ARG_X_1066: tail_call(shen_aum, [KL_ARG_X_1066, KL_CTX.KL_LOC_Parameters_1064])), KL_CTX.KL_LOC_Linear_1061])), [setattr(KL_CTX, 'KL_LOC_Code_1067', tco_apply(shen_catchx45cut, [tco_apply(shen_nestx45disjunct, [tco_apply(kl_map, [symdic.symdic_shen_aum_to_shen, KL_CTX.KL_LOC_AUM_instructions_1065])])])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1068', [symdic.symdic_kl_define, [KL_ARG_V1054_1059, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1064, tco_apply(kl_append, [[symdic.symdic_ProcessN, [symdic.symdic_Continuation, []]], [symdic.symdic_kl_x45x62, [KL_CTX.KL_LOC_Code_1067, []]]])])]]), KL_CTX.KL_LOC_ShenDef_1068][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.clauses-to-shen', shen_clausesx45tox45shen)

@tail_recursion
def shen_catchx45cut(KL_ARG_V1056_1069):
    global symdic
    return (KL_ARG_V1056_1069 if (not tco_apply(shen_occursx63, [symdic.symdic_kl_cut, KL_ARG_V1056_1069])) else ([symdic.symdic_kl_let, [symdic.symdic_Throwcontrol, [[symdic.symdic_shen_catchpoint, []], [[symdic.symdic_shen_cutpoint, [symdic.symdic_Throwcontrol, [KL_ARG_V1056_1069, []]]], []]]]] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.catch-cut', shen_catchx45cut)

@tail_recursion
def shen_catchpoint():
    global symdic
    return shen_set(symdic.symdic_shen_x42catchx42, (1 + shen_get(symdic.symdic_shen_x42catchx42)))
shen_add_fun('shen.catchpoint', shen_catchpoint)

@tail_recursion
def shen_cutpoint(KL_ARG_V1061_1070, KL_ARG_V1062_1071):
    global symdic
    return (False if shen_eq(KL_ARG_V1062_1071, KL_ARG_V1061_1070) else (KL_ARG_V1062_1071 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cutpoint', shen_cutpoint)

@tail_recursion
def shen_nestx45disjunct(KL_ARG_V1064_1072):
    global symdic
    return (KL_ARG_V1064_1072[0] if (shen_eq([], KL_ARG_V1064_1072[1]) if shen_consp(KL_ARG_V1064_1072) else False) else (tail_call(shen_lispx45or, [KL_ARG_V1064_1072[0], tco_apply(shen_nestx45disjunct, [KL_ARG_V1064_1072[1]])]) if shen_consp(KL_ARG_V1064_1072) else (tail_call(shen_sysx45error, [symdic.symdic_shen_nestx45disjunct]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.nest-disjunct', shen_nestx45disjunct)

@tail_recursion
def shen_lispx45or(KL_ARG_V1065_1073, KL_ARG_V1066_1074):
    global symdic
    return [symdic.symdic_kl_let, [symdic.symdic_Case, [KL_ARG_V1065_1073, [[symdic.symdic_kl_if, [[symdic.symdic_kl_x61, [symdic.symdic_Case, [False, []]]], [KL_ARG_V1066_1074, [symdic.symdic_Case, []]]]], []]]]]
shen_add_fun('shen.lisp-or', shen_lispx45or)

@tail_recursion
def shen_prologx45aritycheck(KL_ARG_V1069_1075, KL_ARG_V1070_1076):
    global symdic
    return ((tco_apply(kl_length, [KL_ARG_V1070_1076[0]]) - 1) if (shen_eq([], KL_ARG_V1070_1076[1]) if shen_consp(KL_ARG_V1070_1076) else False) else ((tail_call(shen_prologx45aritycheck, [KL_ARG_V1069_1075, KL_ARG_V1070_1076[1]]) if shen_eq(tco_apply(kl_length, [KL_ARG_V1070_1076[0]]), tco_apply(kl_length, [KL_ARG_V1070_1076[1][0]])) else shen_simple_error(('arity error in prolog procedure ' + tco_apply(shen_app, [[KL_ARG_V1069_1075, []], '\r\n', symdic.symdic_shen_a])))) if (shen_consp(KL_ARG_V1070_1076[1]) if shen_consp(KL_ARG_V1070_1076) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_prologx45aritycheck]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.prolog-aritycheck', shen_prologx45aritycheck)

@tail_recursion
def shen_linearisex45clause(KL_ARG_V1071_1077):

    class KL_Context:
        KL_LOC_Linear_1078 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Linear_1078', tco_apply(shen_linearise, [[KL_ARG_V1071_1077[0], KL_ARG_V1071_1077[1][1]]])), tail_call(shen_clause_form, [KL_CTX.KL_LOC_Linear_1078])][(-1)] if ((((shen_eq([], KL_ARG_V1071_1077[1][1][1]) if shen_consp(KL_ARG_V1071_1077[1][1]) else False) if shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V1071_1077[1][0]) else False) if shen_consp(KL_ARG_V1071_1077[1]) else False) if shen_consp(KL_ARG_V1071_1077) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_linearisex45clause]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.linearise-clause', shen_linearisex45clause)

@tail_recursion
def shen_clause_form(KL_ARG_V1072_1079):
    global symdic
    return ([tco_apply(shen_explicit_modes, [KL_ARG_V1072_1079[0]]), [symdic.symdic_kl_x58x45, [tco_apply(shen_cf_help, [KL_ARG_V1072_1079[1][0]]), []]]] if ((shen_eq([], KL_ARG_V1072_1079[1][1]) if shen_consp(KL_ARG_V1072_1079[1]) else False) if shen_consp(KL_ARG_V1072_1079) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_clause_form]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.clause_form', shen_clause_form)

@tail_recursion
def shen_explicit_modes(KL_ARG_V1073_1080):
    global symdic
    return ([KL_ARG_V1073_1080[0], tco_apply(kl_map, [symdic.symdic_shen_em_help, KL_ARG_V1073_1080[1]])] if shen_consp(KL_ARG_V1073_1080) else (tail_call(shen_sysx45error, [symdic.symdic_shen_explicit_modes]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.explicit_modes', shen_explicit_modes)

@tail_recursion
def shen_em_help(KL_ARG_V1074_1081):
    global symdic
    return (KL_ARG_V1074_1081 if ((((shen_eq([], KL_ARG_V1074_1081[1][1][1]) if shen_consp(KL_ARG_V1074_1081[1][1]) else False) if shen_consp(KL_ARG_V1074_1081[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1074_1081[0]) else False) if shen_consp(KL_ARG_V1074_1081) else False) else ([symdic.symdic_kl_mode, [KL_ARG_V1074_1081, [symdic.symdic_kl_x43, []]]] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.em_help', shen_em_help)

@tail_recursion
def shen_cf_help(KL_ARG_V1075_1082):
    global symdic
    return ([[(symdic.symdic_kl_unifyx33 if shen_get(symdic.symdic_shen_x42occursx42) else symdic.symdic_kl_unify), KL_ARG_V1075_1082[1][0][1]], tco_apply(shen_cf_help, [KL_ARG_V1075_1082[1][1][0]])] if (((((((((shen_eq([], KL_ARG_V1075_1082[1][1][1]) if shen_consp(KL_ARG_V1075_1082[1][1]) else False) if shen_eq([], KL_ARG_V1075_1082[1][0][1][1][1]) else False) if shen_consp(KL_ARG_V1075_1082[1][0][1][1]) else False) if shen_consp(KL_ARG_V1075_1082[1][0][1]) else False) if shen_eq(symdic.symdic_kl_x61, KL_ARG_V1075_1082[1][0][0]) else False) if shen_consp(KL_ARG_V1075_1082[1][0]) else False) if shen_consp(KL_ARG_V1075_1082[1]) else False) if shen_eq(symdic.symdic_kl_where, KL_ARG_V1075_1082[0]) else False) if shen_consp(KL_ARG_V1075_1082) else False) else (KL_ARG_V1075_1082 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.cf_help', shen_cf_help)

@tail_recursion
def kl_occursx45check(KL_ARG_V1080_1083):
    global symdic
    return (shen_set(symdic.symdic_shen_x42occursx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1080_1083) else (shen_set(symdic.symdic_shen_x42occursx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1080_1083) else (shen_simple_error('occurs-check expects + or -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('occurs-check', kl_occursx45check)

@tail_recursion
def shen_aum(KL_ARG_V1081_1084, KL_ARG_V1082_1085):

    class KL_Context:
        KL_LOC_MuApplication_1086 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_MuApplication_1086', tco_apply(shen_make_mu_application, [[symdic.symdic_shen_mu, [KL_ARG_V1081_1084[0][1], [tco_apply(shen_continuation_call, [KL_ARG_V1081_1084[0][1], KL_ARG_V1081_1084[1][1][0]]), []]]], KL_ARG_V1082_1085])), tail_call(shen_mu_reduction, [KL_CTX.KL_LOC_MuApplication_1086, symdic.symdic_kl_x43])][(-1)] if (((((shen_eq([], KL_ARG_V1081_1084[1][1][1]) if shen_consp(KL_ARG_V1081_1084[1][1]) else False) if shen_eq(symdic.symdic_kl_x58x45, KL_ARG_V1081_1084[1][0]) else False) if shen_consp(KL_ARG_V1081_1084[1]) else False) if shen_consp(KL_ARG_V1081_1084[0]) else False) if shen_consp(KL_ARG_V1081_1084) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_aum]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.aum', shen_aum)

@tail_recursion
def shen_continuation_call(KL_ARG_V1083_1087, KL_ARG_V1084_1088):

    class KL_Context:
        KL_LOC_VTerms_1089 = None
        KL_LOC_VBody_1090 = None
        KL_LOC_Free_1091 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_VTerms_1089', [symdic.symdic_ProcessN, tco_apply(shen_extract_vars, [KL_ARG_V1083_1087])]), [setattr(KL_CTX, 'KL_LOC_VBody_1090', tco_apply(shen_extract_vars, [KL_ARG_V1084_1088])), [setattr(KL_CTX, 'KL_LOC_Free_1091', tco_apply(kl_remove, [symdic.symdic_Throwcontrol, tco_apply(kl_difference, [KL_CTX.KL_LOC_VBody_1090, KL_CTX.KL_LOC_VTerms_1089])])), tail_call(shen_cc_help, [KL_CTX.KL_LOC_Free_1091, KL_ARG_V1084_1088])][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.continuation_call', shen_continuation_call)

@tail_recursion
def kl_remove(KL_ARG_V1085_1092, KL_ARG_V1086_1093):
    global symdic
    return tail_call(shen_removex45h, [KL_ARG_V1085_1092, KL_ARG_V1086_1093, []])
shen_add_fun('remove', kl_remove)

@tail_recursion
def shen_removex45h(KL_ARG_V1089_1094, KL_ARG_V1090_1095, KL_ARG_V1091_1096):
    global symdic
    return (tail_call(kl_reverse, [KL_ARG_V1091_1096]) if shen_eq([], KL_ARG_V1090_1095) else (tail_call(shen_removex45h, [KL_ARG_V1090_1095[0], KL_ARG_V1090_1095[1], KL_ARG_V1091_1096]) if (shen_eq(KL_ARG_V1090_1095[0], KL_ARG_V1089_1094) if shen_consp(KL_ARG_V1090_1095) else False) else (tail_call(shen_removex45h, [KL_ARG_V1089_1094, KL_ARG_V1090_1095[1], [KL_ARG_V1090_1095[0], KL_ARG_V1091_1096]]) if shen_consp(KL_ARG_V1090_1095) else (tail_call(shen_sysx45error, [symdic.symdic_shen_removex45h]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove-h', shen_removex45h)

@tail_recursion
def shen_cc_help(KL_ARG_V1093_1097, KL_ARG_V1094_1098):
    global symdic
    return ([symdic.symdic_shen_pop, [symdic.symdic_shen_the, [symdic.symdic_shen_stack, []]]] if (shen_eq([], KL_ARG_V1094_1098) if shen_eq([], KL_ARG_V1093_1097) else False) else ([symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1093_1097, [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_shen_pop, [symdic.symdic_shen_the, [symdic.symdic_shen_stack, []]]], []]]]]]]]] if shen_eq([], KL_ARG_V1094_1098) else ([symdic.symdic_kl_call, [symdic.symdic_shen_the, [symdic.symdic_shen_continuation, [KL_ARG_V1094_1098, []]]]] if shen_eq([], KL_ARG_V1093_1097) else ([symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1093_1097, [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_kl_call, [symdic.symdic_shen_the, [symdic.symdic_shen_continuation, [KL_ARG_V1094_1098, []]]]], []]]]]]]]] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.cc_help', shen_cc_help)

@tail_recursion
def shen_make_mu_application(KL_ARG_V1095_1099, KL_ARG_V1096_1100):
    global symdic
    return (KL_ARG_V1095_1099[1][1][0] if ((((((shen_eq([], KL_ARG_V1096_1100) if shen_eq([], KL_ARG_V1095_1099[1][1][1]) else False) if shen_consp(KL_ARG_V1095_1099[1][1]) else False) if shen_eq([], KL_ARG_V1095_1099[1][0]) else False) if shen_consp(KL_ARG_V1095_1099[1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1095_1099[0]) else False) if shen_consp(KL_ARG_V1095_1099) else False) else ([[symdic.symdic_shen_mu, [KL_ARG_V1095_1099[1][0][0], [tco_apply(shen_make_mu_application, [[symdic.symdic_shen_mu, [KL_ARG_V1095_1099[1][0][1], KL_ARG_V1095_1099[1][1]]], KL_ARG_V1096_1100[1]]), []]]], [KL_ARG_V1096_1100[0], []]] if ((((((shen_consp(KL_ARG_V1096_1100) if shen_eq([], KL_ARG_V1095_1099[1][1][1]) else False) if shen_consp(KL_ARG_V1095_1099[1][1]) else False) if shen_consp(KL_ARG_V1095_1099[1][0]) else False) if shen_consp(KL_ARG_V1095_1099[1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1095_1099[0]) else False) if shen_consp(KL_ARG_V1095_1099) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_make_mu_application]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.make_mu_application', shen_make_mu_application)

@tail_recursion
def shen_mu_reduction(KL_ARG_V1103_1101, KL_ARG_V1104_1102):

    class KL_Context:
        KL_LOC_Z_1103 = None
        KL_LOC_Z_1104 = None
        KL_LOC_Z_1105 = None
        KL_LOC_Z_1106 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1103_1101[0][1][0][1][0], KL_ARG_V1103_1101[0][1][1]]], KL_ARG_V1103_1101[1]], KL_ARG_V1103_1101[0][1][0][1][1][0]]) if ((((((((((((shen_eq([], KL_ARG_V1103_1101[1][1]) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][0][1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1103_1101[0][1][0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][0]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else (tail_call(shen_mu_reduction, [KL_ARG_V1103_1101[0][1][1][0], KL_ARG_V1104_1102]) if ((((((((shen_eq(symdic.symdic_kl__, KL_ARG_V1103_1101[0][1][0]) if shen_eq([], KL_ARG_V1103_1101[1][1]) else False) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else (tail_call(kl_subst, [KL_ARG_V1103_1101[1][0], KL_ARG_V1103_1101[0][1][0], tco_apply(shen_mu_reduction, [KL_ARG_V1103_1101[0][1][1][0], KL_ARG_V1104_1102])]) if ((((((((tco_apply(shen_ephemeral_variablex63, [KL_ARG_V1103_1101[0][1][0], KL_ARG_V1103_1101[1][0]]) if shen_eq([], KL_ARG_V1103_1101[1][1]) else False) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([symdic.symdic_kl_let, [KL_ARG_V1103_1101[0][1][0], [symdic.symdic_shen_be, [KL_ARG_V1103_1101[1][0], [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1103_1101[0][1][1][0], KL_ARG_V1104_1102]), []]]]]]] if ((((((((tco_apply(kl_variablex63, [KL_ARG_V1103_1101[0][1][0]]) if shen_eq([], KL_ARG_V1103_1101[1][1]) else False) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1103', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1103, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1103_1101[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1103, [symdic.symdic_kl_is, [symdic.symdic_kl_identical, [symdic.symdic_shen_to, [KL_ARG_V1103_1101[0][1][0], []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [KL_ARG_V1103_1101[0][1][1][0], symdic.symdic_kl_x45]), [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]]][(-1)] if (((((((((tco_apply(shen_prolog_constantx63, [KL_ARG_V1103_1101[0][1][0]]) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1104_1102) else False) if shen_eq([], KL_ARG_V1103_1101[1][1]) else False) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1104', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1104, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1103_1101[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1104, [symdic.symdic_kl_is, [symdic.symdic_kl_identical, [symdic.symdic_shen_to, [KL_ARG_V1103_1101[0][1][0], []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [KL_ARG_V1103_1101[0][1][1][0], symdic.symdic_kl_x43]), [symdic.symdic_shen_else, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1104, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_variable, []]]]], [symdic.symdic_shen_then, [[symdic.symdic_kl_bind, [KL_CTX.KL_LOC_Z_1104, [symdic.symdic_shen_to, [KL_ARG_V1103_1101[0][1][0], [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1103_1101[0][1][1][0], symdic.symdic_kl_x43]), []]]]]]], [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]], []]]]]]]][(-1)] if (((((((((tco_apply(shen_prolog_constantx63, [KL_ARG_V1103_1101[0][1][0]]) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1104_1102) else False) if shen_eq([], KL_ARG_V1103_1101[1][1]) else False) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1105', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1105, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1103_1101[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1105, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_nonx45empty, [symdic.symdic_kl_list, []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1103_1101[0][1][0][0], [[[symdic.symdic_shen_mu, [KL_ARG_V1103_1101[0][1][0][1], KL_ARG_V1103_1101[0][1][1]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_tail, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1105, []]]]], []]], []]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_head, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1105, []]]]], []]], symdic.symdic_kl_x45]), [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]]][(-1)] if (((((((((shen_eq(symdic.symdic_kl_x45, KL_ARG_V1104_1102) if shen_eq([], KL_ARG_V1103_1101[1][1]) else False) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][0]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else ([setattr(KL_CTX, 'KL_LOC_Z_1106', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_let, [KL_CTX.KL_LOC_Z_1106, [symdic.symdic_shen_be, [[symdic.symdic_shen_the, [symdic.symdic_shen_result, [symdic.symdic_shen_of, [symdic.symdic_shen_dereferencing, KL_ARG_V1103_1101[1]]]]], [symdic.symdic_kl_in, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1106, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_nonx45empty, [symdic.symdic_kl_list, []]]]]], [symdic.symdic_shen_then, [tco_apply(shen_mu_reduction, [[[symdic.symdic_shen_mu, [KL_ARG_V1103_1101[0][1][0][0], [[[symdic.symdic_shen_mu, [KL_ARG_V1103_1101[0][1][0][1], KL_ARG_V1103_1101[0][1][1]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_tail, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1106, []]]]], []]], []]]], [[symdic.symdic_shen_the, [symdic.symdic_kl_head, [symdic.symdic_shen_of, [KL_CTX.KL_LOC_Z_1106, []]]]], []]], symdic.symdic_kl_x43]), [symdic.symdic_shen_else, [[symdic.symdic_kl_if, [[KL_CTX.KL_LOC_Z_1106, [symdic.symdic_kl_is, [symdic.symdic_shen_a, [symdic.symdic_shen_variable, []]]]], [symdic.symdic_shen_then, [[symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [tco_apply(shen_extract_vars, [KL_ARG_V1103_1101[0][1][0]]), [symdic.symdic_kl_and, [symdic.symdic_shen_then, [[symdic.symdic_kl_bind, [KL_CTX.KL_LOC_Z_1106, [symdic.symdic_shen_to, [tco_apply(shen_rcons_form, [tco_apply(shen_remove_modes, [KL_ARG_V1103_1101[0][1][0]])]), [symdic.symdic_kl_in, [tco_apply(shen_mu_reduction, [KL_ARG_V1103_1101[0][1][1][0], symdic.symdic_kl_x43]), []]]]]]], []]]]]]]]], [symdic.symdic_shen_else, [symdic.symdic_shen_failedx33, []]]]]]], []]]]]]], []]]]]]]][(-1)] if (((((((((shen_eq(symdic.symdic_kl_x43, KL_ARG_V1104_1102) if shen_eq([], KL_ARG_V1103_1101[1][1]) else False) if shen_consp(KL_ARG_V1103_1101[1]) else False) if shen_eq([], KL_ARG_V1103_1101[0][1][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][1]) else False) if shen_consp(KL_ARG_V1103_1101[0][1][0]) else False) if shen_consp(KL_ARG_V1103_1101[0][1]) else False) if shen_eq(symdic.symdic_shen_mu, KL_ARG_V1103_1101[0][0]) else False) if shen_consp(KL_ARG_V1103_1101[0]) else False) if shen_consp(KL_ARG_V1103_1101) else False) else (KL_ARG_V1103_1101 if True else shen_simple_error('condition failure'))))))))))
shen_add_fun('shen.mu_reduction', shen_mu_reduction)

@tail_recursion
def shen_rcons_form(KL_ARG_V1105_1107):
    global symdic
    return ([symdic.symdic_kl_cons, [tco_apply(shen_rcons_form, [KL_ARG_V1105_1107[0]]), [tco_apply(shen_rcons_form, [KL_ARG_V1105_1107[1]]), []]]] if shen_consp(KL_ARG_V1105_1107) else (KL_ARG_V1105_1107 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.rcons_form', shen_rcons_form)

@tail_recursion
def shen_remove_modes(KL_ARG_V1106_1108):
    global symdic
    return (tail_call(shen_remove_modes, [KL_ARG_V1106_1108[1][0]]) if (((((shen_eq([], KL_ARG_V1106_1108[1][1][1]) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V1106_1108[1][1][0]) else False) if shen_consp(KL_ARG_V1106_1108[1][1]) else False) if shen_consp(KL_ARG_V1106_1108[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1106_1108[0]) else False) if shen_consp(KL_ARG_V1106_1108) else False) else (tail_call(shen_remove_modes, [KL_ARG_V1106_1108[1][0]]) if (((((shen_eq([], KL_ARG_V1106_1108[1][1][1]) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V1106_1108[1][1][0]) else False) if shen_consp(KL_ARG_V1106_1108[1][1]) else False) if shen_consp(KL_ARG_V1106_1108[1]) else False) if shen_eq(symdic.symdic_kl_mode, KL_ARG_V1106_1108[0]) else False) if shen_consp(KL_ARG_V1106_1108) else False) else ([tco_apply(shen_remove_modes, [KL_ARG_V1106_1108[0]]), tco_apply(shen_remove_modes, [KL_ARG_V1106_1108[1]])] if shen_consp(KL_ARG_V1106_1108) else (KL_ARG_V1106_1108 if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.remove_modes', shen_remove_modes)

@tail_recursion
def shen_ephemeral_variablex63(KL_ARG_V1107_1109, KL_ARG_V1108_1110):
    global symdic
    return (tail_call(kl_variablex63, [KL_ARG_V1108_1110]) if tco_apply(kl_variablex63, [KL_ARG_V1107_1109]) else False)
shen_add_fun('shen.ephemeral_variable?', shen_ephemeral_variablex63)

@tail_recursion
def shen_prolog_constantx63(KL_ARG_V1117_1111):
    global symdic
    return (False if shen_consp(KL_ARG_V1117_1111) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog_constant?', shen_prolog_constantx63)

@tail_recursion
def shen_aum_to_shen(KL_ARG_V1118_1112):
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V1118_1112[1][0], [tco_apply(shen_aum_to_shen, [KL_ARG_V1118_1112[1][1][1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1118_1112[1][1][1][1][1][0]]), []]]]] if (((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_in, KL_ARG_V1118_1112[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_be, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_kl_let, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_shen_lazyderef, [tco_apply(shen_aum_to_shen, [KL_ARG_V1118_1112[1][1][1][1][0]]), [symdic.symdic_ProcessN, []]]] if (((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_eq(symdic.symdic_shen_dereferencing, KL_ARG_V1118_1112[1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_of, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_shen_result, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_shen_the, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_if, [tco_apply(shen_aum_to_shen, [KL_ARG_V1118_1112[1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1118_1112[1][1][1][0]]), [tco_apply(shen_aum_to_shen, [KL_ARG_V1118_1112[1][1][1][1][1][0]]), []]]]] if (((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1]) else False) if shen_eq(symdic.symdic_shen_else, KL_ARG_V1118_1112[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_then, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_kl_if, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_shen_pvarx63, [KL_ARG_V1118_1112[0], []]] if (((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1]) if shen_eq(symdic.symdic_shen_variable, KL_ARG_V1118_1112[1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_a, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_kl_is, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_consx63, [KL_ARG_V1118_1112[0], []]] if (((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1]) if shen_eq(symdic.symdic_kl_list, KL_ARG_V1118_1112[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_eq(symdic.symdic_shen_nonx45empty, KL_ARG_V1118_1112[1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_a, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_kl_is, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (tail_call(shen_aum_to_shen, [KL_ARG_V1118_1112[1][1][1][1][1][1][1][0]]) if (((((((((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1][1][1]) else False) if shen_eq(symdic.symdic_shen_then, KL_ARG_V1118_1112[1][1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_and, KL_ARG_V1118_1112[1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1]) else False) if shen_eq([], KL_ARG_V1118_1112[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_in, KL_ARG_V1118_1112[1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_variables, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_shen_the, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_shen_rename, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_let, [KL_ARG_V1118_1112[1][1][1][1][0][0], [[symdic.symdic_shen_newpv, [symdic.symdic_ProcessN, []]], [tco_apply(shen_aum_to_shen, [[symdic.symdic_shen_rename, [symdic.symdic_shen_the, [symdic.symdic_shen_variables, [symdic.symdic_kl_in, [KL_ARG_V1118_1112[1][1][1][1][0][1], KL_ARG_V1118_1112[1][1][1][1][1]]]]]]]), []]]]] if (((((((((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1][1][1]) else False) if shen_eq(symdic.symdic_shen_then, KL_ARG_V1118_1112[1][1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_and, KL_ARG_V1118_1112[1][1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_in, KL_ARG_V1118_1112[1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_variables, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_shen_the, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_shen_rename, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_bindv, [KL_ARG_V1118_1112[1][0], [tco_apply(shen_chwild, [KL_ARG_V1118_1112[1][1][1][0]]), [symdic.symdic_ProcessN, []]]]], [[symdic.symdic_kl_let, [symdic.symdic_Result, [tco_apply(shen_aum_to_shen, [KL_ARG_V1118_1112[1][1][1][1][1][0]]), [[symdic.symdic_kl_do, [[symdic.symdic_shen_unbindv, [KL_ARG_V1118_1112[1][0], [symdic.symdic_ProcessN, []]]], [symdic.symdic_Result, []]]], []]]]], []]]] if (((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_in, KL_ARG_V1118_1112[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_to, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_kl_bind, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_x61, [KL_ARG_V1118_1112[1][1][1][1][0], [KL_ARG_V1118_1112[0], []]]] if ((((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1][1]) else False) if shen_eq(symdic.symdic_shen_to, KL_ARG_V1118_1112[1][1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_kl_identical, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_kl_is, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (False if shen_eq(symdic.symdic_shen_failedx33, KL_ARG_V1118_1112) else ([symdic.symdic_kl_hd, KL_ARG_V1118_1112[1][1][1]] if (((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_of, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_kl_head, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_shen_the, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_tl, KL_ARG_V1118_1112[1][1][1]] if (((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_of, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_kl_tail, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_shen_the, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_incinfs, []], [[symdic.symdic_kl_thaw, [symdic.symdic_Continuation, []]], []]]] if ((((((shen_eq([], KL_ARG_V1118_1112[1][1][1]) if shen_eq(symdic.symdic_shen_stack, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_shen_the, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_shen_pop, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else ([symdic.symdic_kl_do, [[symdic.symdic_shen_incinfs, []], [tco_apply(shen_call_the_continuation, [tco_apply(shen_chwild, [KL_ARG_V1118_1112[1][1][1][0]]), symdic.symdic_ProcessN, symdic.symdic_Continuation]), []]]] if (((((((shen_eq([], KL_ARG_V1118_1112[1][1][1][1]) if shen_consp(KL_ARG_V1118_1112[1][1][1]) else False) if shen_eq(symdic.symdic_shen_continuation, KL_ARG_V1118_1112[1][1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1][1]) else False) if shen_eq(symdic.symdic_shen_the, KL_ARG_V1118_1112[1][0]) else False) if shen_consp(KL_ARG_V1118_1112[1]) else False) if shen_eq(symdic.symdic_kl_call, KL_ARG_V1118_1112[0]) else False) if shen_consp(KL_ARG_V1118_1112) else False) else (KL_ARG_V1118_1112 if True else shen_simple_error('condition failure'))))))))))))))))
shen_add_fun('shen.aum_to_shen', shen_aum_to_shen)

@tail_recursion
def shen_chwild(KL_ARG_V1119_1113):
    global symdic
    return ([symdic.symdic_shen_newpv, [symdic.symdic_ProcessN, []]] if shen_eq(KL_ARG_V1119_1113, symdic.symdic_kl__) else (tail_call(kl_map, [symdic.symdic_shen_chwild, KL_ARG_V1119_1113]) if shen_consp(KL_ARG_V1119_1113) else (KL_ARG_V1119_1113 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.chwild', shen_chwild)

@tail_recursion
def shen_newpv(KL_ARG_V1120_1114):

    class KL_Context:
        KL_LOC_Countx431_1115 = None
        KL_LOC_IncVar_1116 = None
        KL_LOC_Vector_1117 = None
        KL_LOC_ResizeVectorIfNeeded_1118 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Countx431_1115', (shen_absvector_get(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1120_1114) + 1)), [setattr(KL_CTX, 'KL_LOC_IncVar_1116', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1120_1114, KL_CTX.KL_LOC_Countx431_1115)), [setattr(KL_CTX, 'KL_LOC_Vector_1117', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1120_1114)), [setattr(KL_CTX, 'KL_LOC_ResizeVectorIfNeeded_1118', (tco_apply(shen_resizeprocessvector, [KL_ARG_V1120_1114, KL_CTX.KL_LOC_Countx431_1115]) if shen_eq(KL_CTX.KL_LOC_Countx431_1115, tco_apply(kl_limit, [KL_CTX.KL_LOC_Vector_1117])) else symdic.symdic_shen_skip)), tail_call(shen_mkx45pvar, [KL_CTX.KL_LOC_Countx431_1115])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.newpv', shen_newpv)

@tail_recursion
def shen_resizeprocessvector(KL_ARG_V1121_1119, KL_ARG_V1122_1120):

    class KL_Context:
        KL_LOC_Vector_1121 = None
        KL_LOC_BigVector_1122 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1121', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1121_1119)), [setattr(KL_CTX, 'KL_LOC_BigVector_1122', tco_apply(shen_resizex45vector, [KL_CTX.KL_LOC_Vector_1121, (KL_ARG_V1122_1120 + KL_ARG_V1122_1120), symdic.symdic_shen_x45nullx45])), shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1121_1119, KL_CTX.KL_LOC_BigVector_1122)][(-1)]][(-1)]
shen_add_fun('shen.resizeprocessvector', shen_resizeprocessvector)

@tail_recursion
def shen_resizex45vector(KL_ARG_V1123_1123, KL_ARG_V1124_1124, KL_ARG_V1125_1125):

    class KL_Context:
        KL_LOC_BigVector_1126 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_BigVector_1126', shen_absvector_set(shen_absvector((1 + KL_ARG_V1124_1124)), 0, KL_ARG_V1124_1124)), tail_call(shen_copyx45vector, [KL_ARG_V1123_1123, KL_CTX.KL_LOC_BigVector_1126, tco_apply(kl_limit, [KL_ARG_V1123_1123]), KL_ARG_V1124_1124, KL_ARG_V1125_1125])][(-1)]
shen_add_fun('shen.resize-vector', shen_resizex45vector)

@tail_recursion
def shen_copyx45vector(KL_ARG_V1126_1127, KL_ARG_V1127_1128, KL_ARG_V1128_1129, KL_ARG_V1129_1130, KL_ARG_V1130_1131):
    global symdic
    return tail_call(shen_copyx45vectorx45stagex452, [(1 + KL_ARG_V1128_1129), (KL_ARG_V1129_1130 + 1), KL_ARG_V1130_1131, tco_apply(shen_copyx45vectorx45stagex451, [1, KL_ARG_V1126_1127, KL_ARG_V1127_1128, (1 + KL_ARG_V1128_1129)])])
shen_add_fun('shen.copy-vector', shen_copyx45vector)

@tail_recursion
def shen_copyx45vectorx45stagex451(KL_ARG_V1133_1132, KL_ARG_V1134_1133, KL_ARG_V1135_1134, KL_ARG_V1136_1135):
    global symdic
    return (KL_ARG_V1135_1134 if shen_eq(KL_ARG_V1136_1135, KL_ARG_V1133_1132) else (tail_call(shen_copyx45vectorx45stagex451, [(1 + KL_ARG_V1133_1132), KL_ARG_V1134_1133, shen_absvector_set(KL_ARG_V1135_1134, KL_ARG_V1133_1132, shen_absvector_get(KL_ARG_V1134_1133, KL_ARG_V1133_1132)), KL_ARG_V1136_1135]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-1', shen_copyx45vectorx45stagex451)

@tail_recursion
def shen_copyx45vectorx45stagex452(KL_ARG_V1140_1136, KL_ARG_V1141_1137, KL_ARG_V1142_1138, KL_ARG_V1143_1139):
    global symdic
    return (KL_ARG_V1143_1139 if shen_eq(KL_ARG_V1141_1137, KL_ARG_V1140_1136) else (tail_call(shen_copyx45vectorx45stagex452, [(KL_ARG_V1140_1136 + 1), KL_ARG_V1141_1137, KL_ARG_V1142_1138, shen_absvector_set(KL_ARG_V1143_1139, KL_ARG_V1140_1136, KL_ARG_V1142_1138)]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.copy-vector-stage-2', shen_copyx45vectorx45stagex452)

@tail_recursion
def shen_mkx45pvar(KL_ARG_V1145_1140):
    global symdic
    return shen_absvector_set(shen_absvector_set(shen_absvector(2), 0, symdic.symdic_shen_pvar), 1, KL_ARG_V1145_1140)
shen_add_fun('shen.mk-pvar', shen_mkx45pvar)

@tail_recursion
def shen_pvarx63(KL_ARG_V1146_1141):
    global symdic
    return (shen_eq(shen_absvector_get(KL_ARG_V1146_1141, 0), symdic.symdic_shen_pvar) if shen_absvectorp(KL_ARG_V1146_1141) else False)
shen_add_fun('shen.pvar?', shen_pvarx63)

@tail_recursion
def shen_bindv(KL_ARG_V1147_1142, KL_ARG_V1148_1143, KL_ARG_V1149_1144):

    class KL_Context:
        KL_LOC_Vector_1145 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1145', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1149_1144)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1145, shen_absvector_get(KL_ARG_V1147_1142, 1), KL_ARG_V1148_1143)][(-1)]
shen_add_fun('shen.bindv', shen_bindv)

@tail_recursion
def shen_unbindv(KL_ARG_V1150_1146, KL_ARG_V1151_1147):

    class KL_Context:
        KL_LOC_Vector_1148 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1148', shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1151_1147)), shen_absvector_set(KL_CTX.KL_LOC_Vector_1148, shen_absvector_get(KL_ARG_V1150_1146, 1), symdic.symdic_shen_x45nullx45)][(-1)]
shen_add_fun('shen.unbindv', shen_unbindv)

@tail_recursion
def shen_incinfs():
    global symdic
    return shen_set(symdic.symdic_shen_x42infsx42, (1 + shen_get(symdic.symdic_shen_x42infsx42)))
shen_add_fun('shen.incinfs', shen_incinfs)

@tail_recursion
def shen_call_the_continuation(KL_ARG_V1152_1149, KL_ARG_V1153_1150, KL_ARG_V1154_1151):

    class KL_Context:
        KL_LOC_NewContinuation_1152 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V1152_1149[0][0], tco_apply(kl_append, [KL_ARG_V1152_1149[0][1], [KL_ARG_V1153_1150, [KL_ARG_V1154_1151, []]]])] if ((shen_eq([], KL_ARG_V1152_1149[1]) if shen_consp(KL_ARG_V1152_1149[0]) else False) if shen_consp(KL_ARG_V1152_1149) else False) else ([setattr(KL_CTX, 'KL_LOC_NewContinuation_1152', tco_apply(shen_newcontinuation, [KL_ARG_V1152_1149[1], KL_ARG_V1153_1150, KL_ARG_V1154_1151])), [KL_ARG_V1152_1149[0][0], tco_apply(kl_append, [KL_ARG_V1152_1149[0][1], [KL_ARG_V1153_1150, [KL_CTX.KL_LOC_NewContinuation_1152, []]]])]][(-1)] if (shen_consp(KL_ARG_V1152_1149[0]) if shen_consp(KL_ARG_V1152_1149) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_call_the_continuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call_the_continuation', shen_call_the_continuation)

@tail_recursion
def shen_newcontinuation(KL_ARG_V1155_1153, KL_ARG_V1156_1154, KL_ARG_V1157_1155):
    global symdic
    return (KL_ARG_V1157_1155 if shen_eq([], KL_ARG_V1155_1153) else ([symdic.symdic_kl_freeze, [[KL_ARG_V1155_1153[0][0], tco_apply(kl_append, [KL_ARG_V1155_1153[0][1], [KL_ARG_V1156_1154, [tco_apply(shen_newcontinuation, [KL_ARG_V1155_1153[1], KL_ARG_V1156_1154, KL_ARG_V1157_1155]), []]]])], []]] if (shen_consp(KL_ARG_V1155_1153[0]) if shen_consp(KL_ARG_V1155_1153) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_newcontinuation]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.newcontinuation', shen_newcontinuation)

@tail_recursion
def kl_return(KL_ARG_V1162_1156, KL_ARG_V1163_1157, KL_ARG_V1164_1158):
    global symdic
    return tail_call(shen_deref, [KL_ARG_V1162_1156, KL_ARG_V1163_1157])
shen_add_fun('return', kl_return)

@tail_recursion
def shen_measurex38return(KL_ARG_V1169_1159, KL_ARG_V1170_1160, KL_ARG_V1171_1161):
    global symdic
    return [tco_apply(shen_prhush, [tco_apply(shen_app, [shen_get(symdic.symdic_shen_x42infsx42), ' inferences\r\n', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), tail_call(shen_deref, [KL_ARG_V1169_1159, KL_ARG_V1170_1160])][(-1)]
shen_add_fun('shen.measure&return', shen_measurex38return)

@tail_recursion
def kl_unify(KL_ARG_V1172_1162, KL_ARG_V1173_1163, KL_ARG_V1174_1164, KL_ARG_V1175_1165):
    global symdic
    return tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1172_1162, KL_ARG_V1174_1164]), tco_apply(shen_lazyderef, [KL_ARG_V1173_1163, KL_ARG_V1174_1164]), KL_ARG_V1174_1164, KL_ARG_V1175_1165])
shen_add_fun('unify', kl_unify)

@tail_recursion
def shen_lzyx61(KL_ARG_V1192_1166, KL_ARG_V1193_1167, KL_ARG_V1194_1168, KL_ARG_V1195_1169):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1195_1169]) if shen_eq(KL_ARG_V1193_1167, KL_ARG_V1192_1166) else (tail_call(kl_bind, [KL_ARG_V1192_1166, KL_ARG_V1193_1167, KL_ARG_V1194_1168, KL_ARG_V1195_1169]) if tco_apply(shen_pvarx63, [KL_ARG_V1192_1166]) else (tail_call(kl_bind, [KL_ARG_V1193_1167, KL_ARG_V1192_1166, KL_ARG_V1194_1168, KL_ARG_V1195_1169]) if tco_apply(shen_pvarx63, [KL_ARG_V1193_1167]) else (tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1192_1166[0], KL_ARG_V1194_1168]), tco_apply(shen_lazyderef, [KL_ARG_V1193_1167[0], KL_ARG_V1194_1168]), KL_ARG_V1194_1168, (lambda : tail_call(shen_lzyx61, [tco_apply(shen_lazyderef, [KL_ARG_V1192_1166[1], KL_ARG_V1194_1168]), tco_apply(shen_lazyderef, [KL_ARG_V1193_1167[1], KL_ARG_V1194_1168]), KL_ARG_V1194_1168, KL_ARG_V1195_1169]))]) if (shen_consp(KL_ARG_V1193_1167) if shen_consp(KL_ARG_V1192_1166) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=', shen_lzyx61)

@tail_recursion
def shen_deref(KL_ARG_V1197_1170, KL_ARG_V1198_1171):

    class KL_Context:
        KL_LOC_Value_1172 = None
    KL_CTX = KL_Context()
    global symdic
    return ([tco_apply(shen_deref, [KL_ARG_V1197_1170[0], KL_ARG_V1198_1171]), tco_apply(shen_deref, [KL_ARG_V1197_1170[1], KL_ARG_V1198_1171])] if shen_consp(KL_ARG_V1197_1170) else (([setattr(KL_CTX, 'KL_LOC_Value_1172', tco_apply(shen_valvector, [KL_ARG_V1197_1170, KL_ARG_V1198_1171])), (KL_ARG_V1197_1170 if shen_eq(KL_CTX.KL_LOC_Value_1172, symdic.symdic_shen_x45nullx45) else tail_call(shen_deref, [KL_CTX.KL_LOC_Value_1172, KL_ARG_V1198_1171]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1197_1170]) else KL_ARG_V1197_1170) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.deref', shen_deref)

@tail_recursion
def shen_lazyderef(KL_ARG_V1199_1173, KL_ARG_V1200_1174):

    class KL_Context:
        KL_LOC_Value_1175 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Value_1175', tco_apply(shen_valvector, [KL_ARG_V1199_1173, KL_ARG_V1200_1174])), (KL_ARG_V1199_1173 if shen_eq(KL_CTX.KL_LOC_Value_1175, symdic.symdic_shen_x45nullx45) else tail_call(shen_lazyderef, [KL_CTX.KL_LOC_Value_1175, KL_ARG_V1200_1174]))][(-1)] if tco_apply(shen_pvarx63, [KL_ARG_V1199_1173]) else KL_ARG_V1199_1173)
shen_add_fun('shen.lazyderef', shen_lazyderef)

@tail_recursion
def shen_valvector(KL_ARG_V1201_1176, KL_ARG_V1202_1177):
    global symdic
    return shen_absvector_get(shen_absvector_get(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1202_1177), shen_absvector_get(KL_ARG_V1201_1176, 1))
shen_add_fun('shen.valvector', shen_valvector)

@tail_recursion
def kl_unifyx33(KL_ARG_V1203_1178, KL_ARG_V1204_1179, KL_ARG_V1205_1180, KL_ARG_V1206_1181):
    global symdic
    return tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1203_1178, KL_ARG_V1205_1180]), tco_apply(shen_lazyderef, [KL_ARG_V1204_1179, KL_ARG_V1205_1180]), KL_ARG_V1205_1180, KL_ARG_V1206_1181])
shen_add_fun('unify!', kl_unifyx33)

@tail_recursion
def shen_lzyx61x33(KL_ARG_V1223_1182, KL_ARG_V1224_1183, KL_ARG_V1225_1184, KL_ARG_V1226_1185):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1226_1185]) if shen_eq(KL_ARG_V1224_1183, KL_ARG_V1223_1182) else (tail_call(kl_bind, [KL_ARG_V1223_1182, KL_ARG_V1224_1183, KL_ARG_V1225_1184, KL_ARG_V1226_1185]) if ((not tco_apply(shen_occursx63, [KL_ARG_V1223_1182, tco_apply(shen_deref, [KL_ARG_V1224_1183, KL_ARG_V1225_1184])])) if tco_apply(shen_pvarx63, [KL_ARG_V1223_1182]) else False) else (tail_call(kl_bind, [KL_ARG_V1224_1183, KL_ARG_V1223_1182, KL_ARG_V1225_1184, KL_ARG_V1226_1185]) if ((not tco_apply(shen_occursx63, [KL_ARG_V1224_1183, tco_apply(shen_deref, [KL_ARG_V1223_1182, KL_ARG_V1225_1184])])) if tco_apply(shen_pvarx63, [KL_ARG_V1224_1183]) else False) else (tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1223_1182[0], KL_ARG_V1225_1184]), tco_apply(shen_lazyderef, [KL_ARG_V1224_1183[0], KL_ARG_V1225_1184]), KL_ARG_V1225_1184, (lambda : tail_call(shen_lzyx61x33, [tco_apply(shen_lazyderef, [KL_ARG_V1223_1182[1], KL_ARG_V1225_1184]), tco_apply(shen_lazyderef, [KL_ARG_V1224_1183[1], KL_ARG_V1225_1184]), KL_ARG_V1225_1184, KL_ARG_V1226_1185]))]) if (shen_consp(KL_ARG_V1224_1183) if shen_consp(KL_ARG_V1223_1182) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.lzy=!', shen_lzyx61x33)

@tail_recursion
def shen_occursx63(KL_ARG_V1236_1186, KL_ARG_V1237_1187):
    global symdic
    return (True if shen_eq(KL_ARG_V1237_1187, KL_ARG_V1236_1186) else ((True if tco_apply(shen_occursx63, [KL_ARG_V1236_1186, KL_ARG_V1237_1187[0]]) else tail_call(shen_occursx63, [KL_ARG_V1236_1186, KL_ARG_V1237_1187[1]])) if shen_consp(KL_ARG_V1237_1187) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.occurs?', shen_occursx63)

@tail_recursion
def kl_identical(KL_ARG_V1239_1188, KL_ARG_V1240_1189, KL_ARG_V1241_1190, KL_ARG_V1242_1191):
    global symdic
    return tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [KL_ARG_V1239_1188, KL_ARG_V1241_1190]), tco_apply(shen_lazyderef, [KL_ARG_V1240_1189, KL_ARG_V1241_1190]), KL_ARG_V1241_1190, KL_ARG_V1242_1191])
shen_add_fun('identical', kl_identical)

@tail_recursion
def shen_lzyx61x61(KL_ARG_V1259_1192, KL_ARG_V1260_1193, KL_ARG_V1261_1194, KL_ARG_V1262_1195):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1262_1195]) if shen_eq(KL_ARG_V1260_1193, KL_ARG_V1259_1192) else (tail_call(shen_lzyx61x61, [tco_apply(shen_lazyderef, [KL_ARG_V1259_1192[0], KL_ARG_V1261_1194]), tco_apply(shen_lazyderef, [KL_ARG_V1260_1193[0], KL_ARG_V1261_1194]), KL_ARG_V1261_1194, (lambda : tail_call(shen_lzyx61x61, [KL_ARG_V1259_1192[1], KL_ARG_V1260_1193[1], KL_ARG_V1261_1194, KL_ARG_V1262_1195]))]) if (shen_consp(KL_ARG_V1260_1193) if shen_consp(KL_ARG_V1259_1192) else False) else (False if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.lzy==', shen_lzyx61x61)

@tail_recursion
def shen_pvar(KL_ARG_V1264_1196):
    global symdic
    return ('Var' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V1264_1196, 1), '', symdic.symdic_shen_a]))
shen_add_fun('shen.pvar', shen_pvar)

@tail_recursion
def kl_bind(KL_ARG_V1265_1197, KL_ARG_V1266_1198, KL_ARG_V1267_1199, KL_ARG_V1268_1200):

    class KL_Context:
        KL_LOC_Result_1201 = None
    KL_CTX = KL_Context()
    global symdic
    return [tco_apply(shen_bindv, [KL_ARG_V1265_1197, KL_ARG_V1266_1198, KL_ARG_V1267_1199]), [setattr(KL_CTX, 'KL_LOC_Result_1201', tco_apply(kl_thaw, [KL_ARG_V1268_1200])), [tco_apply(shen_unbindv, [KL_ARG_V1265_1197, KL_ARG_V1267_1199]), KL_CTX.KL_LOC_Result_1201][(-1)]][(-1)]][(-1)]
shen_add_fun('bind', kl_bind)

@tail_recursion
def kl_fwhen(KL_ARG_V1283_1202, KL_ARG_V1284_1203, KL_ARG_V1285_1204):
    global symdic
    return (tail_call(kl_thaw, [KL_ARG_V1285_1204]) if shen_eq(True, KL_ARG_V1283_1202) else (False if shen_eq(False, KL_ARG_V1283_1202) else (shen_simple_error(('fwhen expects a boolean: not ' + tco_apply(shen_app, [KL_ARG_V1283_1202, '%', symdic.symdic_shen_s]))) if True else shen_simple_error('condition failure'))))
shen_add_fun('fwhen', kl_fwhen)

@tail_recursion
def kl_call(KL_ARG_V1298_1205, KL_ARG_V1299_1206, KL_ARG_V1300_1207):
    global symdic
    return (tail_call(shen_callx45help, [tco_apply(shen_m_prolog_to_sx45prolog_predicate, [tco_apply(shen_lazyderef, [KL_ARG_V1298_1205[0], KL_ARG_V1299_1206])]), KL_ARG_V1298_1205[1], KL_ARG_V1299_1206, KL_ARG_V1300_1207]) if shen_consp(KL_ARG_V1298_1205) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('call', kl_call)

@tail_recursion
def shen_callx45help(KL_ARG_V1301_1208, KL_ARG_V1302_1209, KL_ARG_V1303_1210, KL_ARG_V1304_1211):
    global symdic
    return (shen_apply(KL_ARG_V1301_1208, [KL_ARG_V1303_1210, KL_ARG_V1304_1211]) if shen_eq([], KL_ARG_V1302_1209) else (tail_call(shen_callx45help, [shen_apply(KL_ARG_V1301_1208, [KL_ARG_V1302_1209[0]]), KL_ARG_V1302_1209[1], KL_ARG_V1303_1210, KL_ARG_V1304_1211]) if shen_consp(KL_ARG_V1302_1209) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.call-help', shen_callx45help)

@tail_recursion
def shen_intprolog(KL_ARG_V1305_1212):

    class KL_Context:
        KL_LOC_ProcessN_1213 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_ProcessN_1213', tco_apply(shen_startx45newx45prologx45process, [])), tail_call(shen_intprologx45help, [KL_ARG_V1305_1212[0][0], tco_apply(shen_insertx45prologx45variables, [[KL_ARG_V1305_1212[0][1], [KL_ARG_V1305_1212[1], []]], KL_CTX.KL_LOC_ProcessN_1213]), KL_CTX.KL_LOC_ProcessN_1213])][(-1)] if (shen_consp(KL_ARG_V1305_1212[0]) if shen_consp(KL_ARG_V1305_1212) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprolog]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog', shen_intprolog)

@tail_recursion
def shen_intprologx45help(KL_ARG_V1306_1214, KL_ARG_V1307_1215, KL_ARG_V1308_1216):
    global symdic
    return (tail_call(shen_intprologx45helpx45help, [KL_ARG_V1306_1214, KL_ARG_V1307_1215[0], KL_ARG_V1307_1215[1][0], KL_ARG_V1308_1216]) if ((shen_eq([], KL_ARG_V1307_1215[1][1]) if shen_consp(KL_ARG_V1307_1215[1]) else False) if shen_consp(KL_ARG_V1307_1215) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45help]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.intprolog-help', shen_intprologx45help)

@tail_recursion
def shen_intprologx45helpx45help(KL_ARG_V1309_1217, KL_ARG_V1310_1218, KL_ARG_V1311_1219, KL_ARG_V1312_1220):
    global symdic
    return (shen_apply(KL_ARG_V1309_1217, [KL_ARG_V1312_1220, (lambda : tail_call(shen_callx45rest, [KL_ARG_V1311_1219, KL_ARG_V1312_1220]))]) if shen_eq([], KL_ARG_V1310_1218) else (tail_call(shen_intprologx45helpx45help, [shen_apply(KL_ARG_V1309_1217, [KL_ARG_V1310_1218[0]]), KL_ARG_V1310_1218[1], KL_ARG_V1311_1219, KL_ARG_V1312_1220]) if shen_consp(KL_ARG_V1310_1218) else (tail_call(shen_sysx45error, [symdic.symdic_shen_intprologx45helpx45help]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.intprolog-help-help', shen_intprologx45helpx45help)

@tail_recursion
def shen_callx45rest(KL_ARG_V1315_1221, KL_ARG_V1316_1222):
    global symdic
    return (True if shen_eq([], KL_ARG_V1315_1221) else (tail_call(shen_callx45rest, [[[tco_apply(KL_ARG_V1315_1221[0][0], [KL_ARG_V1315_1221[0][1][0]]), KL_ARG_V1315_1221[0][1][1]], KL_ARG_V1315_1221[1]], KL_ARG_V1316_1222]) if ((shen_consp(KL_ARG_V1315_1221[0][1]) if shen_consp(KL_ARG_V1315_1221[0]) else False) if shen_consp(KL_ARG_V1315_1221) else False) else (tail_call(KL_ARG_V1315_1221[0][0], [KL_ARG_V1316_1222, (lambda : tail_call(shen_callx45rest, [KL_ARG_V1315_1221[1], KL_ARG_V1316_1222]))]) if ((shen_eq([], KL_ARG_V1315_1221[0][1]) if shen_consp(KL_ARG_V1315_1221[0]) else False) if shen_consp(KL_ARG_V1315_1221) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_callx45rest]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.call-rest', shen_callx45rest)

@tail_recursion
def shen_startx45newx45prologx45process():

    class KL_Context:
        KL_LOC_IncrementProcessCounter_1223 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_IncrementProcessCounter_1223', shen_set(symdic.symdic_shen_x42processx45counterx42, (1 + shen_get(symdic.symdic_shen_x42processx45counterx42)))), tail_call(shen_initialisex45prolog, [KL_CTX.KL_LOC_IncrementProcessCounter_1223])][(-1)]
shen_add_fun('shen.start-new-prolog-process', shen_startx45newx45prologx45process)

@tail_recursion
def shen_insertx45prologx45variables(KL_ARG_V1317_1224, KL_ARG_V1318_1225):
    global symdic
    return tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1317_1224, tco_apply(shen_flatten, [KL_ARG_V1317_1224]), KL_ARG_V1318_1225])
shen_add_fun('shen.insert-prolog-variables', shen_insertx45prologx45variables)

@tail_recursion
def shen_insertx45prologx45variablesx45help(KL_ARG_V1323_1226, KL_ARG_V1324_1227, KL_ARG_V1325_1228):

    class KL_Context:
        KL_LOC_V_1229 = None
        KL_LOC_XVx47Y_1230 = None
        KL_LOC_Zx45Y_1231 = None
    KL_CTX = KL_Context()
    global symdic
    return (KL_ARG_V1323_1226 if shen_eq([], KL_ARG_V1324_1227) else ([setattr(KL_CTX, 'KL_LOC_V_1229', tco_apply(shen_newpv, [KL_ARG_V1325_1228])), [setattr(KL_CTX, 'KL_LOC_XVx47Y_1230', tco_apply(kl_subst, [KL_CTX.KL_LOC_V_1229, KL_ARG_V1324_1227[0], KL_ARG_V1323_1226])), [setattr(KL_CTX, 'KL_LOC_Zx45Y_1231', tco_apply(kl_remove, [KL_ARG_V1324_1227[0], KL_ARG_V1324_1227[1]])), tail_call(shen_insertx45prologx45variablesx45help, [KL_CTX.KL_LOC_XVx47Y_1230, KL_CTX.KL_LOC_Zx45Y_1231, KL_ARG_V1325_1228])][(-1)]][(-1)]][(-1)] if (tco_apply(kl_variablex63, [KL_ARG_V1324_1227[0]]) if shen_consp(KL_ARG_V1324_1227) else False) else (tail_call(shen_insertx45prologx45variablesx45help, [KL_ARG_V1323_1226, KL_ARG_V1324_1227[1], KL_ARG_V1325_1228]) if shen_consp(KL_ARG_V1324_1227) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45prologx45variablesx45help]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.insert-prolog-variables-help', shen_insertx45prologx45variablesx45help)

@tail_recursion
def shen_initialisex45prolog(KL_ARG_V1326_1232):

    class KL_Context:
        KL_LOC_Vector_1233 = None
        KL_LOC_Counter_1234 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Vector_1233', shen_absvector_set(shen_get(symdic.symdic_shen_x42prologvectorsx42), KL_ARG_V1326_1232, tco_apply(shen_fillvector, [tco_apply(kl_vector, [10]), 1, 10, symdic.symdic_shen_x45nullx45]))), [setattr(KL_CTX, 'KL_LOC_Counter_1234', shen_absvector_set(shen_get(symdic.symdic_shen_x42varcounterx42), KL_ARG_V1326_1232, 1)), KL_ARG_V1326_1232][(-1)]][(-1)]
shen_add_fun('shen.initialise-prolog', shen_initialisex45prolog)


#============================== track.kl==============================



@tail_recursion
def shen_f_error(KL_ARG_V2086_1235):
    global symdic
    return [tco_apply(shen_prhush, [('partial function ' + tco_apply(shen_app, [KL_ARG_V2086_1235, ';\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), [(tco_apply(shen_trackx45function, [tco_apply(kl_ps, [KL_ARG_V2086_1235])]) if (tco_apply(kl_yx45orx45nx63, [('track ' + tco_apply(shen_app, [KL_ARG_V2086_1235, '? ', symdic.symdic_shen_a]))]) if (not tco_apply(shen_trackedx63, [KL_ARG_V2086_1235])) else False) else symdic.symdic_shen_ok), shen_simple_error('aborted')][(-1)]][(-1)]
shen_add_fun('shen.f_error', shen_f_error)

@tail_recursion
def shen_trackedx63(KL_ARG_V2087_1236):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2087_1236, shen_get(symdic.symdic_shen_x42trackingx42)])
shen_add_fun('shen.tracked?', shen_trackedx63)

@tail_recursion
def kl_track(KL_ARG_V2088_1237):

    class KL_Context:
        KL_LOC_Source_1238 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Source_1238', tco_apply(kl_ps, [KL_ARG_V2088_1237])), tail_call(shen_trackx45function, [KL_CTX.KL_LOC_Source_1238])][(-1)]
shen_add_fun('track', kl_track)

@tail_recursion
def shen_trackx45function(KL_ARG_V2089_1239):

    class KL_Context:
        KL_LOC_KL_1240 = None
        KL_LOC_Ob_1241 = None
        KL_LOC_Tr_1242 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_KL_1240', [symdic.symdic_kl_defun, [KL_ARG_V2089_1239[1][0], [KL_ARG_V2089_1239[1][1][0], [tco_apply(shen_insertx45trackingx45code, [KL_ARG_V2089_1239[1][0], KL_ARG_V2089_1239[1][1][0], KL_ARG_V2089_1239[1][1][1][0]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Ob_1241', tco_apply(kl_eval, [KL_CTX.KL_LOC_KL_1240])), [setattr(KL_CTX, 'KL_LOC_Tr_1242', shen_set(symdic.symdic_shen_x42trackingx42, [KL_CTX.KL_LOC_Ob_1241, shen_get(symdic.symdic_shen_x42trackingx42)])), KL_CTX.KL_LOC_Ob_1241][(-1)]][(-1)]][(-1)] if (((((shen_eq([], KL_ARG_V2089_1239[1][1][1][1]) if shen_consp(KL_ARG_V2089_1239[1][1][1]) else False) if shen_consp(KL_ARG_V2089_1239[1][1]) else False) if shen_consp(KL_ARG_V2089_1239[1]) else False) if shen_eq(symdic.symdic_kl_defun, KL_ARG_V2089_1239[0]) else False) if shen_consp(KL_ARG_V2089_1239) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_trackx45function]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.track-function', shen_trackx45function)

@tail_recursion
def shen_insertx45trackingx45code(KL_ARG_V2090_1243, KL_ARG_V2091_1244, KL_ARG_V2092_1245):
    global symdic
    return [symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_shen_x42callx42, [[symdic.symdic_kl_x43, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [1, []]]], []]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_inputx45track, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [KL_ARG_V2090_1243, [tco_apply(shen_cons_form, [KL_ARG_V2091_1244]), []]]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_terprix45orx45readx45char, []], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V2092_1245, [[symdic.symdic_kl_do, [[symdic.symdic_shen_outputx45track, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [KL_ARG_V2090_1243, [symdic.symdic_Result, []]]]], [[symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_shen_x42callx42, [[symdic.symdic_kl_x45, [[symdic.symdic_kl_value, [symdic.symdic_shen_x42callx42, []]], [1, []]]], []]]], [[symdic.symdic_kl_do, [[symdic.symdic_shen_terprix45orx45readx45char, []], [symdic.symdic_Result, []]]], []]]], []]]], []]]]], []]]], []]]], []]]]
shen_add_fun('shen.insert-tracking-code', shen_insertx45trackingx45code)
shen_set(symdic.symdic_shen_x42stepx42, False)

@tail_recursion
def kl_step(KL_ARG_V2097_1246):
    global symdic
    return (shen_set(symdic.symdic_shen_x42stepx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2097_1246) else (shen_set(symdic.symdic_shen_x42stepx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2097_1246) else (shen_simple_error('step expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('step', kl_step)

@tail_recursion
def kl_spy(KL_ARG_V2102_1247):
    global symdic
    return (shen_set(symdic.symdic_shen_x42spyx42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2102_1247) else (shen_set(symdic.symdic_shen_x42spyx42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2102_1247) else (shen_simple_error('spy expects a + or a -.\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('spy', kl_spy)

@tail_recursion
def shen_terprix45orx45readx45char():
    global symdic
    return (tail_call(shen_checkx45byte, [shen_read_byte(shen_get(symdic.symdic_kl_x42stinputx42))]) if shen_get(symdic.symdic_shen_x42stepx42) else tail_call(kl_nl, [1]))
shen_add_fun('shen.terpri-or-read-char', shen_terprix45orx45readx45char)

@tail_recursion
def shen_checkx45byte(KL_ARG_V2107_1248):
    global symdic
    return (shen_simple_error('aborted') if shen_eq(KL_ARG_V2107_1248, tco_apply(shen_hat, [])) else (True if True else shen_simple_error('condition failure')))
shen_add_fun('shen.check-byte', shen_checkx45byte)

@tail_recursion
def shen_inputx45track(KL_ARG_V2108_1249, KL_ARG_V2109_1250, KL_ARG_V2110_1251):
    global symdic
    return [tco_apply(shen_prhush, [('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2108_1249]), ('<' + tco_apply(shen_app, [KL_ARG_V2108_1249, ('> Inputs to ' + tco_apply(shen_app, [KL_ARG_V2109_1250, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2108_1249]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]), tail_call(shen_recursivelyx45print, [KL_ARG_V2110_1251])][(-1)]
shen_add_fun('shen.input-track', shen_inputx45track)

@tail_recursion
def shen_recursivelyx45print(KL_ARG_V2111_1252):
    global symdic
    return (tail_call(shen_prhush, [' ==>', tco_apply(kl_stoutput, [])]) if shen_eq([], KL_ARG_V2111_1252) else ([tco_apply(kl_print, [KL_ARG_V2111_1252[0]]), [tco_apply(shen_prhush, [', ', tco_apply(kl_stoutput, [])]), tail_call(shen_recursivelyx45print, [KL_ARG_V2111_1252[1]])][(-1)]][(-1)] if shen_consp(KL_ARG_V2111_1252) else (tail_call(shen_sysx45error, [symdic.symdic_shen_recursivelyx45print]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.recursively-print', shen_recursivelyx45print)

@tail_recursion
def shen_spaces(KL_ARG_V2112_1253):
    global symdic
    return ('' if shen_eq(0, KL_ARG_V2112_1253) else ((' ' + tco_apply(shen_spaces, [(KL_ARG_V2112_1253 - 1)])) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.spaces', shen_spaces)

@tail_recursion
def shen_outputx45track(KL_ARG_V2113_1254, KL_ARG_V2114_1255, KL_ARG_V2115_1256):
    global symdic
    return tail_call(shen_prhush, [('\r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2113_1254]), ('<' + tco_apply(shen_app, [KL_ARG_V2113_1254, ('> Output from ' + tco_apply(shen_app, [KL_ARG_V2114_1255, (' \r\n' + tco_apply(shen_app, [tco_apply(shen_spaces, [KL_ARG_V2113_1254]), ('==> ' + tco_apply(shen_app, [KL_ARG_V2115_1256, '', symdic.symdic_shen_s])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])
shen_add_fun('shen.output-track', shen_outputx45track)

@tail_recursion
def kl_untrack(KL_ARG_V2116_1257):
    global symdic
    return tail_call(kl_eval, [tco_apply(kl_ps, [KL_ARG_V2116_1257])])
shen_add_fun('untrack', kl_untrack)

@tail_recursion
def kl_profile(KL_ARG_V2117_1258):
    global symdic
    return tail_call(shen_profilex45help, [tco_apply(kl_ps, [KL_ARG_V2117_1258])])
shen_add_fun('profile', kl_profile)

@tail_recursion
def shen_profilex45help(KL_ARG_V2122_1259):

    class KL_Context:
        KL_LOC_G_1260 = None
        KL_LOC_Profile_1261 = None
        KL_LOC_Def_1262 = None
        KL_LOC_CompileProfile_1263 = None
        KL_LOC_CompileG_1264 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_G_1260', tco_apply(kl_gensym, [symdic.symdic_shen_f])), [setattr(KL_CTX, 'KL_LOC_Profile_1261', [symdic.symdic_kl_defun, [KL_ARG_V2122_1259[1][0], [KL_ARG_V2122_1259[1][1][0], [tco_apply(shen_profilex45func, [KL_ARG_V2122_1259[1][0], KL_ARG_V2122_1259[1][1][0], [KL_CTX.KL_LOC_G_1260, KL_ARG_V2122_1259[1][1][0]]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_Def_1262', [symdic.symdic_kl_defun, [KL_CTX.KL_LOC_G_1260, [KL_ARG_V2122_1259[1][1][0], [tco_apply(kl_subst, [KL_CTX.KL_LOC_G_1260, KL_ARG_V2122_1259[1][0], KL_ARG_V2122_1259[1][1][1][0]]), []]]]]), [setattr(KL_CTX, 'KL_LOC_CompileProfile_1263', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Profile_1261])), [setattr(KL_CTX, 'KL_LOC_CompileG_1264', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_Def_1262])), KL_ARG_V2122_1259[1][0]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if (((((shen_eq([], KL_ARG_V2122_1259[1][1][1][1]) if shen_consp(KL_ARG_V2122_1259[1][1][1]) else False) if shen_consp(KL_ARG_V2122_1259[1][1]) else False) if shen_consp(KL_ARG_V2122_1259[1]) else False) if shen_eq(symdic.symdic_kl_defun, KL_ARG_V2122_1259[0]) else False) if shen_consp(KL_ARG_V2122_1259) else False) else (shen_simple_error('Cannot profile.\r\n') if True else shen_simple_error('condition failure')))
shen_add_fun('shen.profile-help', shen_profilex45help)

@tail_recursion
def kl_unprofile(KL_ARG_V2123_1265):
    global symdic
    return tail_call(kl_untrack, [KL_ARG_V2123_1265])
shen_add_fun('unprofile', kl_unprofile)

@tail_recursion
def shen_profilex45func(KL_ARG_V2124_1266, KL_ARG_V2125_1267, KL_ARG_V2126_1268):
    global symdic
    return [symdic.symdic_kl_let, [symdic.symdic_Start, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [[symdic.symdic_kl_let, [symdic.symdic_Result, [KL_ARG_V2126_1268, [[symdic.symdic_kl_let, [symdic.symdic_Finish, [[symdic.symdic_kl_x45, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Start, []]]], [[symdic.symdic_kl_let, [symdic.symdic_Record, [[symdic.symdic_shen_putx45profile, [KL_ARG_V2124_1266, [[symdic.symdic_kl_x43, [[symdic.symdic_shen_getx45profile, [KL_ARG_V2124_1266, []]], [symdic.symdic_Finish, []]]], []]]], [symdic.symdic_Result, []]]]], []]]]], []]]]], []]]]]
shen_add_fun('shen.profile-func', shen_profilex45func)

@tail_recursion
def kl_profilex45results(KL_ARG_V2127_1269):

    class KL_Context:
        KL_LOC_Results_1270 = None
        KL_LOC_Initialise_1271 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Results_1270', tco_apply(shen_getx45profile, [KL_ARG_V2127_1269])), [setattr(KL_CTX, 'KL_LOC_Initialise_1271', tco_apply(shen_putx45profile, [KL_ARG_V2127_1269, 0])), tail_call(kl_x64p, [KL_ARG_V2127_1269, KL_CTX.KL_LOC_Results_1270])][(-1)]][(-1)]
shen_add_fun('profile-results', kl_profilex45results)

@tail_recursion
def shen_getx45profile(KL_ARG_V2128_1272):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V2128_1272, symdic.symdic_kl_profile, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1273: 0))
shen_add_fun('shen.get-profile', shen_getx45profile)

@tail_recursion
def shen_putx45profile(KL_ARG_V2129_1274, KL_ARG_V2130_1275):
    global symdic
    return tail_call(kl_put, [KL_ARG_V2129_1274, symdic.symdic_kl_profile, KL_ARG_V2130_1275, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])
shen_add_fun('shen.put-profile', shen_putx45profile)


#============================== load.kl==============================



@tail_recursion
def kl_load(KL_ARG_V829_1276):

    class KL_Context:
        KL_LOC_Load_1277 = None
        KL_LOC_Start_1278 = None
        KL_LOC_Result_1279 = None
        KL_LOC_Finish_1280 = None
        KL_LOC_Time_1281 = None
        KL_LOC_Message_1282 = None
        KL_LOC_Infs_1283 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Load_1277', [setattr(KL_CTX, 'KL_LOC_Start_1278', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Result_1279', tco_apply(shen_loadx45help, [shen_get(symdic.symdic_shen_x42tcx42), tco_apply(kl_readx45file, [KL_ARG_V829_1276])])), [setattr(KL_CTX, 'KL_LOC_Finish_1280', shen_get_time(symdic.symdic_kl_run)), [setattr(KL_CTX, 'KL_LOC_Time_1281', (KL_CTX.KL_LOC_Finish_1280 - KL_CTX.KL_LOC_Start_1278)), [setattr(KL_CTX, 'KL_LOC_Message_1282', tco_apply(shen_prhush, [('\r\nrun time: ' + (str(KL_CTX.KL_LOC_Time_1281) + ' secs\r\n')), tco_apply(kl_stoutput, [])])), KL_CTX.KL_LOC_Result_1279][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]), [setattr(KL_CTX, 'KL_LOC_Infs_1283', (tco_apply(shen_prhush, [('\r\ntypechecked in ' + tco_apply(shen_app, [tco_apply(kl_inferences, []), ' inferences\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])]) if shen_get(symdic.symdic_shen_x42tcx42) else symdic.symdic_shen_skip)), symdic.symdic_kl_loaded][(-1)]][(-1)]
shen_add_fun('load', kl_load)

@tail_recursion
def shen_loadx45help(KL_ARG_V834_1284, KL_ARG_V835_1285):

    class KL_Context:
        KL_LOC_RemoveSynonyms_1287 = None
        KL_LOC_Table_1288 = None
        KL_LOC_Assume_1289 = None
    KL_CTX = KL_Context()
    global symdic
    return (tail_call(kl_map, [(lambda KL_ARG_X_1286: tail_call(shen_prhush, [tco_apply(shen_app, [tco_apply(shen_evalx45withoutx45macros, [KL_ARG_X_1286]), '\r\n', symdic.symdic_shen_s]), tco_apply(kl_stoutput, [])])), KL_ARG_V835_1285]) if shen_eq(False, KL_ARG_V834_1284) else ([setattr(KL_CTX, 'KL_LOC_RemoveSynonyms_1287', tco_apply(kl_mapcan, [symdic.symdic_shen_removex45synonyms, KL_ARG_V835_1285])), [setattr(KL_CTX, 'KL_LOC_Table_1288', tco_apply(kl_mapcan, [symdic.symdic_shen_typetable, KL_CTX.KL_LOC_RemoveSynonyms_1287])), [setattr(KL_CTX, 'KL_LOC_Assume_1289', tco_apply(kl_map, [symdic.symdic_shen_assumetype, KL_CTX.KL_LOC_Table_1288])), shen_try_except((lambda : tco_apply(kl_map, [symdic.symdic_shen_typecheckx45andx45load, KL_CTX.KL_LOC_RemoveSynonyms_1287])), (lambda KL_ARG_E_1290: tail_call(shen_unwindx45types, [KL_ARG_E_1290, KL_CTX.KL_LOC_Table_1288])))][(-1)]][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.load-help', shen_loadx45help)

@tail_recursion
def shen_removex45synonyms(KL_ARG_V836_1291):
    global symdic
    return ([tco_apply(kl_eval, [KL_ARG_V836_1291]), []][(-1)] if (shen_eq(symdic.symdic_shen_synonymsx45help, KL_ARG_V836_1291[0]) if shen_consp(KL_ARG_V836_1291) else False) else ([KL_ARG_V836_1291, []] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.remove-synonyms', shen_removex45synonyms)

@tail_recursion
def shen_typecheckx45andx45load(KL_ARG_V837_1292):
    global symdic
    return [tco_apply(kl_nl, [1]), tail_call(shen_typecheckx45andx45evaluate, [KL_ARG_V837_1292, tco_apply(kl_gensym, [symdic.symdic_A])])][(-1)]
shen_add_fun('shen.typecheck-and-load', shen_typecheckx45andx45load)

@tail_recursion
def shen_typetable(KL_ARG_V846_1293):

    class KL_Context:
        KL_LOC_Sig_1294 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Sig_1294', tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43restx62, KL_ARG_V846_1293[1][1], []])), (shen_simple_error(tco_apply(shen_app, [KL_ARG_V846_1293[1][0], ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if shen_eq(KL_CTX.KL_LOC_Sig_1294, tco_apply(kl_fail, [])) else [[KL_ARG_V846_1293[1][0], KL_CTX.KL_LOC_Sig_1294], []])][(-1)] if ((shen_consp(KL_ARG_V846_1293[1]) if shen_eq(symdic.symdic_kl_define, KL_ARG_V846_1293[0]) else False) if shen_consp(KL_ARG_V846_1293) else False) else ([[KL_ARG_V846_1293[1][0], [KL_ARG_V846_1293[1][1][1][0], [symdic.symdic_kl_x61x61x62, [KL_ARG_V846_1293[1][1][1][1][1][0], []]]]], []] if ((((((((((((((shen_eq(symdic.symdic_kl_x125, KL_ARG_V846_1293[1][1][1][1][1][1][0]) if shen_consp(KL_ARG_V846_1293[1][1][1][1][1][1]) else False) if shen_consp(KL_ARG_V846_1293[1][1][1][1][1]) else False) if shen_eq(symdic.symdic_kl_x61x61x62, KL_ARG_V846_1293[1][1][1][1][0]) else False) if shen_consp(KL_ARG_V846_1293[1][1][1][1]) else False) if shen_eq([], KL_ARG_V846_1293[1][1][1][0][1][1]) else False) if shen_consp(KL_ARG_V846_1293[1][1][1][0][1]) else False) if shen_eq(symdic.symdic_kl_list, KL_ARG_V846_1293[1][1][1][0][0]) else False) if shen_consp(KL_ARG_V846_1293[1][1][1][0]) else False) if shen_consp(KL_ARG_V846_1293[1][1][1]) else False) if shen_eq(symdic.symdic_kl_x123, KL_ARG_V846_1293[1][1][0]) else False) if shen_consp(KL_ARG_V846_1293[1][1]) else False) if shen_consp(KL_ARG_V846_1293[1]) else False) if shen_eq(symdic.symdic_kl_defcc, KL_ARG_V846_1293[0]) else False) if shen_consp(KL_ARG_V846_1293) else False) else (shen_simple_error(tco_apply(shen_app, [KL_ARG_V846_1293[1][0], ' lacks a proper signature.\r\n', symdic.symdic_shen_a])) if ((shen_consp(KL_ARG_V846_1293[1]) if shen_eq(symdic.symdic_kl_defcc, KL_ARG_V846_1293[0]) else False) if shen_consp(KL_ARG_V846_1293) else False) else ([] if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.typetable', shen_typetable)

@tail_recursion
def shen_assumetype(KL_ARG_V847_1295):
    global symdic
    return (apply(kl_declare, [KL_ARG_V847_1295[0], KL_ARG_V847_1295[1]]) if shen_consp(KL_ARG_V847_1295) else (tail_call(shen_sysx45error, [symdic.symdic_shen_assumetype]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assumetype', shen_assumetype)

@tail_recursion
def shen_unwindx45types(KL_ARG_V852_1296, KL_ARG_V853_1297):
    global symdic
    return (shen_simple_error(KL_ARG_V852_1296.message) if shen_eq([], KL_ARG_V853_1297) else ([tco_apply(shen_remtype, [KL_ARG_V853_1297[0][0]]), tail_call(shen_unwindx45types, [KL_ARG_V852_1296, KL_ARG_V853_1297[1]])][(-1)] if (shen_consp(KL_ARG_V853_1297[0]) if shen_consp(KL_ARG_V853_1297) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_unwindx45types]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.unwind-types', shen_unwindx45types)

@tail_recursion
def shen_remtype(KL_ARG_V854_1298):
    global symdic
    return shen_set(symdic.symdic_shen_x42signedfuncsx42, tco_apply(shen_removetype, [KL_ARG_V854_1298, shen_get(symdic.symdic_shen_x42signedfuncsx42)]))
shen_add_fun('shen.remtype', shen_remtype)

@tail_recursion
def shen_removetype(KL_ARG_V859_1299, KL_ARG_V860_1300):
    global symdic
    return ([] if shen_eq([], KL_ARG_V860_1300) else (tail_call(shen_removetype, [KL_ARG_V860_1300[0][0], KL_ARG_V860_1300[1]]) if ((shen_eq(KL_ARG_V860_1300[0][0], KL_ARG_V859_1299) if shen_consp(KL_ARG_V860_1300[0]) else False) if shen_consp(KL_ARG_V860_1300) else False) else ([KL_ARG_V860_1300[0], tco_apply(shen_removetype, [KL_ARG_V859_1299, KL_ARG_V860_1300[1]])] if shen_consp(KL_ARG_V860_1300) else (tail_call(shen_sysx45error, [symdic.symdic_shen_removetype]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.removetype', shen_removetype)

@tail_recursion
def shen_x60sigx43restx62(KL_ARG_V866_1301):

    class KL_Context:
        KL_LOC_Result_1302 = None
        KL_LOC_Parse_shen_x60signaturex62_1303 = None
        KL_LOC_Parse_x60x33x62_1304 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1302', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_1303', tco_apply(shen_x60signaturex62, [KL_ARG_V866_1301])), ([setattr(KL_CTX, 'KL_LOC_Parse_x60x33x62_1304', tco_apply(x60x33x62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1303])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_x60x33x62_1304[0], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1303])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_x60x33x62_1304)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_1303)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1302, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1302)][(-1)]
shen_add_fun('shen.<sig+rest>', shen_x60sigx43restx62)

@tail_recursion
def kl_writex45tox45file(KL_ARG_V867_1305, KL_ARG_V868_1306):

    class KL_Context:
        KL_LOC_Stream_1307 = None
        KL_LOC_String_1308 = None
        KL_LOC_Write_1309 = None
        KL_LOC_Close_1310 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Stream_1307', shen_open(symdic.symdic_kl_file, KL_ARG_V867_1305, symdic.symdic_kl_out)), [setattr(KL_CTX, 'KL_LOC_String_1308', (tco_apply(shen_app, [KL_ARG_V868_1306, '\r\n\r\n', symdic.symdic_shen_a]) if isinstance(KL_ARG_V868_1306, str) else tco_apply(shen_app, [KL_ARG_V868_1306, '\r\n\r\n', symdic.symdic_shen_s]))), [setattr(KL_CTX, 'KL_LOC_Write_1309', shen_pr(KL_CTX.KL_LOC_String_1308, KL_CTX.KL_LOC_Stream_1307)), [setattr(KL_CTX, 'KL_LOC_Close_1310', shen_close(KL_CTX.KL_LOC_Stream_1307)), KL_ARG_V868_1306][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('write-to-file', kl_writex45tox45file)


#============================== writer.kl==============================



@tail_recursion
def kl_print(KL_ARG_V2238_1311):

    class KL_Context:
        KL_LOC_String_1312 = None
        KL_LOC_Print_1313 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_String_1312', tco_apply(shen_insert, [KL_ARG_V2238_1311, '~S'])), [setattr(KL_CTX, 'KL_LOC_Print_1313', tco_apply(shen_prhush, [KL_CTX.KL_LOC_String_1312, tco_apply(kl_stoutput, [])])), KL_ARG_V2238_1311][(-1)]][(-1)]
shen_add_fun('print', kl_print)

@tail_recursion
def shen_prhush(KL_ARG_V2239_1314, KL_ARG_V2240_1315):
    global symdic
    return (KL_ARG_V2239_1314 if shen_get(symdic.symdic_x42hushx42) else shen_pr(KL_ARG_V2239_1314, KL_ARG_V2240_1315))
shen_add_fun('shen.prhush', shen_prhush)

@tail_recursion
def shen_mkstr(KL_ARG_V2241_1316, KL_ARG_V2242_1317):
    global symdic
    return (tail_call(shen_mkstrx45l, [tco_apply(shen_procx45nl, [KL_ARG_V2241_1316]), KL_ARG_V2242_1317]) if isinstance(KL_ARG_V2241_1316, str) else (tail_call(shen_mkstrx45r, [[symdic.symdic_shen_procx45nl, [KL_ARG_V2241_1316, []]], KL_ARG_V2242_1317]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.mkstr', shen_mkstr)

@tail_recursion
def shen_mkstrx45l(KL_ARG_V2243_1318, KL_ARG_V2244_1319):
    global symdic
    return (KL_ARG_V2243_1318 if shen_eq([], KL_ARG_V2244_1319) else (tail_call(shen_mkstrx45l, [tco_apply(shen_insertx45l, [KL_ARG_V2244_1319[0], KL_ARG_V2243_1318]), KL_ARG_V2244_1319[1]]) if shen_consp(KL_ARG_V2244_1319) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45l]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-l', shen_mkstrx45l)

@tail_recursion
def shen_insertx45l(KL_ARG_V2247_1320, KL_ARG_V2248_1321):
    global symdic
    return ('' if shen_eq('', KL_ARG_V2248_1321) else ([symdic.symdic_shen_app, [KL_ARG_V2247_1320, [KL_ARG_V2248_1321[1:][1:], [symdic.symdic_shen_a, []]]]] if (((shen_eq('A', KL_ARG_V2248_1321[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321[1:]]) else False) if shen_eq('~', KL_ARG_V2248_1321[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else False) else ([symdic.symdic_shen_app, [KL_ARG_V2247_1320, [KL_ARG_V2248_1321[1:][1:], [symdic.symdic_shen_r, []]]]] if (((shen_eq('R', KL_ARG_V2248_1321[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321[1:]]) else False) if shen_eq('~', KL_ARG_V2248_1321[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else False) else ([symdic.symdic_shen_app, [KL_ARG_V2247_1320, [KL_ARG_V2248_1321[1:][1:], [symdic.symdic_shen_s, []]]]] if (((shen_eq('S', KL_ARG_V2248_1321[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321[1:]]) else False) if shen_eq('~', KL_ARG_V2248_1321[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else False) else (tail_call(shen_factorx45cn, [[symdic.symdic_kl_cn, [KL_ARG_V2248_1321[0], [tco_apply(shen_insertx45l, [KL_ARG_V2247_1320, KL_ARG_V2248_1321[1:]]), []]]]]) if tco_apply(shen_x43stringx63, [KL_ARG_V2248_1321]) else ([symdic.symdic_kl_cn, [KL_ARG_V2248_1321[1][0], [tco_apply(shen_insertx45l, [KL_ARG_V2247_1320, KL_ARG_V2248_1321[1][1][0]]), []]]] if ((((shen_eq([], KL_ARG_V2248_1321[1][1][1]) if shen_consp(KL_ARG_V2248_1321[1][1]) else False) if shen_consp(KL_ARG_V2248_1321[1]) else False) if shen_eq(symdic.symdic_kl_cn, KL_ARG_V2248_1321[0]) else False) if shen_consp(KL_ARG_V2248_1321) else False) else ([symdic.symdic_shen_app, [KL_ARG_V2248_1321[1][0], [tco_apply(shen_insertx45l, [KL_ARG_V2247_1320, KL_ARG_V2248_1321[1][1][0]]), KL_ARG_V2248_1321[1][1][1]]]] if (((((shen_eq([], KL_ARG_V2248_1321[1][1][1][1]) if shen_consp(KL_ARG_V2248_1321[1][1][1]) else False) if shen_consp(KL_ARG_V2248_1321[1][1]) else False) if shen_consp(KL_ARG_V2248_1321[1]) else False) if shen_eq(symdic.symdic_shen_app, KL_ARG_V2248_1321[0]) else False) if shen_consp(KL_ARG_V2248_1321) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45l]) if True else shen_simple_error('condition failure')))))))))
shen_add_fun('shen.insert-l', shen_insertx45l)

@tail_recursion
def shen_factorx45cn(KL_ARG_V2249_1322):
    global symdic
    return ([symdic.symdic_kl_cn, [(KL_ARG_V2249_1322[1][0] + KL_ARG_V2249_1322[1][1][0][1][0]), KL_ARG_V2249_1322[1][1][0][1][1]]] if (((((((((((isinstance(KL_ARG_V2249_1322[1][1][0][1][0], str) if isinstance(KL_ARG_V2249_1322[1][0], str) else False) if shen_eq([], KL_ARG_V2249_1322[1][1][1]) else False) if shen_eq([], KL_ARG_V2249_1322[1][1][0][1][1][1]) else False) if shen_consp(KL_ARG_V2249_1322[1][1][0][1][1]) else False) if shen_consp(KL_ARG_V2249_1322[1][1][0][1]) else False) if shen_eq(symdic.symdic_kl_cn, KL_ARG_V2249_1322[1][1][0][0]) else False) if shen_consp(KL_ARG_V2249_1322[1][1][0]) else False) if shen_consp(KL_ARG_V2249_1322[1][1]) else False) if shen_consp(KL_ARG_V2249_1322[1]) else False) if shen_eq(symdic.symdic_kl_cn, KL_ARG_V2249_1322[0]) else False) if shen_consp(KL_ARG_V2249_1322) else False) else (KL_ARG_V2249_1322 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.factor-cn', shen_factorx45cn)

@tail_recursion
def shen_procx45nl(KL_ARG_V2250_1323):
    global symdic
    return ('' if shen_eq('', KL_ARG_V2250_1323) else ((chr(10) + tco_apply(shen_procx45nl, [KL_ARG_V2250_1323[1:][1:]])) if (((shen_eq('%', KL_ARG_V2250_1323[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2250_1323[1:]]) else False) if shen_eq('~', KL_ARG_V2250_1323[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2250_1323]) else False) else ((KL_ARG_V2250_1323[0] + tco_apply(shen_procx45nl, [KL_ARG_V2250_1323[1:]])) if tco_apply(shen_x43stringx63, [KL_ARG_V2250_1323]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_procx45nl]) if True else shen_simple_error('condition failure')))))
shen_add_fun('shen.proc-nl', shen_procx45nl)

@tail_recursion
def shen_mkstrx45r(KL_ARG_V2251_1324, KL_ARG_V2252_1325):
    global symdic
    return (KL_ARG_V2251_1324 if shen_eq([], KL_ARG_V2252_1325) else (tail_call(shen_mkstrx45r, [[symdic.symdic_shen_insert, [KL_ARG_V2252_1325[0], [KL_ARG_V2251_1324, []]]], KL_ARG_V2252_1325[1]]) if shen_consp(KL_ARG_V2252_1325) else (tail_call(shen_sysx45error, [symdic.symdic_shen_mkstrx45r]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.mkstr-r', shen_mkstrx45r)

@tail_recursion
def shen_insert(KL_ARG_V2253_1326, KL_ARG_V2254_1327):
    global symdic
    return tail_call(shen_insertx45h, [KL_ARG_V2253_1326, KL_ARG_V2254_1327, ''])
shen_add_fun('shen.insert', shen_insert)

@tail_recursion
def shen_insertx45h(KL_ARG_V2257_1328, KL_ARG_V2258_1329, KL_ARG_V2259_1330):
    global symdic
    return (KL_ARG_V2259_1330 if shen_eq('', KL_ARG_V2258_1329) else ((KL_ARG_V2259_1330 + tco_apply(shen_app, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:][1:], symdic.symdic_shen_a])) if (((shen_eq('A', KL_ARG_V2258_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329[1:]]) else False) if shen_eq('~', KL_ARG_V2258_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else False) else ((KL_ARG_V2259_1330 + tco_apply(shen_app, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:][1:], symdic.symdic_shen_r])) if (((shen_eq('R', KL_ARG_V2258_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329[1:]]) else False) if shen_eq('~', KL_ARG_V2258_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else False) else ((KL_ARG_V2259_1330 + tco_apply(shen_app, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:][1:], symdic.symdic_shen_s])) if (((shen_eq('S', KL_ARG_V2258_1329[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329[1:]]) else False) if shen_eq('~', KL_ARG_V2258_1329[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else False) else (tail_call(shen_insertx45h, [KL_ARG_V2257_1328, KL_ARG_V2258_1329[1:], (KL_ARG_V2259_1330 + KL_ARG_V2258_1329[0])]) if tco_apply(shen_x43stringx63, [KL_ARG_V2258_1329]) else (tail_call(shen_sysx45error, [symdic.symdic_shen_insertx45h]) if True else shen_simple_error('condition failure')))))))
shen_add_fun('shen.insert-h', shen_insertx45h)

@tail_recursion
def shen_app(KL_ARG_V2260_1331, KL_ARG_V2261_1332, KL_ARG_V2262_1333):
    global symdic
    return (tco_apply(shen_argx45x62str, [KL_ARG_V2260_1331, KL_ARG_V2262_1333]) + KL_ARG_V2261_1332)
shen_add_fun('shen.app', shen_app)

@tail_recursion
def shen_argx45x62str(KL_ARG_V2268_1334, KL_ARG_V2269_1335):
    global symdic
    return ('...' if shen_eq(KL_ARG_V2268_1334, tco_apply(kl_fail, [])) else (tail_call(shen_listx45x62str, [KL_ARG_V2268_1334, KL_ARG_V2269_1335]) if tco_apply(shen_listx63, [KL_ARG_V2268_1334]) else (tail_call(shen_strx45x62str, [KL_ARG_V2268_1334, KL_ARG_V2269_1335]) if isinstance(KL_ARG_V2268_1334, str) else (tail_call(shen_vectorx45x62str, [KL_ARG_V2268_1334, KL_ARG_V2269_1335]) if shen_absvectorp(KL_ARG_V2268_1334) else (tail_call(shen_atomx45x62str, [KL_ARG_V2268_1334]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.arg->str', shen_argx45x62str)

@tail_recursion
def shen_listx45x62str(KL_ARG_V2270_1336, KL_ARG_V2271_1337):
    global symdic
    return (tail_call(kl_x64s, ['(', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2270_1336, symdic.symdic_shen_r, tco_apply(shen_maxseq, [])]), ')'])]) if shen_eq(symdic.symdic_shen_r, KL_ARG_V2271_1337) else (tail_call(kl_x64s, ['[', tco_apply(kl_x64s, [tco_apply(shen_iterx45list, [KL_ARG_V2270_1336, KL_ARG_V2271_1337, tco_apply(shen_maxseq, [])]), ']'])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.list->str', shen_listx45x62str)

@tail_recursion
def shen_maxseq():
    global symdic
    return shen_get(symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42)
shen_add_fun('shen.maxseq', shen_maxseq)

@tail_recursion
def shen_iterx45list(KL_ARG_V2282_1338, KL_ARG_V2283_1339, KL_ARG_V2284_1340):
    global symdic
    return ('' if shen_eq([], KL_ARG_V2282_1338) else ('... etc' if shen_eq(0, KL_ARG_V2284_1340) else (tail_call(shen_argx45x62str, [KL_ARG_V2282_1338[0], KL_ARG_V2283_1339]) if (shen_eq([], KL_ARG_V2282_1338[1]) if shen_consp(KL_ARG_V2282_1338) else False) else (tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [KL_ARG_V2282_1338[0], KL_ARG_V2283_1339]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45list, [KL_ARG_V2282_1338[1], KL_ARG_V2283_1339, (KL_ARG_V2284_1340 - 1)])])]) if shen_consp(KL_ARG_V2282_1338) else (tail_call(kl_x64s, ['|', tco_apply(kl_x64s, [' ', tco_apply(shen_argx45x62str, [KL_ARG_V2282_1338, KL_ARG_V2283_1339])])]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.iter-list', shen_iterx45list)

@tail_recursion
def shen_strx45x62str(KL_ARG_V2289_1341, KL_ARG_V2290_1342):
    global symdic
    return (KL_ARG_V2289_1341 if shen_eq(symdic.symdic_shen_a, KL_ARG_V2290_1342) else (tail_call(kl_x64s, [chr(34), tco_apply(kl_x64s, [KL_ARG_V2289_1341, chr(34)])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.str->str', shen_strx45x62str)

@tail_recursion
def shen_vectorx45x62str(KL_ARG_V2291_1343, KL_ARG_V2292_1344):
    global symdic
    return (tail_call(shen_absvector_get(KL_ARG_V2291_1343, 0), [KL_ARG_V2291_1343]) if tco_apply(shen_printx45vectorx63, [KL_ARG_V2291_1343]) else (tail_call(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2291_1343, 1, KL_ARG_V2292_1344, tco_apply(shen_maxseq, [])]), '>'])]) if tco_apply(kl_vectorx63, [KL_ARG_V2291_1343]) else tail_call(kl_x64s, ['<', tco_apply(kl_x64s, ['<', tco_apply(kl_x64s, [tco_apply(shen_iterx45vector, [KL_ARG_V2291_1343, 0, KL_ARG_V2292_1344, tco_apply(shen_maxseq, [])]), '>>'])])])))
shen_add_fun('shen.vector->str', shen_vectorx45x62str)

@tail_recursion
def shen_printx45vectorx63(KL_ARG_V2293_1345):

    class KL_Context:
        KL_LOC_Zero_1346 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Zero_1346', shen_absvector_get(KL_ARG_V2293_1345, 0)), (True if shen_eq(KL_CTX.KL_LOC_Zero_1346, symdic.symdic_shen_tuple) else (True if shen_eq(KL_CTX.KL_LOC_Zero_1346, symdic.symdic_shen_pvar) else (tail_call(shen_fboundx63, [KL_CTX.KL_LOC_Zero_1346]) if (not isinstance(KL_CTX.KL_LOC_Zero_1346, numbers.Number)) else False)))][(-1)]
shen_add_fun('shen.print-vector?', shen_printx45vectorx63)

@tail_recursion
def shen_fboundx63(KL_ARG_V2294_1347):
    global symdic
    return shen_try_except((lambda : [tco_apply(kl_ps, [KL_ARG_V2294_1347]), True][(-1)]), (lambda KL_ARG_E_1348: False))
shen_add_fun('shen.fbound?', shen_fboundx63)

@tail_recursion
def shen_tuple(KL_ARG_V2295_1349):
    global symdic
    return ('(@p ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2295_1349, 1), (' ' + tco_apply(shen_app, [shen_absvector_get(KL_ARG_V2295_1349, 2), ')', symdic.symdic_shen_s])), symdic.symdic_shen_s]))
shen_add_fun('shen.tuple', shen_tuple)

@tail_recursion
def shen_iterx45vector(KL_ARG_V2302_1350, KL_ARG_V2303_1351, KL_ARG_V2304_1352, KL_ARG_V2305_1353):

    class KL_Context:
        KL_LOC_Item_1354 = None
        KL_LOC_Next_1356 = None
    KL_CTX = KL_Context()
    global symdic
    return ('... etc' if shen_eq(0, KL_ARG_V2305_1353) else ([setattr(KL_CTX, 'KL_LOC_Item_1354', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2302_1350, KL_ARG_V2303_1351)), (lambda KL_ARG_E_1355: symdic.symdic_shen_outx45ofx45bounds))), [setattr(KL_CTX, 'KL_LOC_Next_1356', shen_try_except((lambda : shen_absvector_get(KL_ARG_V2302_1350, (KL_ARG_V2303_1351 + 1))), (lambda KL_ARG_E_1357: symdic.symdic_shen_outx45ofx45bounds))), ('' if shen_eq(KL_CTX.KL_LOC_Item_1354, symdic.symdic_shen_outx45ofx45bounds) else (tail_call(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1354, KL_ARG_V2304_1352]) if shen_eq(KL_CTX.KL_LOC_Next_1356, symdic.symdic_shen_outx45ofx45bounds) else tail_call(kl_x64s, [tco_apply(shen_argx45x62str, [KL_CTX.KL_LOC_Item_1354, KL_ARG_V2304_1352]), tco_apply(kl_x64s, [' ', tco_apply(shen_iterx45vector, [KL_ARG_V2302_1350, (KL_ARG_V2303_1351 + 1), KL_ARG_V2304_1352, (KL_ARG_V2305_1353 - 1)])])])))][(-1)]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.iter-vector', shen_iterx45vector)

@tail_recursion
def shen_atomx45x62str(KL_ARG_V2306_1358):
    global symdic
    return shen_try_except((lambda : str(KL_ARG_V2306_1358)), (lambda KL_ARG_E_1359: tail_call(shen_funexstring, [])))
shen_add_fun('shen.atom->str', shen_atomx45x62str)

@tail_recursion
def shen_funexstring():
    global symdic
    return tail_call(kl_x64s, ['\x10', tco_apply(kl_x64s, ['f', tco_apply(kl_x64s, ['u', tco_apply(kl_x64s, ['n', tco_apply(kl_x64s, ['e', tco_apply(kl_x64s, [tco_apply(shen_argx45x62str, [tco_apply(kl_gensym, [shen_intern('x')]), symdic.symdic_shen_a]), '\x11'])])])])])])
shen_add_fun('shen.funexstring', shen_funexstring)

@tail_recursion
def shen_listx63(KL_ARG_V2307_1360):
    global symdic
    return (True if tco_apply(kl_emptyx63, [KL_ARG_V2307_1360]) else shen_consp(KL_ARG_V2307_1360))
shen_add_fun('shen.list?', shen_listx63)


#============================== macros.kl==============================



@tail_recursion
def kl_macroexpand(KL_ARG_V869_1361):

    class KL_Context:
        KL_LOC_Y_1362 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Y_1362', tco_apply(shen_compose, [shen_get(symdic.symdic_kl_x42macrosx42), KL_ARG_V869_1361])), (KL_ARG_V869_1361 if shen_eq(KL_ARG_V869_1361, KL_CTX.KL_LOC_Y_1362) else tail_call(shen_walk, [symdic.symdic_kl_macroexpand, KL_CTX.KL_LOC_Y_1362]))][(-1)]
shen_add_fun('macroexpand', kl_macroexpand)
shen_set(symdic.symdic_kl_x42macrosx42, [symdic.symdic_shen_timerx45macro, [symdic.symdic_shen_casesx45macro, [symdic.symdic_shen_absx45macro, [symdic.symdic_shen_putx47getx45macro, [symdic.symdic_shen_compilex45macro, [symdic.symdic_shen_datatypex45macro, [symdic.symdic_shen_letx45macro, [symdic.symdic_shen_assocx45macro, [symdic.symdic_shen_makex45stringx45macro, [symdic.symdic_shen_outputx45macro, [symdic.symdic_shen_errorx45macro, [symdic.symdic_shen_prologx45macro, [symdic.symdic_shen_synonymsx45macro, [symdic.symdic_shen_nlx45macro, [symdic.symdic_shen_x64sx45macro, [symdic.symdic_shen_defmacrox45macro, [symdic.symdic_shen_defprologx45macro, [symdic.symdic_shen_functionx45macro, []]]]]]]]]]]]]]]]]]])

@tail_recursion
def shen_errorx45macro(KL_ARG_V870_1363):
    global symdic
    return ([symdic.symdic_kl_simplex45error, [tco_apply(shen_mkstr, [KL_ARG_V870_1363[1][0], KL_ARG_V870_1363[1][1]]), []]] if ((shen_consp(KL_ARG_V870_1363[1]) if shen_eq(symdic.symdic_kl_error, KL_ARG_V870_1363[0]) else False) if shen_consp(KL_ARG_V870_1363) else False) else (KL_ARG_V870_1363 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.error-macro', shen_errorx45macro)

@tail_recursion
def shen_outputx45macro(KL_ARG_V871_1364):
    global symdic
    return ([symdic.symdic_shen_prhush, [tco_apply(shen_mkstr, [KL_ARG_V871_1364[1][0], KL_ARG_V871_1364[1][1]]), [[symdic.symdic_kl_stoutput, []], []]]] if ((shen_consp(KL_ARG_V871_1364[1]) if shen_eq(symdic.symdic_kl_output, KL_ARG_V871_1364[0]) else False) if shen_consp(KL_ARG_V871_1364) else False) else (KL_ARG_V871_1364 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.output-macro', shen_outputx45macro)

@tail_recursion
def shen_makex45stringx45macro(KL_ARG_V872_1365):
    global symdic
    return (tail_call(shen_mkstr, [KL_ARG_V872_1365[1][0], KL_ARG_V872_1365[1][1]]) if ((shen_consp(KL_ARG_V872_1365[1]) if shen_eq(symdic.symdic_kl_makex45string, KL_ARG_V872_1365[0]) else False) if shen_consp(KL_ARG_V872_1365) else False) else (KL_ARG_V872_1365 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.make-string-macro', shen_makex45stringx45macro)

@tail_recursion
def shen_compose(KL_ARG_V873_1366, KL_ARG_V874_1367):
    global symdic
    return (KL_ARG_V874_1367 if shen_eq([], KL_ARG_V873_1366) else (tail_call(shen_compose, [KL_ARG_V873_1366[1], tco_apply(KL_ARG_V873_1366[0], [KL_ARG_V874_1367])]) if shen_consp(KL_ARG_V873_1366) else (tail_call(shen_sysx45error, [symdic.symdic_shen_compose]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.compose', shen_compose)

@tail_recursion
def shen_compilex45macro(KL_ARG_V875_1368):
    global symdic
    return ([symdic.symdic_kl_compile, [KL_ARG_V875_1368[1][0], [KL_ARG_V875_1368[1][1][0], [[symdic.symdic_kl_lambda, [symdic.symdic_E, [[symdic.symdic_kl_if, [[symdic.symdic_kl_consx63, [symdic.symdic_E, []]], [[symdic.symdic_kl_error, ['parse error here: ~S~%', [symdic.symdic_E, []]]], [[symdic.symdic_kl_error, ['parse error~%', []]], []]]]], []]]], []]]]] if ((((shen_eq([], KL_ARG_V875_1368[1][1][1]) if shen_consp(KL_ARG_V875_1368[1][1]) else False) if shen_consp(KL_ARG_V875_1368[1]) else False) if shen_eq(symdic.symdic_kl_compile, KL_ARG_V875_1368[0]) else False) if shen_consp(KL_ARG_V875_1368) else False) else (KL_ARG_V875_1368 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.compile-macro', shen_compilex45macro)

@tail_recursion
def shen_prologx45macro(KL_ARG_V876_1369):
    global symdic
    return ([symdic.symdic_shen_intprolog, [tco_apply(shen_prologx45form, [KL_ARG_V876_1369[1]]), []]] if (shen_eq(symdic.symdic_kl_prologx63, KL_ARG_V876_1369[0]) if shen_consp(KL_ARG_V876_1369) else False) else (KL_ARG_V876_1369 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.prolog-macro', shen_prologx45macro)

@tail_recursion
def shen_defprologx45macro(KL_ARG_V877_1370):
    global symdic
    return (tail_call(kl_compile, [symdic.symdic_shen_x60defprologx62, KL_ARG_V877_1370[1], (lambda KL_ARG_Y_1371: tail_call(shen_prologx45error, [KL_ARG_V877_1370[1][0], KL_ARG_Y_1371]))]) if ((shen_consp(KL_ARG_V877_1370[1]) if shen_eq(symdic.symdic_kl_defprolog, KL_ARG_V877_1370[0]) else False) if shen_consp(KL_ARG_V877_1370) else False) else (KL_ARG_V877_1370 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.defprolog-macro', shen_defprologx45macro)

@tail_recursion
def shen_prologx45form(KL_ARG_V878_1372):
    global symdic
    return tail_call(shen_cons_form, [tco_apply(kl_map, [symdic.symdic_shen_cons_form, KL_ARG_V878_1372])])
shen_add_fun('shen.prolog-form', shen_prologx45form)

@tail_recursion
def shen_datatypex45macro(KL_ARG_V879_1373):
    global symdic
    return ([symdic.symdic_shen_processx45datatype, [tco_apply(shen_internx45type, [KL_ARG_V879_1373[1][0]]), [[symdic.symdic_kl_compile, [[symdic.symdic_kl_function, [symdic.symdic_shen_x60datatypex45rulesx62, []]], [tco_apply(shen_rcons_form, [KL_ARG_V879_1373[1][1]]), [[symdic.symdic_kl_function, [symdic.symdic_shen_datatypex45error, []]], []]]]], []]]] if ((shen_consp(KL_ARG_V879_1373[1]) if shen_eq(symdic.symdic_kl_datatype, KL_ARG_V879_1373[0]) else False) if shen_consp(KL_ARG_V879_1373) else False) else (KL_ARG_V879_1373 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.datatype-macro', shen_datatypex45macro)

@tail_recursion
def shen_internx45type(KL_ARG_V880_1374):
    global symdic
    return shen_intern(('type#' + str(KL_ARG_V880_1374)))
shen_add_fun('shen.intern-type', shen_internx45type)

@tail_recursion
def shen_defmacrox45macro(KL_ARG_V881_1375):

    class KL_Context:
        KL_LOC_Macro_1376 = None
        KL_LOC_Declare_1377 = None
        KL_LOC_Package_1378 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_Macro_1376', [symdic.symdic_kl_define, [KL_ARG_V881_1375[1][0], tco_apply(kl_append, [KL_ARG_V881_1375[1][1], [symdic.symdic_X, [symdic.symdic_kl_x45x62, [symdic.symdic_X, []]]]])]]), [setattr(KL_CTX, 'KL_LOC_Declare_1377', [symdic.symdic_kl_do, [[symdic.symdic_kl_set, [symdic.symdic_kl_x42macrosx42, [[symdic.symdic_kl_adjoin, [KL_ARG_V881_1375[1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42macrosx42, []]], []]]], []]]], [symdic.symdic_kl_macro, []]]]), [setattr(KL_CTX, 'KL_LOC_Package_1378', [symdic.symdic_kl_package, [symdic.symdic_kl_null, [[], [KL_CTX.KL_LOC_Declare_1377, [KL_CTX.KL_LOC_Macro_1376, []]]]]]), KL_CTX.KL_LOC_Package_1378][(-1)]][(-1)]][(-1)] if ((shen_consp(KL_ARG_V881_1375[1]) if shen_eq(symdic.symdic_kl_defmacro, KL_ARG_V881_1375[0]) else False) if shen_consp(KL_ARG_V881_1375) else False) else (KL_ARG_V881_1375 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.defmacro-macro', shen_defmacrox45macro)

@tail_recursion
def shen_x60defmacrox62(KL_ARG_V886_1379):

    class KL_Context:
        KL_LOC_Result_1380 = None
        KL_LOC_Parse_shen_x60namex62_1381 = None
        KL_LOC_Parse_shen_x60macrorulesx62_1382 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1380', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60namex62_1381', tco_apply(shen_x60namex62, [KL_ARG_V886_1379])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulesx62_1382', tco_apply(shen_x60macrorulesx62, [KL_CTX.KL_LOC_Parse_shen_x60namex62_1381])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1382[0], [symdic.symdic_kl_define, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60namex62_1381]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1382])]]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1382)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60namex62_1381)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1380, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1380)][(-1)]
shen_add_fun('shen.<defmacro>', shen_x60defmacrox62)

@tail_recursion
def shen_x60macrorulesx62(KL_ARG_V891_1383):

    class KL_Context:
        KL_LOC_Result_1384 = None
        KL_LOC_Parse_shen_x60macrorulex62_1385 = None
        KL_LOC_Parse_shen_x60macrorulesx62_1386 = None
        KL_LOC_Result_1387 = None
        KL_LOC_Parse_shen_x60macrorulex62_1388 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1384', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulex62_1385', tco_apply(shen_x60macrorulex62, [KL_ARG_V891_1383])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulesx62_1386', tco_apply(shen_x60macrorulesx62, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1385])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1386[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1385]), tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1386]), []])])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulesx62_1386)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1385)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1387', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macrorulex62_1388', tco_apply(shen_x60macrorulex62, [KL_ARG_V891_1383])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1388[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1388]), [symdic.symdic_Parse_X, [symdic.symdic_kl_x45x62, [symdic.symdic_Parse_X, []]]]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macrorulex62_1388)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1387, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1387)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1384, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1384)][(-1)]
shen_add_fun('shen.<macrorules>', shen_x60macrorulesx62)

@tail_recursion
def shen_x60macrorulex62(KL_ARG_V896_1389):

    class KL_Context:
        KL_LOC_Result_1390 = None
        KL_LOC_Parse_shen_x60patternsx62_1391 = None
        KL_LOC_Parse_shen_x60macroactionx62_1392 = None
        KL_LOC_Parse_shen_x60guardx62_1393 = None
        KL_LOC_Result_1394 = None
        KL_LOC_Parse_shen_x60patternsx62_1395 = None
        KL_LOC_Parse_shen_x60macroactionx62_1396 = None
        KL_LOC_Result_1397 = None
        KL_LOC_Parse_shen_x60patternsx62_1398 = None
        KL_LOC_Parse_shen_x60macroactionx62_1399 = None
        KL_LOC_Parse_shen_x60guardx62_1400 = None
        KL_LOC_Result_1401 = None
        KL_LOC_Parse_shen_x60patternsx62_1402 = None
        KL_LOC_Parse_shen_x60macroactionx62_1403 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1390', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1391', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1392', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_1393', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1393[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391]), [symdic.symdic_kl_x45x62, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392]), [symdic.symdic_kl_where, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1393]), []])]])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_1393)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1392)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1391)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1394', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1395', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1396', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1396[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395]), [symdic.symdic_kl_x45x62, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1396]), []])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1396)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x45x62, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1395)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1397', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1398', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1399', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398])])])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60guardx62_1400', tco_apply(shen_x60guardx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1400[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398]), [symdic.symdic_kl_x60x45, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399]), [symdic.symdic_kl_where, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60guardx62_1400]), []])]])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60guardx62_1400)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1399)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1398)) else tco_apply(kl_fail, []))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Result_1401', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60patternsx62_1402', tco_apply(shen_x60patternsx62, [KL_ARG_V896_1389])), (([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60macroactionx62_1403', tco_apply(shen_x60macroactionx62, [tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402[0][1], tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402])])])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1403[0], tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402]), [symdic.symdic_kl_x60x45, tco_apply(kl_append, [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1403]), []])]])]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60macroactionx62_1403)) else tco_apply(kl_fail, []))][(-1)] if (shen_eq(symdic.symdic_kl_x60x45, KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402[0][0]) if shen_consp(KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402[0]) else False) else tco_apply(kl_fail, [])) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60patternsx62_1402)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1401, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1401)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1397, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1397)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1394, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1394)][(-1)] if shen_eq(KL_CTX.KL_LOC_Result_1390, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1390)][(-1)]
shen_add_fun('shen.<macrorule>', shen_x60macrorulex62)

@tail_recursion
def shen_x60macroactionx62(KL_ARG_V901_1404):

    class KL_Context:
        KL_LOC_Result_1405 = None
        KL_LOC_Parse_shen_x60actionx62_1406 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_1405', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60actionx62_1406', tco_apply(shen_x60actionx62, [KL_ARG_V901_1404])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_1406[0], [[symdic.symdic_shen_walk, [[symdic.symdic_kl_function, [symdic.symdic_kl_macroexpand, []]], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60actionx62_1406]), []]]], []]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60actionx62_1406)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_1405, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_1405)][(-1)]
shen_add_fun('shen.<macroaction>', shen_x60macroactionx62)

@tail_recursion
def shen_x64sx45macro(KL_ARG_V902_1407):

    class KL_Context:
        KL_LOC_E_1408 = None
    KL_CTX = KL_Context()
    global symdic
    return ([symdic.symdic_kl_x64s, [KL_ARG_V902_1407[1][0], [tco_apply(shen_x64sx45macro, [[symdic.symdic_kl_x64s, KL_ARG_V902_1407[1][1]]]), []]]] if ((((shen_consp(KL_ARG_V902_1407[1][1][1]) if shen_consp(KL_ARG_V902_1407[1][1]) else False) if shen_consp(KL_ARG_V902_1407[1]) else False) if shen_eq(symdic.symdic_kl_x64s, KL_ARG_V902_1407[0]) else False) if shen_consp(KL_ARG_V902_1407) else False) else ([setattr(KL_CTX, 'KL_LOC_E_1408', tco_apply(kl_explode, [KL_ARG_V902_1407[1][0]])), (tail_call(shen_x64sx45macro, [[symdic.symdic_kl_x64s, tco_apply(kl_append, [KL_CTX.KL_LOC_E_1408, KL_ARG_V902_1407[1][1]])]]) if (tco_apply(kl_length, [KL_CTX.KL_LOC_E_1408]) > 1) else KL_ARG_V902_1407)][(-1)] if (((((isinstance(KL_ARG_V902_1407[1][0], str) if shen_eq([], KL_ARG_V902_1407[1][1][1]) else False) if shen_consp(KL_ARG_V902_1407[1][1]) else False) if shen_consp(KL_ARG_V902_1407[1]) else False) if shen_eq(symdic.symdic_kl_x64s, KL_ARG_V902_1407[0]) else False) if shen_consp(KL_ARG_V902_1407) else False) else (KL_ARG_V902_1407 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.@s-macro', shen_x64sx45macro)

@tail_recursion
def shen_synonymsx45macro(KL_ARG_V903_1409):
    global symdic
    return ([symdic.symdic_shen_synonymsx45help, [tco_apply(shen_rcons_form, [KL_ARG_V903_1409[1]]), []]] if (shen_eq(symdic.symdic_kl_synonyms, KL_ARG_V903_1409[0]) if shen_consp(KL_ARG_V903_1409) else False) else (KL_ARG_V903_1409 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.synonyms-macro', shen_synonymsx45macro)

@tail_recursion
def shen_nlx45macro(KL_ARG_V904_1410):
    global symdic
    return ([symdic.symdic_kl_nl, [1, []]] if ((shen_eq([], KL_ARG_V904_1410[1]) if shen_eq(symdic.symdic_kl_nl, KL_ARG_V904_1410[0]) else False) if shen_consp(KL_ARG_V904_1410) else False) else (KL_ARG_V904_1410 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.nl-macro', shen_nlx45macro)

@tail_recursion
def shen_assocx45macro(KL_ARG_V905_1411):
    global symdic
    return ([KL_ARG_V905_1411[0], [KL_ARG_V905_1411[1][0], [tco_apply(shen_assocx45macro, [[KL_ARG_V905_1411[0], KL_ARG_V905_1411[1][1]]]), []]]] if ((((tco_apply(kl_elementx63, [KL_ARG_V905_1411[0], [symdic.symdic_kl_x64p, [symdic.symdic_kl_x64v, [symdic.symdic_kl_append, [symdic.symdic_kl_and, [symdic.symdic_kl_or, [symdic.symdic_kl_x43, [symdic.symdic_kl_x42, [symdic.symdic_kl_do, []]]]]]]]]]) if shen_consp(KL_ARG_V905_1411[1][1][1]) else False) if shen_consp(KL_ARG_V905_1411[1][1]) else False) if shen_consp(KL_ARG_V905_1411[1]) else False) if shen_consp(KL_ARG_V905_1411) else False) else (KL_ARG_V905_1411 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.assoc-macro', shen_assocx45macro)

@tail_recursion
def shen_letx45macro(KL_ARG_V906_1412):
    global symdic
    return ([symdic.symdic_kl_let, [KL_ARG_V906_1412[1][0], [KL_ARG_V906_1412[1][1][0], [tco_apply(shen_letx45macro, [[symdic.symdic_kl_let, KL_ARG_V906_1412[1][1][1]]]), []]]]] if (((((shen_consp(KL_ARG_V906_1412[1][1][1][1]) if shen_consp(KL_ARG_V906_1412[1][1][1]) else False) if shen_consp(KL_ARG_V906_1412[1][1]) else False) if shen_consp(KL_ARG_V906_1412[1]) else False) if shen_eq(symdic.symdic_kl_let, KL_ARG_V906_1412[0]) else False) if shen_consp(KL_ARG_V906_1412) else False) else (KL_ARG_V906_1412 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.let-macro', shen_letx45macro)

@tail_recursion
def shen_absx45macro(KL_ARG_V907_1413):
    global symdic
    return ([symdic.symdic_kl_lambda, [KL_ARG_V907_1413[1][0], [tco_apply(shen_absx45macro, [[symdic.symdic_kl_x47_, KL_ARG_V907_1413[1][1]]]), []]]] if ((((shen_consp(KL_ARG_V907_1413[1][1][1]) if shen_consp(KL_ARG_V907_1413[1][1]) else False) if shen_consp(KL_ARG_V907_1413[1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V907_1413[0]) else False) if shen_consp(KL_ARG_V907_1413) else False) else ([symdic.symdic_kl_lambda, KL_ARG_V907_1413[1]] if ((((shen_eq([], KL_ARG_V907_1413[1][1][1]) if shen_consp(KL_ARG_V907_1413[1][1]) else False) if shen_consp(KL_ARG_V907_1413[1]) else False) if shen_eq(symdic.symdic_kl_x47_, KL_ARG_V907_1413[0]) else False) if shen_consp(KL_ARG_V907_1413) else False) else (KL_ARG_V907_1413 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.abs-macro', shen_absx45macro)

@tail_recursion
def shen_casesx45macro(KL_ARG_V910_1414):
    global symdic
    return (KL_ARG_V910_1414[1][1][0] if ((((shen_consp(KL_ARG_V910_1414[1][1]) if shen_eq(True, KL_ARG_V910_1414[1][0]) else False) if shen_consp(KL_ARG_V910_1414[1]) else False) if shen_eq(symdic.symdic_kl_cases, KL_ARG_V910_1414[0]) else False) if shen_consp(KL_ARG_V910_1414) else False) else ([symdic.symdic_kl_if, [KL_ARG_V910_1414[1][0], [KL_ARG_V910_1414[1][1][0], [[symdic.symdic_kl_simplex45error, ['error: cases exhausted', []]], []]]]] if ((((shen_eq([], KL_ARG_V910_1414[1][1][1]) if shen_consp(KL_ARG_V910_1414[1][1]) else False) if shen_consp(KL_ARG_V910_1414[1]) else False) if shen_eq(symdic.symdic_kl_cases, KL_ARG_V910_1414[0]) else False) if shen_consp(KL_ARG_V910_1414) else False) else ([symdic.symdic_kl_if, [KL_ARG_V910_1414[1][0], [KL_ARG_V910_1414[1][1][0], [tco_apply(shen_casesx45macro, [[symdic.symdic_kl_cases, KL_ARG_V910_1414[1][1][1]]]), []]]]] if (((shen_consp(KL_ARG_V910_1414[1][1]) if shen_consp(KL_ARG_V910_1414[1]) else False) if shen_eq(symdic.symdic_kl_cases, KL_ARG_V910_1414[0]) else False) if shen_consp(KL_ARG_V910_1414) else False) else (shen_simple_error('error: odd number of case elements\r\n') if (((shen_eq([], KL_ARG_V910_1414[1][1]) if shen_consp(KL_ARG_V910_1414[1]) else False) if shen_eq(symdic.symdic_kl_cases, KL_ARG_V910_1414[0]) else False) if shen_consp(KL_ARG_V910_1414) else False) else (KL_ARG_V910_1414 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.cases-macro', shen_casesx45macro)

@tail_recursion
def shen_timerx45macro(KL_ARG_V911_1415):
    global symdic
    return (tail_call(shen_letx45macro, [[symdic.symdic_kl_let, [symdic.symdic_Start, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Result, [KL_ARG_V911_1415[1][0], [symdic.symdic_Finish, [[symdic.symdic_kl_getx45time, [symdic.symdic_kl_run, []]], [symdic.symdic_Time, [[symdic.symdic_kl_x45, [symdic.symdic_Finish, [symdic.symdic_Start, []]]], [symdic.symdic_Message, [[symdic.symdic_shen_prhush, [[symdic.symdic_kl_cn, ['\r\nrun time: ', [[symdic.symdic_kl_cn, [[symdic.symdic_kl_str, [symdic.symdic_Time, []]], [' secs\r\n', []]]], []]]], [[symdic.symdic_kl_stoutput, []], []]]], [symdic.symdic_Result, []]]]]]]]]]]]]]) if (((shen_eq([], KL_ARG_V911_1415[1][1]) if shen_consp(KL_ARG_V911_1415[1]) else False) if shen_eq(symdic.symdic_kl_time, KL_ARG_V911_1415[0]) else False) if shen_consp(KL_ARG_V911_1415) else False) else (KL_ARG_V911_1415 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.timer-macro', shen_timerx45macro)

@tail_recursion
def shen_tuplex45up(KL_ARG_V912_1416):
    global symdic
    return ([symdic.symdic_kl_x64p, [KL_ARG_V912_1416[0], [tco_apply(shen_tuplex45up, [KL_ARG_V912_1416[1]]), []]]] if shen_consp(KL_ARG_V912_1416) else (KL_ARG_V912_1416 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.tuple-up', shen_tuplex45up)

@tail_recursion
def shen_putx47getx45macro(KL_ARG_V913_1417):
    global symdic
    return ([symdic.symdic_kl_put, [KL_ARG_V913_1417[1][0], [KL_ARG_V913_1417[1][1][0], [KL_ARG_V913_1417[1][1][1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42propertyx45vectorx42, []]], []]]]]] if (((((shen_eq([], KL_ARG_V913_1417[1][1][1][1]) if shen_consp(KL_ARG_V913_1417[1][1][1]) else False) if shen_consp(KL_ARG_V913_1417[1][1]) else False) if shen_consp(KL_ARG_V913_1417[1]) else False) if shen_eq(symdic.symdic_kl_put, KL_ARG_V913_1417[0]) else False) if shen_consp(KL_ARG_V913_1417) else False) else ([symdic.symdic_kl_get, [KL_ARG_V913_1417[1][0], [KL_ARG_V913_1417[1][1][0], [[symdic.symdic_kl_value, [symdic.symdic_kl_x42propertyx45vectorx42, []]], []]]]] if ((((shen_eq([], KL_ARG_V913_1417[1][1][1]) if shen_consp(KL_ARG_V913_1417[1][1]) else False) if shen_consp(KL_ARG_V913_1417[1]) else False) if shen_eq(symdic.symdic_kl_get, KL_ARG_V913_1417[0]) else False) if shen_consp(KL_ARG_V913_1417) else False) else (KL_ARG_V913_1417 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.put/get-macro', shen_putx47getx45macro)

@tail_recursion
def shen_functionx45macro(KL_ARG_V914_1418):
    global symdic
    return (tail_call(shen_functionx45abstraction, [KL_ARG_V914_1418[1][0], tco_apply(kl_arity, [KL_ARG_V914_1418[1][0]])]) if (((shen_eq([], KL_ARG_V914_1418[1][1]) if shen_consp(KL_ARG_V914_1418[1]) else False) if shen_eq(symdic.symdic_kl_function, KL_ARG_V914_1418[0]) else False) if shen_consp(KL_ARG_V914_1418) else False) else (KL_ARG_V914_1418 if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-macro', shen_functionx45macro)

@tail_recursion
def shen_functionx45abstraction(KL_ARG_V915_1419, KL_ARG_V916_1420):
    global symdic
    return ([symdic.symdic_kl_freeze, [KL_ARG_V915_1419, []]] if shen_eq(0, KL_ARG_V916_1420) else (KL_ARG_V915_1419 if shen_eq((-1), KL_ARG_V916_1420) else (tail_call(shen_functionx45abstractionx45help, [KL_ARG_V915_1419, KL_ARG_V916_1420, []]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.function-abstraction', shen_functionx45abstraction)

@tail_recursion
def shen_functionx45abstractionx45help(KL_ARG_V917_1421, KL_ARG_V918_1422, KL_ARG_V919_1423):

    class KL_Context:
        KL_LOC_X_1424 = None
    KL_CTX = KL_Context()
    global symdic
    return ([KL_ARG_V917_1421, KL_ARG_V919_1423] if shen_eq(0, KL_ARG_V918_1422) else ([setattr(KL_CTX, 'KL_LOC_X_1424', tco_apply(kl_gensym, [symdic.symdic_V])), [symdic.symdic_kl_x47_, [KL_CTX.KL_LOC_X_1424, [tco_apply(shen_functionx45abstractionx45help, [KL_ARG_V917_1421, (KL_ARG_V918_1422 - 1), tco_apply(kl_append, [KL_ARG_V919_1423, [KL_CTX.KL_LOC_X_1424, []]])]), []]]]][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.function-abstraction-help', shen_functionx45abstractionx45help)

@tail_recursion
def kl_undefmacro(KL_ARG_V920_1425):
    global symdic
    return [shen_set(symdic.symdic_kl_x42macrosx42, tco_apply(kl_remove, [KL_ARG_V920_1425, shen_get(symdic.symdic_kl_x42macrosx42)])), KL_ARG_V920_1425][(-1)]
shen_add_fun('undefmacro', kl_undefmacro)


#============================== declarations.kl==============================


shen_set(symdic.symdic_shen_x42installingx45klx42, False)
shen_set(symdic.symdic_shen_x42historyx42, [])
shen_set(symdic.symdic_shen_x42tcx42, False)
shen_set(symdic.symdic_kl_x42propertyx45vectorx42, tco_apply(kl_vector, [20000]))
shen_set(symdic.symdic_shen_x42processx45counterx42, 0)
shen_set(symdic.symdic_shen_x42varcounterx42, tco_apply(kl_vector, [1000]))
shen_set(symdic.symdic_shen_x42prologvectorsx42, tco_apply(kl_vector, [1000]))
shen_set(symdic.symdic_shen_x42readerx45macrosx42, [])
shen_set(symdic.symdic_kl_x42homex45directoryx42, [])
shen_set(symdic.symdic_shen_x42gensymx42, 0)
shen_set(symdic.symdic_shen_x42trackingx42, [])
shen_set(symdic.symdic_kl_x42homex45directoryx42, '')
shen_set(symdic.symdic_shen_x42alphabetx42, [symdic.symdic_A, [symdic.symdic_B, [symdic.symdic_C, [symdic.symdic_D, [symdic.symdic_E, [symdic.symdic_F, [symdic.symdic_G, [symdic.symdic_H, [symdic.symdic_I, [symdic.symdic_J, [symdic.symdic_K, [symdic.symdic_L, [symdic.symdic_M, [symdic.symdic_N, [symdic.symdic_O, [symdic.symdic_P, [symdic.symdic_Q, [symdic.symdic_R, [symdic.symdic_S, [symdic.symdic_T, [symdic.symdic_U, [symdic.symdic_V, [symdic.symdic_W, [symdic.symdic_X, [symdic.symdic_Y, [symdic.symdic_Z, []]]]]]]]]]]]]]]]]]]]]]]]]]])
shen_set(symdic.symdic_shen_x42specialx42, [symdic.symdic_kl_x64p, [symdic.symdic_kl_x64s, [symdic.symdic_kl_x64v, [symdic.symdic_kl_cons, [symdic.symdic_kl_lambda, [symdic.symdic_kl_let, [symdic.symdic_kl_type, [symdic.symdic_kl_where, [symdic.symdic_kl_set, [symdic.symdic_kl_open, []]]]]]]]]]])
shen_set(symdic.symdic_shen_x42extraspecialx42, [symdic.symdic_kl_define, [symdic.symdic_shen_processx45datatype, [symdic.symdic_kl_inputx43, [symdic.symdic_kl_defcc, [symdic.symdic_readx43, []]]]]])
shen_set(symdic.symdic_shen_x42spyx42, False)
shen_set(symdic.symdic_shen_x42datatypesx42, [])
shen_set(symdic.symdic_shen_x42alldatatypesx42, [])
shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, True)
shen_set(symdic.symdic_shen_x42synonymsx42, [])
shen_set(symdic.symdic_shen_x42systemx42, [])
shen_set(symdic.symdic_shen_x42signedfuncsx42, [])
shen_set(symdic.symdic_shen_x42maxcomplexityx42, 128)
shen_set(symdic.symdic_shen_x42occursx42, True)
shen_set(symdic.symdic_shen_x42maxinferencesx42, 1000000)
shen_set(symdic.symdic_kl_x42maximumx45printx45sequencex45sizex42, 20)
shen_set(symdic.symdic_shen_x42catchx42, 0)
shen_set(symdic.symdic_shen_x42callx42, 0)
shen_set(symdic.symdic_shen_x42infsx42, 0)
shen_set(symdic.symdic_x42hushx42, False)
shen_set(symdic.symdic_shen_x42optimisex42, False)

@tail_recursion
def shen_initialise_arity_table(KL_ARG_V822_1426):

    class KL_Context:
        KL_LOC_DecArity_1427 = None
    KL_CTX = KL_Context()
    global symdic
    return ([] if shen_eq([], KL_ARG_V822_1426) else ([setattr(KL_CTX, 'KL_LOC_DecArity_1427', tco_apply(kl_put, [KL_ARG_V822_1426[0], symdic.symdic_kl_arity, KL_ARG_V822_1426[1][0], shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(shen_initialise_arity_table, [KL_ARG_V822_1426[1][1]])][(-1)] if (shen_consp(KL_ARG_V822_1426[1]) if shen_consp(KL_ARG_V822_1426) else False) else (tail_call(shen_sysx45error, [symdic.symdic_shen_initialise_arity_table]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.initialise_arity_table', shen_initialise_arity_table)

@tail_recursion
def kl_arity(KL_ARG_V823_1428):
    global symdic
    return shen_try_except((lambda : tco_apply(kl_get, [KL_ARG_V823_1428, symdic.symdic_kl_arity, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), (lambda KL_ARG_E_1429: (-1)))
shen_add_fun('arity', kl_arity)

@tail_recursion
def kl_systemf(KL_ARG_V824_1430):

    class KL_Context:
        KL_LOC_Shen_1431 = None
        KL_LOC_External_1432 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Shen_1431', shen_intern('shen')), [setattr(KL_CTX, 'KL_LOC_External_1432', tco_apply(kl_get, [KL_CTX.KL_LOC_Shen_1431, symdic.symdic_shen_externalx45symbols, shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])), tail_call(kl_put, [KL_CTX.KL_LOC_Shen_1431, symdic.symdic_shen_externalx45symbols, tco_apply(kl_adjoin, [KL_ARG_V824_1430, KL_CTX.KL_LOC_External_1432]), shen_get(symdic.symdic_kl_x42propertyx45vectorx42)])][(-1)]][(-1)]
shen_add_fun('systemf', kl_systemf)

@tail_recursion
def kl_adjoin(KL_ARG_V825_1433, KL_ARG_V826_1434):
    global symdic
    return (KL_ARG_V826_1434 if tco_apply(kl_elementx63, [KL_ARG_V825_1433, KL_ARG_V826_1434]) else [KL_ARG_V825_1433, KL_ARG_V826_1434])
shen_add_fun('adjoin', kl_adjoin)

@tail_recursion
def kl_specialise(KL_ARG_V827_1435):
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, [KL_ARG_V827_1435, shen_get(symdic.symdic_shen_x42specialx42)]), KL_ARG_V827_1435][(-1)]
shen_add_fun('specialise', kl_specialise)

@tail_recursion
def kl_unspecialise(KL_ARG_V828_1436):
    global symdic
    return [shen_set(symdic.symdic_shen_x42specialx42, tco_apply(kl_remove, [KL_ARG_V828_1436, shen_get(symdic.symdic_shen_x42specialx42)])), KL_ARG_V828_1436][(-1)]
shen_add_fun('unspecialise', kl_unspecialise)


#============================== types.kl==============================



@tail_recursion
def kl_declare(KL_ARG_V2131_1437, KL_ARG_V2132_1438):

    class KL_Context:
        KL_LOC_Record_1439 = None
        KL_LOC_Variancy_1440 = None
        KL_LOC_Type_1442 = None
        KL_LOC_Fx42_1443 = None
        KL_LOC_Parameters_1444 = None
        KL_LOC_Clause_1445 = None
        KL_LOC_AUM_instruction_1446 = None
        KL_LOC_Code_1447 = None
        KL_LOC_ShenDef_1448 = None
        KL_LOC_Eval_1449 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Record_1439', shen_set(symdic.symdic_shen_x42signedfuncsx42, [[KL_ARG_V2131_1437, KL_ARG_V2132_1438], shen_get(symdic.symdic_shen_x42signedfuncsx42)])), [setattr(KL_CTX, 'KL_LOC_Variancy_1440', shen_try_except((lambda : tco_apply(shen_variancyx45test, [KL_ARG_V2131_1437, KL_ARG_V2132_1438])), (lambda KL_ARG_E_1441: symdic.symdic_shen_skip))), [setattr(KL_CTX, 'KL_LOC_Type_1442', tco_apply(shen_rcons_form, [tco_apply(shen_demodulate, [KL_ARG_V2132_1438])])), [setattr(KL_CTX, 'KL_LOC_Fx42_1443', tco_apply(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2131_1437])), [setattr(KL_CTX, 'KL_LOC_Parameters_1444', tco_apply(shen_parameters, [1])), [setattr(KL_CTX, 'KL_LOC_Clause_1445', [[KL_CTX.KL_LOC_Fx42_1443, [symdic.symdic_X, []]], [symdic.symdic_kl_x58x45, [[[symdic.symdic_kl_unifyx33, [symdic.symdic_X, [KL_CTX.KL_LOC_Type_1442, []]]], []], []]]]), [setattr(KL_CTX, 'KL_LOC_AUM_instruction_1446', tco_apply(shen_aum, [KL_CTX.KL_LOC_Clause_1445, KL_CTX.KL_LOC_Parameters_1444])), [setattr(KL_CTX, 'KL_LOC_Code_1447', tco_apply(shen_aum_to_shen, [KL_CTX.KL_LOC_AUM_instruction_1446])), [setattr(KL_CTX, 'KL_LOC_ShenDef_1448', [symdic.symdic_kl_define, [KL_CTX.KL_LOC_Fx42_1443, tco_apply(kl_append, [KL_CTX.KL_LOC_Parameters_1444, tco_apply(kl_append, [[symdic.symdic_ProcessN, [symdic.symdic_Continuation, []]], [symdic.symdic_kl_x45x62, [KL_CTX.KL_LOC_Code_1447, []]]])])]]), [setattr(KL_CTX, 'KL_LOC_Eval_1449', tco_apply(shen_evalx45withoutx45macros, [KL_CTX.KL_LOC_ShenDef_1448])), KL_ARG_V2131_1437][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('declare', kl_declare)

@tail_recursion
def shen_demodulate(KL_ARG_V2133_1450):
    global symdic
    return tail_call(kl_fix, [symdic.symdic_shen_demodh, KL_ARG_V2133_1450])
shen_add_fun('shen.demodulate', shen_demodulate)

@tail_recursion
def shen_demodh(KL_ARG_V2134_1451):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_demodh, KL_ARG_V2134_1451]) if shen_consp(KL_ARG_V2134_1451) else (tail_call(shen_demodx45atom, [KL_ARG_V2134_1451]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.demodh', shen_demodh)

@tail_recursion
def shen_demodx45atom(KL_ARG_V2135_1452):

    class KL_Context:
        KL_LOC_Val_1453 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Val_1453', tco_apply(kl_assoc, [KL_ARG_V2135_1452, shen_get(symdic.symdic_shen_x42synonymsx42)])), (KL_ARG_V2135_1452 if tco_apply(kl_emptyx63, [KL_CTX.KL_LOC_Val_1453]) else KL_CTX.KL_LOC_Val_1453[1])][(-1)]
shen_add_fun('shen.demod-atom', shen_demodx45atom)

@tail_recursion
def shen_variancyx45test(KL_ARG_V2136_1454, KL_ARG_V2137_1455):

    class KL_Context:
        KL_LOC_TypeF_1456 = None
        KL_LOC_Check_1457 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_TypeF_1456', tco_apply(shen_typecheck, [KL_ARG_V2136_1454, symdic.symdic_B])), [setattr(KL_CTX, 'KL_LOC_Check_1457', (symdic.symdic_shen_skip if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_TypeF_1456) else (symdic.symdic_shen_skip if tco_apply(shen_variantx63, [KL_CTX.KL_LOC_TypeF_1456, KL_ARG_V2137_1455]) else tco_apply(shen_prhush, [('warning: changing the type of ' + tco_apply(shen_app, [KL_ARG_V2136_1454, ' may create errors\r\n', symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])))), symdic.symdic_shen_skip][(-1)]][(-1)]
shen_add_fun('shen.variancy-test', shen_variancyx45test)

@tail_recursion
def shen_variantx63(KL_ARG_V2146_1458, KL_ARG_V2147_1459):
    global symdic
    return (True if shen_eq(KL_ARG_V2147_1459, KL_ARG_V2146_1458) else (tail_call(shen_variantx63, [KL_ARG_V2146_1458[1], KL_ARG_V2147_1459[1]]) if ((shen_eq(KL_ARG_V2147_1459[0], KL_ARG_V2146_1458[0]) if shen_consp(KL_ARG_V2147_1459) else False) if shen_consp(KL_ARG_V2146_1458) else False) else (tail_call(shen_variantx63, [tco_apply(kl_subst, [symdic.symdic_shen_a, KL_ARG_V2146_1458[0], KL_ARG_V2146_1458[1]]), tco_apply(kl_subst, [symdic.symdic_shen_a, KL_ARG_V2147_1459[0], KL_ARG_V2147_1459[1]])]) if (((tco_apply(kl_variablex63, [KL_ARG_V2147_1459[0]]) if tco_apply(shen_pvarx63, [KL_ARG_V2146_1458[0]]) else False) if shen_consp(KL_ARG_V2147_1459) else False) if shen_consp(KL_ARG_V2146_1458) else False) else (tail_call(shen_variantx63, [tco_apply(kl_append, [KL_ARG_V2146_1458[0], KL_ARG_V2146_1458[1]]), tco_apply(kl_append, [KL_ARG_V2147_1459[0], KL_ARG_V2147_1459[1]])]) if (((shen_consp(KL_ARG_V2147_1459[0]) if shen_consp(KL_ARG_V2147_1459) else False) if shen_consp(KL_ARG_V2146_1458[0]) else False) if shen_consp(KL_ARG_V2146_1458) else False) else (False if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.variant?', shen_variantx63)


#============================== t-star.kl==============================



@tail_recursion
def shen_typecheck(KL_ARG_V2848_1460, KL_ARG_V2849_1461):

    class KL_Context:
        KL_LOC_Curry_1462 = None
        KL_LOC_ProcessN_1463 = None
        KL_LOC_Type_1464 = None
        KL_LOC_Continuation_1465 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Curry_1462', tco_apply(shen_curry, [KL_ARG_V2848_1460])), [setattr(KL_CTX, 'KL_LOC_ProcessN_1463', tco_apply(shen_startx45newx45prologx45process, [])), [setattr(KL_CTX, 'KL_LOC_Type_1464', tco_apply(shen_insertx45prologx45variables, [tco_apply(shen_demodulate, [tco_apply(shen_curryx45type, [KL_ARG_V2849_1461])]), KL_CTX.KL_LOC_ProcessN_1463])), [setattr(KL_CTX, 'KL_LOC_Continuation_1465', (lambda : tail_call(kl_return, [KL_CTX.KL_LOC_Type_1464, KL_CTX.KL_LOC_ProcessN_1463, symdic.symdic_shen_void]))), tail_call(shen_tx42, [[KL_CTX.KL_LOC_Curry_1462, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_Type_1464, []]]], [], KL_CTX.KL_LOC_ProcessN_1463, KL_CTX.KL_LOC_Continuation_1465])][(-1)]][(-1)]][(-1)]][(-1)]
shen_add_fun('shen.typecheck', shen_typecheck)

@tail_recursion
def shen_curry(KL_ARG_V2850_1466):
    global symdic
    return ([KL_ARG_V2850_1466[0], tco_apply(kl_map, [symdic.symdic_shen_curry, KL_ARG_V2850_1466[1]])] if (tco_apply(shen_specialx63, [KL_ARG_V2850_1466[0]]) if shen_consp(KL_ARG_V2850_1466) else False) else (KL_ARG_V2850_1466 if ((tco_apply(shen_extraspecialx63, [KL_ARG_V2850_1466[0]]) if shen_consp(KL_ARG_V2850_1466[1]) else False) if shen_consp(KL_ARG_V2850_1466) else False) else (tail_call(shen_curry, [[[KL_ARG_V2850_1466[0], [KL_ARG_V2850_1466[1][0], []]], KL_ARG_V2850_1466[1][1]]]) if ((shen_consp(KL_ARG_V2850_1466[1][1]) if shen_consp(KL_ARG_V2850_1466[1]) else False) if shen_consp(KL_ARG_V2850_1466) else False) else ([tco_apply(shen_curry, [KL_ARG_V2850_1466[0]]), [tco_apply(shen_curry, [KL_ARG_V2850_1466[1][0]]), []]] if ((shen_eq([], KL_ARG_V2850_1466[1][1]) if shen_consp(KL_ARG_V2850_1466[1]) else False) if shen_consp(KL_ARG_V2850_1466) else False) else (KL_ARG_V2850_1466 if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.curry', shen_curry)

@tail_recursion
def shen_specialx63(KL_ARG_V2851_1467):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2851_1467, shen_get(symdic.symdic_shen_x42specialx42)])
shen_add_fun('shen.special?', shen_specialx63)

@tail_recursion
def shen_extraspecialx63(KL_ARG_V2852_1468):
    global symdic
    return tail_call(kl_elementx63, [KL_ARG_V2852_1468, shen_get(symdic.symdic_shen_x42extraspecialx42)])
shen_add_fun('shen.extraspecial?', shen_extraspecialx63)

@tail_recursion
def shen_tx42(KL_ARG_V2853_1469, KL_ARG_V2854_1470, KL_ARG_V2855_1471, KL_ARG_V2856_1472):

    class KL_Context:
        KL_LOC_Throwcontrol_1473 = None
        KL_LOC_Case_1474 = None
        KL_LOC_Error_1475 = None
        KL_LOC_Case_1476 = None
        KL_LOC_V2842_1477 = None
        KL_LOC_Case_1478 = None
        KL_LOC_V2843_1479 = None
        KL_LOC_X_1480 = None
        KL_LOC_V2844_1481 = None
        KL_LOC_V2845_1482 = None
        KL_LOC_V2846_1483 = None
        KL_LOC_A_1484 = None
        KL_LOC_V2847_1485 = None
        KL_LOC_Datatypes_1486 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1473', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1473, [setattr(KL_CTX, 'KL_LOC_Case_1474', [setattr(KL_CTX, 'KL_LOC_Error_1475', tco_apply(shen_newpv, [KL_ARG_V2855_1471])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_maxinfexceededx63, []), KL_ARG_V2855_1471, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Error_1475, tco_apply(shen_errormaxinfs, []), KL_ARG_V2855_1471, KL_ARG_V2856_1472]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1476', [setattr(KL_CTX, 'KL_LOC_V2842_1477', tco_apply(shen_lazyderef, [KL_ARG_V2853_1469, KL_ARG_V2855_1471])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1473, KL_ARG_V2855_1471, (lambda : tail_call(shen_prologx45failure, [KL_ARG_V2855_1471, KL_ARG_V2856_1472]))])][(-1)] if shen_eq(symdic.symdic_kl_fail, KL_CTX.KL_LOC_V2842_1477) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1478', [setattr(KL_CTX, 'KL_LOC_V2843_1479', tco_apply(shen_lazyderef, [KL_ARG_V2853_1469, KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_X_1480', KL_CTX.KL_LOC_V2843_1479[0]), [setattr(KL_CTX, 'KL_LOC_V2844_1481', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2843_1479[1], KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_V2845_1482', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2844_1481[0], KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_V2846_1483', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2844_1481[1], KL_ARG_V2855_1471])), ([setattr(KL_CTX, 'KL_LOC_A_1484', KL_CTX.KL_LOC_V2846_1483[0]), [setattr(KL_CTX, 'KL_LOC_V2847_1485', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2846_1483[1], KL_ARG_V2855_1471])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typex45theoryx45enabledx63, []), KL_ARG_V2855_1471, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1473, KL_ARG_V2855_1471, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1480, KL_CTX.KL_LOC_A_1484, KL_ARG_V2854_1470, KL_ARG_V2855_1471, KL_ARG_V2856_1472]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2847_1485) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2846_1483) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2845_1482) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2844_1481) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2843_1479) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1486', tco_apply(shen_newpv, [KL_ARG_V2855_1471])), [tco_apply(shen_incinfs, []), tco_apply(shen_show, [KL_ARG_V2853_1469, KL_ARG_V2854_1470, KL_ARG_V2855_1471, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Datatypes_1486, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2855_1471, (lambda : tail_call(shen_udefsx42, [KL_ARG_V2853_1469, KL_ARG_V2854_1470, KL_CTX.KL_LOC_Datatypes_1486, KL_ARG_V2855_1471, KL_ARG_V2856_1472]))]))])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1478, False) else KL_CTX.KL_LOC_Case_1478)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1476, False) else KL_CTX.KL_LOC_Case_1476)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1474, False) else KL_CTX.KL_LOC_Case_1474)][(-1)]])][(-1)]
shen_add_fun('shen.t*', shen_tx42)

@tail_recursion
def shen_typex45theoryx45enabledx63():
    global symdic
    return shen_get(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42)
shen_add_fun('shen.type-theory-enabled?', shen_typex45theoryx45enabledx63)

@tail_recursion
def kl_enablex45typex45theory(KL_ARG_V2861_1487):
    global symdic
    return (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, True) if shen_eq(symdic.symdic_kl_x43, KL_ARG_V2861_1487) else (shen_set(symdic.symdic_shen_x42shenx45typex45theoryx45enabledx63x42, False) if shen_eq(symdic.symdic_kl_x45, KL_ARG_V2861_1487) else (shen_simple_error('enable-type-theory expects a + or a -\r\n') if True else shen_simple_error('condition failure'))))
shen_add_fun('enable-type-theory', kl_enablex45typex45theory)

@tail_recursion
def shen_prologx45failure(KL_ARG_V2870_1488, KL_ARG_V2871_1489):
    global symdic
    return False
shen_add_fun('shen.prolog-failure', shen_prologx45failure)

@tail_recursion
def shen_maxinfexceededx63():
    global symdic
    return (tco_apply(kl_inferences, []) > shen_get(symdic.symdic_shen_x42maxinferencesx42))
shen_add_fun('shen.maxinfexceeded?', shen_maxinfexceededx63)

@tail_recursion
def shen_errormaxinfs():
    global symdic
    return shen_simple_error('maximum inferences exceeded~%')
shen_add_fun('shen.errormaxinfs', shen_errormaxinfs)

@tail_recursion
def shen_udefsx42(KL_ARG_V2872_1490, KL_ARG_V2873_1491, KL_ARG_V2874_1492, KL_ARG_V2875_1493, KL_ARG_V2876_1494):

    class KL_Context:
        KL_LOC_Case_1495 = None
        KL_LOC_V2838_1496 = None
        KL_LOC_D_1497 = None
        KL_LOC_V2839_1498 = None
        KL_LOC_Ds_1499 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1495', [setattr(KL_CTX, 'KL_LOC_V2838_1496', tco_apply(shen_lazyderef, [KL_ARG_V2874_1492, KL_ARG_V2875_1493])), ([setattr(KL_CTX, 'KL_LOC_D_1497', KL_CTX.KL_LOC_V2838_1496[0]), [tco_apply(shen_incinfs, []), tco_apply(kl_call, [[KL_CTX.KL_LOC_D_1497, [KL_ARG_V2872_1490, [KL_ARG_V2873_1491, []]]], KL_ARG_V2875_1493, KL_ARG_V2876_1494])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2838_1496) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2839_1498', tco_apply(shen_lazyderef, [KL_ARG_V2874_1492, KL_ARG_V2875_1493])), ([setattr(KL_CTX, 'KL_LOC_Ds_1499', KL_CTX.KL_LOC_V2839_1498[1]), [tco_apply(shen_incinfs, []), tail_call(shen_udefsx42, [KL_ARG_V2872_1490, KL_ARG_V2873_1491, KL_CTX.KL_LOC_Ds_1499, KL_ARG_V2875_1493, KL_ARG_V2876_1494])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2839_1498) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1495, False) else KL_CTX.KL_LOC_Case_1495)][(-1)]
shen_add_fun('shen.udefs*', shen_udefsx42)

@tail_recursion
def shen_thx42(KL_ARG_V2877_1500, KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504):

    class KL_Context:
        KL_LOC_Throwcontrol_1505 = None
        KL_LOC_Case_1506 = None
        KL_LOC_Case_1507 = None
        KL_LOC_F_1508 = None
        KL_LOC_Case_1509 = None
        KL_LOC_Case_1510 = None
        KL_LOC_Case_1511 = None
        KL_LOC_V2717_1512 = None
        KL_LOC_F_1513 = None
        KL_LOC_V2718_1514 = None
        KL_LOC_Case_1515 = None
        KL_LOC_V2719_1516 = None
        KL_LOC_F_1517 = None
        KL_LOC_V2720_1518 = None
        KL_LOC_X_1519 = None
        KL_LOC_V2721_1520 = None
        KL_LOC_B_1521 = None
        KL_LOC_Case_1522 = None
        KL_LOC_V2722_1523 = None
        KL_LOC_V2723_1524 = None
        KL_LOC_V2724_1525 = None
        KL_LOC_X_1526 = None
        KL_LOC_V2725_1527 = None
        KL_LOC_Y_1528 = None
        KL_LOC_V2726_1529 = None
        KL_LOC_V2727_1530 = None
        KL_LOC_V2728_1531 = None
        KL_LOC_V2729_1532 = None
        KL_LOC_A_1533 = None
        KL_LOC_V2730_1534 = None
        KL_LOC_Result_1535 = None
        KL_LOC_A_1536 = None
        KL_LOC_Result_1537 = None
        KL_LOC_Result_1538 = None
        KL_LOC_V2731_1539 = None
        KL_LOC_A_1540 = None
        KL_LOC_V2732_1541 = None
        KL_LOC_Result_1542 = None
        KL_LOC_A_1543 = None
        KL_LOC_Result_1544 = None
        KL_LOC_A_1545 = None
        KL_LOC_Result_1546 = None
        KL_LOC_Case_1547 = None
        KL_LOC_V2733_1548 = None
        KL_LOC_V2734_1549 = None
        KL_LOC_V2735_1550 = None
        KL_LOC_X_1551 = None
        KL_LOC_V2736_1552 = None
        KL_LOC_Y_1553 = None
        KL_LOC_V2737_1554 = None
        KL_LOC_V2738_1555 = None
        KL_LOC_A_1556 = None
        KL_LOC_V2739_1557 = None
        KL_LOC_V2740_1558 = None
        KL_LOC_V2741_1559 = None
        KL_LOC_B_1560 = None
        KL_LOC_V2742_1561 = None
        KL_LOC_Result_1562 = None
        KL_LOC_B_1563 = None
        KL_LOC_Result_1564 = None
        KL_LOC_Result_1565 = None
        KL_LOC_V2743_1566 = None
        KL_LOC_B_1567 = None
        KL_LOC_V2744_1568 = None
        KL_LOC_Result_1569 = None
        KL_LOC_B_1570 = None
        KL_LOC_Result_1571 = None
        KL_LOC_B_1572 = None
        KL_LOC_Result_1573 = None
        KL_LOC_A_1574 = None
        KL_LOC_B_1575 = None
        KL_LOC_Result_1576 = None
        KL_LOC_Case_1577 = None
        KL_LOC_V2745_1578 = None
        KL_LOC_V2746_1579 = None
        KL_LOC_V2747_1580 = None
        KL_LOC_X_1581 = None
        KL_LOC_V2748_1582 = None
        KL_LOC_Y_1583 = None
        KL_LOC_V2749_1584 = None
        KL_LOC_V2750_1585 = None
        KL_LOC_V2751_1586 = None
        KL_LOC_V2752_1587 = None
        KL_LOC_A_1588 = None
        KL_LOC_V2753_1589 = None
        KL_LOC_Result_1590 = None
        KL_LOC_A_1591 = None
        KL_LOC_Result_1592 = None
        KL_LOC_Result_1593 = None
        KL_LOC_V2754_1594 = None
        KL_LOC_A_1595 = None
        KL_LOC_V2755_1596 = None
        KL_LOC_Result_1597 = None
        KL_LOC_A_1598 = None
        KL_LOC_Result_1599 = None
        KL_LOC_A_1600 = None
        KL_LOC_Result_1601 = None
        KL_LOC_Case_1602 = None
        KL_LOC_V2756_1603 = None
        KL_LOC_V2757_1604 = None
        KL_LOC_V2758_1605 = None
        KL_LOC_X_1606 = None
        KL_LOC_V2759_1607 = None
        KL_LOC_Y_1608 = None
        KL_LOC_V2760_1609 = None
        KL_LOC_V2761_1610 = None
        KL_LOC_Result_1611 = None
        KL_LOC_Case_1612 = None
        KL_LOC_V2762_1613 = None
        KL_LOC_V2763_1614 = None
        KL_LOC_V2764_1615 = None
        KL_LOC_X_1616 = None
        KL_LOC_V2765_1617 = None
        KL_LOC_Y_1618 = None
        KL_LOC_V2766_1619 = None
        KL_LOC_V2767_1620 = None
        KL_LOC_A_1621 = None
        KL_LOC_V2768_1622 = None
        KL_LOC_V2769_1623 = None
        KL_LOC_V2770_1624 = None
        KL_LOC_B_1625 = None
        KL_LOC_V2771_1626 = None
        KL_LOC_Z_1627 = None
        KL_LOC_Xx38x38_1628 = None
        KL_LOC_Result_1629 = None
        KL_LOC_Z_1630 = None
        KL_LOC_Xx38x38_1631 = None
        KL_LOC_B_1632 = None
        KL_LOC_Result_1633 = None
        KL_LOC_Z_1634 = None
        KL_LOC_Xx38x38_1635 = None
        KL_LOC_Result_1636 = None
        KL_LOC_V2772_1637 = None
        KL_LOC_B_1638 = None
        KL_LOC_V2773_1639 = None
        KL_LOC_Z_1640 = None
        KL_LOC_Xx38x38_1641 = None
        KL_LOC_Result_1642 = None
        KL_LOC_Z_1643 = None
        KL_LOC_Xx38x38_1644 = None
        KL_LOC_B_1645 = None
        KL_LOC_Result_1646 = None
        KL_LOC_Z_1647 = None
        KL_LOC_Xx38x38_1648 = None
        KL_LOC_B_1649 = None
        KL_LOC_Result_1650 = None
        KL_LOC_Z_1651 = None
        KL_LOC_Xx38x38_1652 = None
        KL_LOC_A_1653 = None
        KL_LOC_B_1654 = None
        KL_LOC_Result_1655 = None
        KL_LOC_Z_1656 = None
        KL_LOC_Xx38x38_1657 = None
        KL_LOC_Case_1658 = None
        KL_LOC_V2774_1659 = None
        KL_LOC_V2775_1660 = None
        KL_LOC_V2776_1661 = None
        KL_LOC_X_1662 = None
        KL_LOC_V2777_1663 = None
        KL_LOC_Y_1664 = None
        KL_LOC_V2778_1665 = None
        KL_LOC_Z_1666 = None
        KL_LOC_V2779_1667 = None
        KL_LOC_W_1668 = None
        KL_LOC_Xx38x38_1669 = None
        KL_LOC_B_1670 = None
        KL_LOC_Case_1671 = None
        KL_LOC_V2780_1672 = None
        KL_LOC_V2781_1673 = None
        KL_LOC_V2782_1674 = None
        KL_LOC_V2783_1675 = None
        KL_LOC_V2784_1676 = None
        KL_LOC_FileName_1677 = None
        KL_LOC_V2785_1678 = None
        KL_LOC_Direction2713_1679 = None
        KL_LOC_V2786_1680 = None
        KL_LOC_V2787_1681 = None
        KL_LOC_V2788_1682 = None
        KL_LOC_V2789_1683 = None
        KL_LOC_Direction_1684 = None
        KL_LOC_V2790_1685 = None
        KL_LOC_Result_1686 = None
        KL_LOC_Direction_1687 = None
        KL_LOC_Result_1688 = None
        KL_LOC_Result_1689 = None
        KL_LOC_V2791_1690 = None
        KL_LOC_Direction_1691 = None
        KL_LOC_V2792_1692 = None
        KL_LOC_Result_1693 = None
        KL_LOC_Direction_1694 = None
        KL_LOC_Result_1695 = None
        KL_LOC_Direction_1696 = None
        KL_LOC_Result_1697 = None
        KL_LOC_Case_1698 = None
        KL_LOC_V2793_1699 = None
        KL_LOC_V2794_1700 = None
        KL_LOC_V2795_1701 = None
        KL_LOC_X_1702 = None
        KL_LOC_V2796_1703 = None
        KL_LOC_A_1704 = None
        KL_LOC_V2797_1705 = None
        KL_LOC_Case_1706 = None
        KL_LOC_V2798_1707 = None
        KL_LOC_V2799_1708 = None
        KL_LOC_V2800_1709 = None
        KL_LOC_V2801_1710 = None
        KL_LOC_V2802_1711 = None
        KL_LOC_A_1712 = None
        KL_LOC_V2803_1713 = None
        KL_LOC_C_1714 = None
        KL_LOC_Case_1715 = None
        KL_LOC_V2804_1716 = None
        KL_LOC_V2805_1717 = None
        KL_LOC_V2806_1718 = None
        KL_LOC_V2807_1719 = None
        KL_LOC_V2808_1720 = None
        KL_LOC_A_1721 = None
        KL_LOC_V2809_1722 = None
        KL_LOC_C_1723 = None
        KL_LOC_Case_1724 = None
        KL_LOC_V2810_1725 = None
        KL_LOC_V2811_1726 = None
        KL_LOC_V2812_1727 = None
        KL_LOC_Var_1728 = None
        KL_LOC_V2813_1729 = None
        KL_LOC_Val_1730 = None
        KL_LOC_V2814_1731 = None
        KL_LOC_Case_1732 = None
        KL_LOC_V2815_1733 = None
        KL_LOC_V2816_1734 = None
        KL_LOC_V2817_1735 = None
        KL_LOC_F_1736 = None
        KL_LOC_V2818_1737 = None
        KL_LOC_A_1738 = None
        KL_LOC_Fx38x38_1739 = None
        KL_LOC_B_1740 = None
        KL_LOC_Case_1741 = None
        KL_LOC_V2819_1742 = None
        KL_LOC_V2820_1743 = None
        KL_LOC_V2821_1744 = None
        KL_LOC_V2822_1745 = None
        KL_LOC_Result_1746 = None
        KL_LOC_Case_1747 = None
        KL_LOC_NewHyp_1748 = None
        KL_LOC_Case_1749 = None
        KL_LOC_V2823_1750 = None
        KL_LOC_V2824_1751 = None
        KL_LOC_V2825_1752 = None
        KL_LOC_F_1753 = None
        KL_LOC_X_1754 = None
        KL_LOC_Case_1755 = None
        KL_LOC_V2826_1756 = None
        KL_LOC_V2827_1757 = None
        KL_LOC_V2828_1758 = None
        KL_LOC_F_1759 = None
        KL_LOC_X_1760 = None
        KL_LOC_Case_1761 = None
        KL_LOC_V2829_1762 = None
        KL_LOC_V2830_1763 = None
        KL_LOC_V2831_1764 = None
        KL_LOC_Result_1765 = None
        KL_LOC_Case_1766 = None
        KL_LOC_V2832_1767 = None
        KL_LOC_V2833_1768 = None
        KL_LOC_V2834_1769 = None
        KL_LOC_Result_1770 = None
        KL_LOC_Datatypes_1771 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_1505', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_1505, [setattr(KL_CTX, 'KL_LOC_Case_1506', [tco_apply(shen_incinfs, []), tco_apply(shen_show, [[KL_ARG_V2877_1500, [symdic.symdic_kl_x58, [KL_ARG_V2878_1501, []]]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1507', [setattr(KL_CTX, 'KL_LOC_F_1508', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_typedfx63, [tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_F_1508, tco_apply(shen_sigf, [tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_call, [[KL_CTX.KL_LOC_F_1508, [KL_ARG_V2878_1501, []]], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1509', [tco_apply(shen_incinfs, []), tco_apply(shen_base, [KL_ARG_V2877_1500, KL_ARG_V2878_1501, KL_ARG_V2880_1503, KL_ARG_V2881_1504])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1510', [tco_apply(shen_incinfs, []), tco_apply(shen_by_hypothesis, [KL_ARG_V2877_1500, KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1511', [setattr(KL_CTX, 'KL_LOC_V2717_1512', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1513', KL_CTX.KL_LOC_V2717_1512[0]), [setattr(KL_CTX, 'KL_LOC_V2718_1514', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2717_1512[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1513, [symdic.symdic_kl_x45x45x62, [KL_ARG_V2878_1501, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2718_1514) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2717_1512) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1515', [setattr(KL_CTX, 'KL_LOC_V2719_1516', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1517', KL_CTX.KL_LOC_V2719_1516[0]), [setattr(KL_CTX, 'KL_LOC_V2720_1518', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2719_1516[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1519', KL_CTX.KL_LOC_V2720_1518[0]), [setattr(KL_CTX, 'KL_LOC_V2721_1520', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2720_1518[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1521', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_F_1517, [KL_CTX.KL_LOC_B_1521, [symdic.symdic_kl_x45x45x62, [KL_ARG_V2878_1501, []]]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1519, KL_CTX.KL_LOC_B_1521, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2721_1520) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2720_1518) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2719_1516) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1522', [setattr(KL_CTX, 'KL_LOC_V2722_1523', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2723_1524', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2722_1523[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2724_1525', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2722_1523[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1526', KL_CTX.KL_LOC_V2724_1525[0]), [setattr(KL_CTX, 'KL_LOC_V2725_1527', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2724_1525[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1528', KL_CTX.KL_LOC_V2725_1527[0]), [setattr(KL_CTX, 'KL_LOC_V2726_1529', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2725_1527[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2727_1530', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2728_1531', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2727_1530[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2729_1532', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2727_1530[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1533', KL_CTX.KL_LOC_V2729_1532[0]), [setattr(KL_CTX, 'KL_LOC_V2730_1534', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2729_1532[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1533, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1533, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2730_1534) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2730_1534, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1535', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1533, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1533, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2730_1534, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1535][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2730_1534]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2729_1532) else ([setattr(KL_CTX, 'KL_LOC_A_1536', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2729_1532, [KL_CTX.KL_LOC_A_1536, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1537', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1536, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1536, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2729_1532, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1537][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2729_1532]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2728_1531) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2728_1531, symdic.symdic_kl_list, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1538', [setattr(KL_CTX, 'KL_LOC_V2731_1539', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2727_1530[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1540', KL_CTX.KL_LOC_V2731_1539[0]), [setattr(KL_CTX, 'KL_LOC_V2732_1541', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2731_1539[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1540, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1540, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2732_1541) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2732_1541, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1542', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1540, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1540, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2732_1541, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1542][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2732_1541]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2731_1539) else ([setattr(KL_CTX, 'KL_LOC_A_1543', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2731_1539, [KL_CTX.KL_LOC_A_1543, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1544', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1543, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1543, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2731_1539, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1544][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2731_1539]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2728_1531, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1538][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2728_1531]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2727_1530) else ([setattr(KL_CTX, 'KL_LOC_A_1545', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2727_1530, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1545, []]], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1546', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1526, KL_CTX.KL_LOC_A_1545, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1528, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1545, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2727_1530, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1546][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2727_1530]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2726_1529) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2725_1527) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2724_1525) else False)][(-1)] if shen_eq(symdic.symdic_kl_cons, KL_CTX.KL_LOC_V2723_1524) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2722_1523) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1547', [setattr(KL_CTX, 'KL_LOC_V2733_1548', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2734_1549', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2733_1548[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2735_1550', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2733_1548[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1551', KL_CTX.KL_LOC_V2735_1550[0]), [setattr(KL_CTX, 'KL_LOC_V2736_1552', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2735_1550[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1553', KL_CTX.KL_LOC_V2736_1552[0]), [setattr(KL_CTX, 'KL_LOC_V2737_1554', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2736_1552[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2738_1555', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1556', KL_CTX.KL_LOC_V2738_1555[0]), [setattr(KL_CTX, 'KL_LOC_V2739_1557', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2738_1555[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2740_1558', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2739_1557[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2741_1559', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2739_1557[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1560', KL_CTX.KL_LOC_V2741_1559[0]), [setattr(KL_CTX, 'KL_LOC_V2742_1561', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2741_1559[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1560, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2742_1561) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2742_1561, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1562', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1560, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2742_1561, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1562][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2742_1561]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2741_1559) else ([setattr(KL_CTX, 'KL_LOC_B_1563', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2741_1559, [KL_CTX.KL_LOC_B_1563, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1564', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1563, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2741_1559, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1564][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2741_1559]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x42, KL_CTX.KL_LOC_V2740_1558) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2740_1558, symdic.symdic_kl_x42, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1565', [setattr(KL_CTX, 'KL_LOC_V2743_1566', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2739_1557[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1567', KL_CTX.KL_LOC_V2743_1566[0]), [setattr(KL_CTX, 'KL_LOC_V2744_1568', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2743_1566[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1567, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2744_1568) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2744_1568, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1569', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1567, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2744_1568, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1569][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2744_1568]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2743_1566) else ([setattr(KL_CTX, 'KL_LOC_B_1570', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2743_1566, [KL_CTX.KL_LOC_B_1570, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1571', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1570, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2743_1566, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1571][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2743_1566]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2740_1558, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1565][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2740_1558]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2739_1557) else ([setattr(KL_CTX, 'KL_LOC_B_1572', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2739_1557, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1572, []]], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1573', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1556, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1572, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2739_1557, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1573][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2739_1557]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2738_1555) else ([setattr(KL_CTX, 'KL_LOC_A_1574', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1575', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2738_1555, [KL_CTX.KL_LOC_A_1574, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1575, []]]], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1576', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1551, KL_CTX.KL_LOC_A_1574, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1553, KL_CTX.KL_LOC_B_1575, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2738_1555, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1576][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2738_1555]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2737_1554) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2736_1552) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2735_1550) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64p, KL_CTX.KL_LOC_V2734_1549) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2733_1548) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1577', [setattr(KL_CTX, 'KL_LOC_V2745_1578', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2746_1579', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2745_1578[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2747_1580', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2745_1578[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1581', KL_CTX.KL_LOC_V2747_1580[0]), [setattr(KL_CTX, 'KL_LOC_V2748_1582', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2747_1580[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1583', KL_CTX.KL_LOC_V2748_1582[0]), [setattr(KL_CTX, 'KL_LOC_V2749_1584', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2748_1582[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2750_1585', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2751_1586', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2750_1585[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2752_1587', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2750_1585[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1588', KL_CTX.KL_LOC_V2752_1587[0]), [setattr(KL_CTX, 'KL_LOC_V2753_1589', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2752_1587[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1588, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1588, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2753_1589) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2753_1589, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1590', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1588, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1588, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2753_1589, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1590][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2753_1589]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2752_1587) else ([setattr(KL_CTX, 'KL_LOC_A_1591', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2752_1587, [KL_CTX.KL_LOC_A_1591, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1592', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1591, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1591, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2752_1587, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1592][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2752_1587]) else False))][(-1)] if shen_eq(symdic.symdic_kl_vector, KL_CTX.KL_LOC_V2751_1586) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2751_1586, symdic.symdic_kl_vector, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1593', [setattr(KL_CTX, 'KL_LOC_V2754_1594', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2750_1585[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1595', KL_CTX.KL_LOC_V2754_1594[0]), [setattr(KL_CTX, 'KL_LOC_V2755_1596', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2754_1594[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1595, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1595, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2755_1596) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2755_1596, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1597', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1595, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1595, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2755_1596, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1597][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2755_1596]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2754_1594) else ([setattr(KL_CTX, 'KL_LOC_A_1598', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2754_1594, [KL_CTX.KL_LOC_A_1598, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1599', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1598, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1598, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2754_1594, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1599][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2754_1594]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2751_1586, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1593][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2751_1586]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2750_1585) else ([setattr(KL_CTX, 'KL_LOC_A_1600', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2750_1585, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1600, []]], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1601', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1581, KL_CTX.KL_LOC_A_1600, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1583, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1600, []]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2750_1585, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1601][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2750_1585]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2749_1584) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2748_1582) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2747_1580) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64v, KL_CTX.KL_LOC_V2746_1579) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2745_1578) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1602', [setattr(KL_CTX, 'KL_LOC_V2756_1603', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2757_1604', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2756_1603[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2758_1605', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2756_1603[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1606', KL_CTX.KL_LOC_V2758_1605[0]), [setattr(KL_CTX, 'KL_LOC_V2759_1607', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2758_1605[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1608', KL_CTX.KL_LOC_V2759_1607[0]), [setattr(KL_CTX, 'KL_LOC_V2760_1609', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2759_1607[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2761_1610', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1606, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1608, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2761_1610) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2761_1610, symdic.symdic_kl_string, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1611', [tco_apply(shen_incinfs, []), tco_apply(shen_thx42, [KL_CTX.KL_LOC_X_1606, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1608, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2761_1610, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1611][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2761_1610]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2760_1609) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2759_1607) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2758_1605) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64s, KL_CTX.KL_LOC_V2757_1604) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2756_1603) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1612', [setattr(KL_CTX, 'KL_LOC_V2762_1613', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2763_1614', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2762_1613[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2764_1615', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2762_1613[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1616', KL_CTX.KL_LOC_V2764_1615[0]), [setattr(KL_CTX, 'KL_LOC_V2765_1617', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2764_1615[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1618', KL_CTX.KL_LOC_V2765_1617[0]), [setattr(KL_CTX, 'KL_LOC_V2766_1619', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2765_1617[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2767_1620', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1621', KL_CTX.KL_LOC_V2767_1620[0]), [setattr(KL_CTX, 'KL_LOC_V2768_1622', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2767_1620[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2769_1623', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2768_1622[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2770_1624', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2768_1622[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1625', KL_CTX.KL_LOC_V2770_1624[0]), [setattr(KL_CTX, 'KL_LOC_V2771_1626', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2770_1624[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Z_1627', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1628', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1628, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1627, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1628, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1627, KL_CTX.KL_LOC_B_1625, [[KL_CTX.KL_LOC_Xx38x38_1628, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1621, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2771_1626) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2771_1626, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1629', [setattr(KL_CTX, 'KL_LOC_Z_1630', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1631', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1631, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1630, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1631, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1630, KL_CTX.KL_LOC_B_1625, [[KL_CTX.KL_LOC_Xx38x38_1631, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1621, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2771_1626, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1629][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2771_1626]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2770_1624) else ([setattr(KL_CTX, 'KL_LOC_B_1632', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2770_1624, [KL_CTX.KL_LOC_B_1632, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1633', [setattr(KL_CTX, 'KL_LOC_Z_1634', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1635', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1635, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1634, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1635, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1634, KL_CTX.KL_LOC_B_1632, [[KL_CTX.KL_LOC_Xx38x38_1635, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1621, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2770_1624, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1633][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2770_1624]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2769_1623) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2769_1623, symdic.symdic_kl_x45x45x62, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1636', [setattr(KL_CTX, 'KL_LOC_V2772_1637', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2768_1622[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_B_1638', KL_CTX.KL_LOC_V2772_1637[0]), [setattr(KL_CTX, 'KL_LOC_V2773_1639', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2772_1637[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Z_1640', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1641', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1641, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1640, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1641, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1640, KL_CTX.KL_LOC_B_1638, [[KL_CTX.KL_LOC_Xx38x38_1641, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1621, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2773_1639) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2773_1639, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1642', [setattr(KL_CTX, 'KL_LOC_Z_1643', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1644', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1644, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1643, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1644, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1643, KL_CTX.KL_LOC_B_1638, [[KL_CTX.KL_LOC_Xx38x38_1644, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1621, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2773_1639, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1642][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2773_1639]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2772_1637) else ([setattr(KL_CTX, 'KL_LOC_B_1645', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2772_1637, [KL_CTX.KL_LOC_B_1645, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1646', [setattr(KL_CTX, 'KL_LOC_Z_1647', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1648', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1648, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1647, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1648, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1647, KL_CTX.KL_LOC_B_1645, [[KL_CTX.KL_LOC_Xx38x38_1648, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1621, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2772_1637, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1646][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2772_1637]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2769_1623, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1636][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2769_1623]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2768_1622) else ([setattr(KL_CTX, 'KL_LOC_B_1649', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2768_1622, [symdic.symdic_kl_x45x45x62, [KL_CTX.KL_LOC_B_1649, []]], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1650', [setattr(KL_CTX, 'KL_LOC_Z_1651', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1652', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1652, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1651, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1652, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1651, KL_CTX.KL_LOC_B_1649, [[KL_CTX.KL_LOC_Xx38x38_1652, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1621, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2768_1622, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1650][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2768_1622]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2767_1620) else ([setattr(KL_CTX, 'KL_LOC_A_1653', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1654', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2767_1620, [KL_CTX.KL_LOC_A_1653, [symdic.symdic_kl_x45x45x62, [KL_CTX.KL_LOC_B_1654, []]]], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1655', [setattr(KL_CTX, 'KL_LOC_Z_1656', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1657', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1657, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Z_1656, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1657, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1616, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1618, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Z_1656, KL_CTX.KL_LOC_B_1654, [[KL_CTX.KL_LOC_Xx38x38_1657, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_1653, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))])][(-1)]][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2767_1620, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1655][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2767_1620]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2766_1619) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2765_1617) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2764_1615) else False)][(-1)] if shen_eq(symdic.symdic_kl_lambda, KL_CTX.KL_LOC_V2763_1614) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2762_1613) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1658', [setattr(KL_CTX, 'KL_LOC_V2774_1659', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2775_1660', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2774_1659[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2776_1661', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2774_1659[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1662', KL_CTX.KL_LOC_V2776_1661[0]), [setattr(KL_CTX, 'KL_LOC_V2777_1663', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2776_1661[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Y_1664', KL_CTX.KL_LOC_V2777_1663[0]), [setattr(KL_CTX, 'KL_LOC_V2778_1665', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2777_1663[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Z_1666', KL_CTX.KL_LOC_V2778_1665[0]), [setattr(KL_CTX, 'KL_LOC_V2779_1667', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2778_1665[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_W_1668', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_1669', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1670', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Y_1664, KL_CTX.KL_LOC_B_1670, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_1669, tco_apply(shen_placeholder, []), KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_W_1668, tco_apply(shen_ebr, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Xx38x38_1669, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1662, KL_ARG_V2880_1503]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Z_1666, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_W_1668, KL_ARG_V2878_1501, [[KL_CTX.KL_LOC_Xx38x38_1669, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_B_1670, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2779_1667) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2778_1665) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2777_1663) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2776_1661) else False)][(-1)] if shen_eq(symdic.symdic_kl_let, KL_CTX.KL_LOC_V2775_1660) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2774_1659) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1671', [setattr(KL_CTX, 'KL_LOC_V2780_1672', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2781_1673', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2780_1672[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2782_1674', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2780_1672[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2783_1675', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2782_1674[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2784_1676', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2782_1674[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_FileName_1677', KL_CTX.KL_LOC_V2784_1676[0]), [setattr(KL_CTX, 'KL_LOC_V2785_1678', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2784_1676[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Direction2713_1679', KL_CTX.KL_LOC_V2785_1678[0]), [setattr(KL_CTX, 'KL_LOC_V2786_1680', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2785_1678[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2787_1681', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2788_1682', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2787_1681[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2789_1683', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2787_1681[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Direction_1684', KL_CTX.KL_LOC_V2789_1683[0]), [setattr(KL_CTX, 'KL_LOC_V2790_1685', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2789_1683[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1684, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2790_1685) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2790_1685, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1686', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1684, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2790_1685, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1686][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2790_1685]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2789_1683) else ([setattr(KL_CTX, 'KL_LOC_Direction_1687', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2789_1683, [KL_CTX.KL_LOC_Direction_1687, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1688', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1687, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2789_1683, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1688][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2789_1683]) else False))][(-1)] if shen_eq(symdic.symdic_kl_stream, KL_CTX.KL_LOC_V2788_1682) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2788_1682, symdic.symdic_kl_stream, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1689', [setattr(KL_CTX, 'KL_LOC_V2791_1690', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2787_1681[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Direction_1691', KL_CTX.KL_LOC_V2791_1690[0]), [setattr(KL_CTX, 'KL_LOC_V2792_1692', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2791_1690[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1691, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2792_1692) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2792_1692, [], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1693', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1691, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2792_1692, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1693][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2792_1692]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2791_1690) else ([setattr(KL_CTX, 'KL_LOC_Direction_1694', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2791_1690, [KL_CTX.KL_LOC_Direction_1694, []], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1695', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1694, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2791_1690, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1695][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2791_1690]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2788_1682, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1689][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2788_1682]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2787_1681) else ([setattr(KL_CTX, 'KL_LOC_Direction_1696', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2787_1681, [symdic.symdic_kl_stream, [KL_CTX.KL_LOC_Direction_1696, []]], KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1697', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Direction_1696, KL_CTX.KL_LOC_Direction2713_1679, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_FileName_1677, symdic.symdic_kl_string, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2787_1681, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1697][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2787_1681]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2786_1680) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2785_1678) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2784_1676) else False)][(-1)] if shen_eq(symdic.symdic_kl_file, KL_CTX.KL_LOC_V2783_1675) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2782_1674) else False)][(-1)] if shen_eq(symdic.symdic_kl_open, KL_CTX.KL_LOC_V2781_1673) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2780_1672) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1698', [setattr(KL_CTX, 'KL_LOC_V2793_1699', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2794_1700', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2793_1699[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2795_1701', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2793_1699[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_X_1702', KL_CTX.KL_LOC_V2795_1701[0]), [setattr(KL_CTX, 'KL_LOC_V2796_1703', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2795_1701[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1704', KL_CTX.KL_LOC_V2796_1703[0]), [setattr(KL_CTX, 'KL_LOC_V2797_1705', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2796_1703[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_unify, [KL_CTX.KL_LOC_A_1704, KL_ARG_V2878_1501, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_X_1702, KL_CTX.KL_LOC_A_1704, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2797_1705) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2796_1703) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2795_1701) else False)][(-1)] if shen_eq(symdic.symdic_kl_type, KL_CTX.KL_LOC_V2794_1700) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2793_1699) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1706', [setattr(KL_CTX, 'KL_LOC_V2798_1707', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2799_1708', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2798_1707[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2800_1709', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2798_1707[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2801_1710', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2800_1709[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2802_1711', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2800_1709[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1712', KL_CTX.KL_LOC_V2802_1711[0]), [setattr(KL_CTX, 'KL_LOC_V2803_1713', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2802_1711[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_C_1714', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_C_1714, tco_apply(shen_demodulate, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1712, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_unify, [KL_ARG_V2878_1501, KL_CTX.KL_LOC_C_1714, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2803_1713) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2802_1711) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2801_1710) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2800_1709) else False)][(-1)] if shen_eq(symdic.symdic_kl_inputx43, KL_CTX.KL_LOC_V2799_1708) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2798_1707) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1715', [setattr(KL_CTX, 'KL_LOC_V2804_1716', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2805_1717', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2804_1716[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2806_1718', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2804_1716[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2807_1719', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2806_1718[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2808_1720', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2806_1718[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1721', KL_CTX.KL_LOC_V2808_1720[0]), [setattr(KL_CTX, 'KL_LOC_V2809_1722', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2808_1720[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_C_1723', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_C_1723, tco_apply(shen_demodulate, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1721, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_unify, [KL_ARG_V2878_1501, KL_CTX.KL_LOC_C_1723, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2809_1722) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2808_1720) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2807_1719) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2806_1718) else False)][(-1)] if shen_eq(symdic.symdic_readx43, KL_CTX.KL_LOC_V2805_1717) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2804_1716) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1724', [setattr(KL_CTX, 'KL_LOC_V2810_1725', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2811_1726', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2810_1725[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2812_1727', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2810_1725[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Var_1728', KL_CTX.KL_LOC_V2812_1727[0]), [setattr(KL_CTX, 'KL_LOC_V2813_1729', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2812_1727[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_Val_1730', KL_CTX.KL_LOC_V2813_1729[0]), [setattr(KL_CTX, 'KL_LOC_V2814_1731', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2813_1729[1], KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Var_1728, symdic.symdic_kl_symbol, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [[symdic.symdic_kl_value, [KL_CTX.KL_LOC_Var_1728, []]], KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Val_1730, KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2814_1731) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2813_1729) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2812_1727) else False)][(-1)] if shen_eq(symdic.symdic_kl_set, KL_CTX.KL_LOC_V2811_1726) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2810_1725) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1732', [setattr(KL_CTX, 'KL_LOC_V2815_1733', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2816_1734', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2815_1733[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2817_1735', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2815_1733[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1736', KL_CTX.KL_LOC_V2817_1735[0]), [setattr(KL_CTX, 'KL_LOC_V2818_1737', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2817_1735[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_A_1738', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_Fx38x38_1739', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [setattr(KL_CTX, 'KL_LOC_B_1740', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_F_1736, [KL_CTX.KL_LOC_A_1738, [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_B_1740, []]]], KL_ARG_V2879_1502, KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Fx38x38_1739, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_1736, KL_ARG_V2880_1503])]), KL_ARG_V2880_1503, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_CTX.KL_LOC_Fx38x38_1739, KL_ARG_V2878_1501, [[KL_CTX.KL_LOC_Fx38x38_1739, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_B_1740, []]]], KL_ARG_V2879_1502], KL_ARG_V2880_1503, KL_ARG_V2881_1504]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2818_1737) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2817_1735) else False)][(-1)] if shen_eq(symdic.symdic_shen_x60x45sem, KL_CTX.KL_LOC_V2816_1734) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2815_1733) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1741', [setattr(KL_CTX, 'KL_LOC_V2819_1742', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2820_1743', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2819_1742[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2821_1744', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2819_1742[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2822_1745', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2822_1745) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2822_1745, symdic.symdic_kl_symbol, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1746', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2822_1745, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1746][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2822_1745]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2821_1744) else False)][(-1)] if shen_eq(symdic.symdic_kl_fail, KL_CTX.KL_LOC_V2820_1743) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2819_1742) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1747', [setattr(KL_CTX, 'KL_LOC_NewHyp_1748', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45hyps, [KL_ARG_V2879_1502, KL_CTX.KL_LOC_NewHyp_1748, KL_ARG_V2880_1503, (lambda : tail_call(shen_thx42, [KL_ARG_V2877_1500, KL_ARG_V2878_1501, KL_CTX.KL_LOC_NewHyp_1748, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1749', [setattr(KL_CTX, 'KL_LOC_V2823_1750', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2824_1751', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2823_1750[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2825_1752', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2823_1750[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1753', KL_CTX.KL_LOC_V2825_1752[0]), [setattr(KL_CTX, 'KL_LOC_X_1754', KL_CTX.KL_LOC_V2825_1752[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_tx42x45def, [[symdic.symdic_kl_define, [KL_CTX.KL_LOC_F_1753, KL_CTX.KL_LOC_X_1754]], KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2825_1752) else False)][(-1)] if shen_eq(symdic.symdic_kl_define, KL_CTX.KL_LOC_V2824_1751) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2823_1750) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1755', [setattr(KL_CTX, 'KL_LOC_V2826_1756', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2827_1757', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2826_1756[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2828_1758', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2826_1756[1], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_F_1759', KL_CTX.KL_LOC_V2828_1758[0]), [setattr(KL_CTX, 'KL_LOC_X_1760', KL_CTX.KL_LOC_V2828_1758[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_1505, KL_ARG_V2880_1503, (lambda : tail_call(shen_tx42x45defcc, [[symdic.symdic_kl_defcc, [KL_CTX.KL_LOC_F_1759, KL_CTX.KL_LOC_X_1760]], KL_ARG_V2878_1501, KL_ARG_V2879_1502, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2828_1758) else False)][(-1)] if shen_eq(symdic.symdic_kl_defcc, KL_CTX.KL_LOC_V2827_1757) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2826_1756) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1761', [setattr(KL_CTX, 'KL_LOC_V2829_1762', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2830_1763', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2829_1762[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2831_1764', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2831_1764) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2831_1764, symdic.symdic_kl_symbol, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1765', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2831_1764, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1765][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2831_1764]) else False))][(-1)] if shen_eq(symdic.symdic_shen_processx45datatype, KL_CTX.KL_LOC_V2830_1763) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2829_1762) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1766', [setattr(KL_CTX, 'KL_LOC_V2832_1767', tco_apply(shen_lazyderef, [KL_ARG_V2877_1500, KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2833_1768', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2832_1767[0], KL_ARG_V2880_1503])), ([setattr(KL_CTX, 'KL_LOC_V2834_1769', tco_apply(shen_lazyderef, [KL_ARG_V2878_1501, KL_ARG_V2880_1503])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2834_1769) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2834_1769, symdic.symdic_kl_symbol, KL_ARG_V2880_1503]), [setattr(KL_CTX, 'KL_LOC_Result_1770', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2881_1504])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2834_1769, KL_ARG_V2880_1503]), KL_CTX.KL_LOC_Result_1770][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2834_1769]) else False))][(-1)] if shen_eq(symdic.symdic_shen_synonymsx45help, KL_CTX.KL_LOC_V2833_1768) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2832_1767) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Datatypes_1771', tco_apply(shen_newpv, [KL_ARG_V2880_1503])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Datatypes_1771, shen_get(symdic.symdic_shen_x42datatypesx42), KL_ARG_V2880_1503, (lambda : tail_call(shen_udefsx42, [[KL_ARG_V2877_1500, [symdic.symdic_kl_x58, [KL_ARG_V2878_1501, []]]], KL_ARG_V2879_1502, KL_CTX.KL_LOC_Datatypes_1771, KL_ARG_V2880_1503, KL_ARG_V2881_1504]))])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1766, False) else KL_CTX.KL_LOC_Case_1766)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1761, False) else KL_CTX.KL_LOC_Case_1761)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1755, False) else KL_CTX.KL_LOC_Case_1755)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1749, False) else KL_CTX.KL_LOC_Case_1749)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1747, False) else KL_CTX.KL_LOC_Case_1747)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1741, False) else KL_CTX.KL_LOC_Case_1741)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1732, False) else KL_CTX.KL_LOC_Case_1732)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1724, False) else KL_CTX.KL_LOC_Case_1724)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1715, False) else KL_CTX.KL_LOC_Case_1715)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1706, False) else KL_CTX.KL_LOC_Case_1706)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1698, False) else KL_CTX.KL_LOC_Case_1698)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1671, False) else KL_CTX.KL_LOC_Case_1671)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1658, False) else KL_CTX.KL_LOC_Case_1658)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1612, False) else KL_CTX.KL_LOC_Case_1612)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1602, False) else KL_CTX.KL_LOC_Case_1602)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1577, False) else KL_CTX.KL_LOC_Case_1577)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1547, False) else KL_CTX.KL_LOC_Case_1547)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1522, False) else KL_CTX.KL_LOC_Case_1522)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1515, False) else KL_CTX.KL_LOC_Case_1515)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1511, False) else KL_CTX.KL_LOC_Case_1511)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1510, False) else KL_CTX.KL_LOC_Case_1510)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1509, False) else KL_CTX.KL_LOC_Case_1509)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1507, False) else KL_CTX.KL_LOC_Case_1507)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1506, False) else KL_CTX.KL_LOC_Case_1506)][(-1)]])][(-1)]
shen_add_fun('shen.th*', shen_thx42)

@tail_recursion
def shen_tx42x45hyps(KL_ARG_V2882_1772, KL_ARG_V2883_1773, KL_ARG_V2884_1774, KL_ARG_V2885_1775):

    class KL_Context:
        KL_LOC_Case_1776 = None
        KL_LOC_V2628_1777 = None
        KL_LOC_V2629_1778 = None
        KL_LOC_V2630_1779 = None
        KL_LOC_V2631_1780 = None
        KL_LOC_V2632_1781 = None
        KL_LOC_X_1782 = None
        KL_LOC_V2633_1783 = None
        KL_LOC_Y_1784 = None
        KL_LOC_V2634_1785 = None
        KL_LOC_V2635_1786 = None
        KL_LOC_V2636_1787 = None
        KL_LOC_V2637_1788 = None
        KL_LOC_V2638_1789 = None
        KL_LOC_V2639_1790 = None
        KL_LOC_V2640_1791 = None
        KL_LOC_A_1792 = None
        KL_LOC_V2641_1793 = None
        KL_LOC_V2642_1794 = None
        KL_LOC_Hyp_1795 = None
        KL_LOC_Result_1796 = None
        KL_LOC_Hyp_1797 = None
        KL_LOC_Result_1798 = None
        KL_LOC_V2643_1799 = None
        KL_LOC_Hyp_1800 = None
        KL_LOC_Result_1801 = None
        KL_LOC_Hyp_1802 = None
        KL_LOC_A_1803 = None
        KL_LOC_Result_1804 = None
        KL_LOC_V2644_1805 = None
        KL_LOC_Hyp_1806 = None
        KL_LOC_Result_1807 = None
        KL_LOC_Hyp_1808 = None
        KL_LOC_Result_1809 = None
        KL_LOC_V2645_1810 = None
        KL_LOC_A_1811 = None
        KL_LOC_V2646_1812 = None
        KL_LOC_V2647_1813 = None
        KL_LOC_Hyp_1814 = None
        KL_LOC_Result_1815 = None
        KL_LOC_Hyp_1816 = None
        KL_LOC_Result_1817 = None
        KL_LOC_V2648_1818 = None
        KL_LOC_Hyp_1819 = None
        KL_LOC_Result_1820 = None
        KL_LOC_Hyp_1821 = None
        KL_LOC_A_1822 = None
        KL_LOC_Result_1823 = None
        KL_LOC_V2649_1824 = None
        KL_LOC_Hyp_1825 = None
        KL_LOC_Result_1826 = None
        KL_LOC_Hyp_1827 = None
        KL_LOC_A_1828 = None
        KL_LOC_Result_1829 = None
        KL_LOC_V2650_1830 = None
        KL_LOC_Hyp_1831 = None
        KL_LOC_Result_1832 = None
        KL_LOC_Hyp_1833 = None
        KL_LOC_Case_1834 = None
        KL_LOC_V2651_1835 = None
        KL_LOC_V2652_1836 = None
        KL_LOC_V2653_1837 = None
        KL_LOC_V2654_1838 = None
        KL_LOC_V2655_1839 = None
        KL_LOC_X_1840 = None
        KL_LOC_V2656_1841 = None
        KL_LOC_Y_1842 = None
        KL_LOC_V2657_1843 = None
        KL_LOC_V2658_1844 = None
        KL_LOC_V2659_1845 = None
        KL_LOC_V2660_1846 = None
        KL_LOC_V2661_1847 = None
        KL_LOC_A_1848 = None
        KL_LOC_V2662_1849 = None
        KL_LOC_V2663_1850 = None
        KL_LOC_V2664_1851 = None
        KL_LOC_B_1852 = None
        KL_LOC_V2665_1853 = None
        KL_LOC_V2666_1854 = None
        KL_LOC_Hyp_1855 = None
        KL_LOC_Result_1856 = None
        KL_LOC_Hyp_1857 = None
        KL_LOC_Result_1858 = None
        KL_LOC_V2667_1859 = None
        KL_LOC_Hyp_1860 = None
        KL_LOC_Result_1861 = None
        KL_LOC_Hyp_1862 = None
        KL_LOC_B_1863 = None
        KL_LOC_Result_1864 = None
        KL_LOC_V2668_1865 = None
        KL_LOC_Hyp_1866 = None
        KL_LOC_Result_1867 = None
        KL_LOC_Hyp_1868 = None
        KL_LOC_Result_1869 = None
        KL_LOC_V2669_1870 = None
        KL_LOC_B_1871 = None
        KL_LOC_V2670_1872 = None
        KL_LOC_V2671_1873 = None
        KL_LOC_Hyp_1874 = None
        KL_LOC_Result_1875 = None
        KL_LOC_Hyp_1876 = None
        KL_LOC_Result_1877 = None
        KL_LOC_V2672_1878 = None
        KL_LOC_Hyp_1879 = None
        KL_LOC_Result_1880 = None
        KL_LOC_Hyp_1881 = None
        KL_LOC_B_1882 = None
        KL_LOC_Result_1883 = None
        KL_LOC_V2673_1884 = None
        KL_LOC_Hyp_1885 = None
        KL_LOC_Result_1886 = None
        KL_LOC_Hyp_1887 = None
        KL_LOC_B_1888 = None
        KL_LOC_Result_1889 = None
        KL_LOC_V2674_1890 = None
        KL_LOC_Hyp_1891 = None
        KL_LOC_Result_1892 = None
        KL_LOC_Hyp_1893 = None
        KL_LOC_A_1894 = None
        KL_LOC_B_1895 = None
        KL_LOC_Result_1896 = None
        KL_LOC_V2675_1897 = None
        KL_LOC_Hyp_1898 = None
        KL_LOC_Result_1899 = None
        KL_LOC_Hyp_1900 = None
        KL_LOC_Case_1901 = None
        KL_LOC_V2676_1902 = None
        KL_LOC_V2677_1903 = None
        KL_LOC_V2678_1904 = None
        KL_LOC_V2679_1905 = None
        KL_LOC_V2680_1906 = None
        KL_LOC_X_1907 = None
        KL_LOC_V2681_1908 = None
        KL_LOC_Y_1909 = None
        KL_LOC_V2682_1910 = None
        KL_LOC_V2683_1911 = None
        KL_LOC_V2684_1912 = None
        KL_LOC_V2685_1913 = None
        KL_LOC_V2686_1914 = None
        KL_LOC_V2687_1915 = None
        KL_LOC_V2688_1916 = None
        KL_LOC_A_1917 = None
        KL_LOC_V2689_1918 = None
        KL_LOC_V2690_1919 = None
        KL_LOC_Hyp_1920 = None
        KL_LOC_Result_1921 = None
        KL_LOC_Hyp_1922 = None
        KL_LOC_Result_1923 = None
        KL_LOC_V2691_1924 = None
        KL_LOC_Hyp_1925 = None
        KL_LOC_Result_1926 = None
        KL_LOC_Hyp_1927 = None
        KL_LOC_A_1928 = None
        KL_LOC_Result_1929 = None
        KL_LOC_V2692_1930 = None
        KL_LOC_Hyp_1931 = None
        KL_LOC_Result_1932 = None
        KL_LOC_Hyp_1933 = None
        KL_LOC_Result_1934 = None
        KL_LOC_V2693_1935 = None
        KL_LOC_A_1936 = None
        KL_LOC_V2694_1937 = None
        KL_LOC_V2695_1938 = None
        KL_LOC_Hyp_1939 = None
        KL_LOC_Result_1940 = None
        KL_LOC_Hyp_1941 = None
        KL_LOC_Result_1942 = None
        KL_LOC_V2696_1943 = None
        KL_LOC_Hyp_1944 = None
        KL_LOC_Result_1945 = None
        KL_LOC_Hyp_1946 = None
        KL_LOC_A_1947 = None
        KL_LOC_Result_1948 = None
        KL_LOC_V2697_1949 = None
        KL_LOC_Hyp_1950 = None
        KL_LOC_Result_1951 = None
        KL_LOC_Hyp_1952 = None
        KL_LOC_A_1953 = None
        KL_LOC_Result_1954 = None
        KL_LOC_V2698_1955 = None
        KL_LOC_Hyp_1956 = None
        KL_LOC_Result_1957 = None
        KL_LOC_Hyp_1958 = None
        KL_LOC_Case_1959 = None
        KL_LOC_V2699_1960 = None
        KL_LOC_V2700_1961 = None
        KL_LOC_V2701_1962 = None
        KL_LOC_V2702_1963 = None
        KL_LOC_V2703_1964 = None
        KL_LOC_X_1965 = None
        KL_LOC_V2704_1966 = None
        KL_LOC_Y_1967 = None
        KL_LOC_V2705_1968 = None
        KL_LOC_V2706_1969 = None
        KL_LOC_V2707_1970 = None
        KL_LOC_V2708_1971 = None
        KL_LOC_V2709_1972 = None
        KL_LOC_V2710_1973 = None
        KL_LOC_Hyp_1974 = None
        KL_LOC_Result_1975 = None
        KL_LOC_Hyp_1976 = None
        KL_LOC_Result_1977 = None
        KL_LOC_V2711_1978 = None
        KL_LOC_Hyp_1979 = None
        KL_LOC_Result_1980 = None
        KL_LOC_Hyp_1981 = None
        KL_LOC_V2712_1982 = None
        KL_LOC_X_1983 = None
        KL_LOC_Hyp_1984 = None
        KL_LOC_NewHyps_1985 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_1776', [setattr(KL_CTX, 'KL_LOC_V2628_1777', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2629_1778', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2628_1777[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2630_1779', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2629_1778[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2631_1780', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2630_1779[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2632_1781', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2630_1779[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1782', KL_CTX.KL_LOC_V2632_1781[0]), [setattr(KL_CTX, 'KL_LOC_V2633_1783', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2632_1781[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1784', KL_CTX.KL_LOC_V2633_1783[0]), [setattr(KL_CTX, 'KL_LOC_V2634_1785', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2633_1783[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2635_1786', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2629_1778[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2636_1787', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2635_1786[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2637_1788', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2635_1786[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2638_1789', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2639_1790', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2638_1789[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2640_1791', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2638_1789[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1792', KL_CTX.KL_LOC_V2640_1791[0]), [setattr(KL_CTX, 'KL_LOC_V2641_1793', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2640_1791[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2642_1794', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1795', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1795, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2642_1794) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2642_1794, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1796', [setattr(KL_CTX, 'KL_LOC_Hyp_1797', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1797, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2642_1794, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1796][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2642_1794]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2641_1793) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2641_1793, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1798', [setattr(KL_CTX, 'KL_LOC_V2643_1799', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1800', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1800, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2643_1799) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2643_1799, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1801', [setattr(KL_CTX, 'KL_LOC_Hyp_1802', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1792, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1802, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2643_1799, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1801][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2643_1799]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2641_1793, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1798][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2641_1793]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2640_1791) else ([setattr(KL_CTX, 'KL_LOC_A_1803', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2640_1791, [KL_CTX.KL_LOC_A_1803, []], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1804', [setattr(KL_CTX, 'KL_LOC_V2644_1805', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1806', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1806, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2644_1805) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2644_1805, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1807', [setattr(KL_CTX, 'KL_LOC_Hyp_1808', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1803, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1808, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2644_1805, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1807][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2644_1805]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2640_1791, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1804][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2640_1791]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2639_1790) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2639_1790, symdic.symdic_kl_list, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1809', [setattr(KL_CTX, 'KL_LOC_V2645_1810', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2638_1789[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1811', KL_CTX.KL_LOC_V2645_1810[0]), [setattr(KL_CTX, 'KL_LOC_V2646_1812', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2645_1810[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2647_1813', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1814', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1814, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2647_1813) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2647_1813, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1815', [setattr(KL_CTX, 'KL_LOC_Hyp_1816', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1816, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2647_1813, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1815][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2647_1813]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2646_1812) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2646_1812, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1817', [setattr(KL_CTX, 'KL_LOC_V2648_1818', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1819', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1819, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2648_1818) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2648_1818, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1820', [setattr(KL_CTX, 'KL_LOC_Hyp_1821', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1811, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1821, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2648_1818, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1820][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2648_1818]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2646_1812, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1817][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2646_1812]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2645_1810) else ([setattr(KL_CTX, 'KL_LOC_A_1822', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2645_1810, [KL_CTX.KL_LOC_A_1822, []], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1823', [setattr(KL_CTX, 'KL_LOC_V2649_1824', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1825', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1825, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2649_1824) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2649_1824, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1826', [setattr(KL_CTX, 'KL_LOC_Hyp_1827', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1822, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1827, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2649_1824, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1826][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2649_1824]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2645_1810, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1823][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2645_1810]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2639_1790, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1809][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2639_1790]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2638_1789) else ([setattr(KL_CTX, 'KL_LOC_A_1828', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2638_1789, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_1828, []]], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1829', [setattr(KL_CTX, 'KL_LOC_V2650_1830', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2637_1788[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1831', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1831, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2650_1830) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2650_1830, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1832', [setattr(KL_CTX, 'KL_LOC_Hyp_1833', KL_CTX.KL_LOC_V2628_1777[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1782, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1784, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1828, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1833, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2650_1830, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1832][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2650_1830]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2638_1789, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1829][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2638_1789]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2637_1788) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2636_1787) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2635_1786) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2634_1785) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2633_1783) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2632_1781) else False)][(-1)] if shen_eq(symdic.symdic_kl_cons, KL_CTX.KL_LOC_V2631_1780) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2630_1779) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2629_1778) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2628_1777) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1834', [setattr(KL_CTX, 'KL_LOC_V2651_1835', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2652_1836', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2651_1835[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2653_1837', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2652_1836[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2654_1838', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2653_1837[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2655_1839', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2653_1837[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1840', KL_CTX.KL_LOC_V2655_1839[0]), [setattr(KL_CTX, 'KL_LOC_V2656_1841', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2655_1839[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1842', KL_CTX.KL_LOC_V2656_1841[0]), [setattr(KL_CTX, 'KL_LOC_V2657_1843', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2656_1841[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2658_1844', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2652_1836[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2659_1845', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2658_1844[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2660_1846', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2658_1844[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2661_1847', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1848', KL_CTX.KL_LOC_V2661_1847[0]), [setattr(KL_CTX, 'KL_LOC_V2662_1849', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2661_1847[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2663_1850', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2662_1849[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2664_1851', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2662_1849[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_B_1852', KL_CTX.KL_LOC_V2664_1851[0]), [setattr(KL_CTX, 'KL_LOC_V2665_1853', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2664_1851[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2666_1854', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1855', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1855, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2666_1854) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2666_1854, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1856', [setattr(KL_CTX, 'KL_LOC_Hyp_1857', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1857, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2666_1854, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1856][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2666_1854]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2665_1853) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2665_1853, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1858', [setattr(KL_CTX, 'KL_LOC_V2667_1859', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1860', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1860, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2667_1859) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2667_1859, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1861', [setattr(KL_CTX, 'KL_LOC_Hyp_1862', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1852, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1862, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2667_1859, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1861][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2667_1859]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2665_1853, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1858][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2665_1853]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2664_1851) else ([setattr(KL_CTX, 'KL_LOC_B_1863', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2664_1851, [KL_CTX.KL_LOC_B_1863, []], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1864', [setattr(KL_CTX, 'KL_LOC_V2668_1865', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1866', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1863, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1866, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2668_1865) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2668_1865, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1867', [setattr(KL_CTX, 'KL_LOC_Hyp_1868', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1863, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1868, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2668_1865, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1867][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2668_1865]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2664_1851, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1864][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2664_1851]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x42, KL_CTX.KL_LOC_V2663_1850) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2663_1850, symdic.symdic_kl_x42, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1869', [setattr(KL_CTX, 'KL_LOC_V2669_1870', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2662_1849[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_B_1871', KL_CTX.KL_LOC_V2669_1870[0]), [setattr(KL_CTX, 'KL_LOC_V2670_1872', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2669_1870[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2671_1873', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1874', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1874, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2671_1873) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2671_1873, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1875', [setattr(KL_CTX, 'KL_LOC_Hyp_1876', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1876, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2671_1873, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1875][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2671_1873]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2670_1872) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2670_1872, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1877', [setattr(KL_CTX, 'KL_LOC_V2672_1878', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1879', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1879, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2672_1878) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2672_1878, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1880', [setattr(KL_CTX, 'KL_LOC_Hyp_1881', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1871, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1881, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2672_1878, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1880][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2672_1878]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2670_1872, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1877][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2670_1872]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2669_1870) else ([setattr(KL_CTX, 'KL_LOC_B_1882', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2669_1870, [KL_CTX.KL_LOC_B_1882, []], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1883', [setattr(KL_CTX, 'KL_LOC_V2673_1884', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1885', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1882, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1885, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2673_1884) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2673_1884, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1886', [setattr(KL_CTX, 'KL_LOC_Hyp_1887', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1882, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1887, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2673_1884, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1886][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2673_1884]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2669_1870, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1883][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2669_1870]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2663_1850, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1869][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2663_1850]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2662_1849) else ([setattr(KL_CTX, 'KL_LOC_B_1888', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2662_1849, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1888, []]], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1889', [setattr(KL_CTX, 'KL_LOC_V2674_1890', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1891', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1888, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1891, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2674_1890) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2674_1890, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1892', [setattr(KL_CTX, 'KL_LOC_Hyp_1893', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1848, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1888, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1893, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2674_1890, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1892][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2674_1890]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2662_1849, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1889][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2662_1849]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2661_1847) else ([setattr(KL_CTX, 'KL_LOC_A_1894', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [setattr(KL_CTX, 'KL_LOC_B_1895', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2661_1847, [KL_CTX.KL_LOC_A_1894, [symdic.symdic_kl_x42, [KL_CTX.KL_LOC_B_1895, []]]], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1896', [setattr(KL_CTX, 'KL_LOC_V2675_1897', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2660_1846[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1898', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1894, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1895, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1898, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2675_1897) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2675_1897, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1899', [setattr(KL_CTX, 'KL_LOC_Hyp_1900', KL_CTX.KL_LOC_V2651_1835[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1840, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1894, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1842, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_1895, KL_ARG_V2884_1774]), []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1900, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2675_1897, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1899][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2675_1897]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2661_1847, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1896][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2661_1847]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2660_1846) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2659_1845) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2658_1844) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2657_1843) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2656_1841) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2655_1839) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64p, KL_CTX.KL_LOC_V2654_1838) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2653_1837) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2652_1836) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2651_1835) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1901', [setattr(KL_CTX, 'KL_LOC_V2676_1902', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2677_1903', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2676_1902[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2678_1904', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2677_1903[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2679_1905', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2678_1904[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2680_1906', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2678_1904[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1907', KL_CTX.KL_LOC_V2680_1906[0]), [setattr(KL_CTX, 'KL_LOC_V2681_1908', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2680_1906[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1909', KL_CTX.KL_LOC_V2681_1908[0]), [setattr(KL_CTX, 'KL_LOC_V2682_1910', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2681_1908[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2683_1911', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2677_1903[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2684_1912', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2683_1911[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2685_1913', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2683_1911[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2686_1914', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2687_1915', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2686_1914[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2688_1916', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2686_1914[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1917', KL_CTX.KL_LOC_V2688_1916[0]), [setattr(KL_CTX, 'KL_LOC_V2689_1918', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2688_1916[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2690_1919', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1920', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1920, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2690_1919) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2690_1919, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1921', [setattr(KL_CTX, 'KL_LOC_Hyp_1922', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1922, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2690_1919, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1921][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2690_1919]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2689_1918) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2689_1918, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1923', [setattr(KL_CTX, 'KL_LOC_V2691_1924', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1925', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1925, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2691_1924) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2691_1924, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1926', [setattr(KL_CTX, 'KL_LOC_Hyp_1927', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1917, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1927, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2691_1924, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1926][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2691_1924]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2689_1918, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1923][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2689_1918]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2688_1916) else ([setattr(KL_CTX, 'KL_LOC_A_1928', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2688_1916, [KL_CTX.KL_LOC_A_1928, []], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1929', [setattr(KL_CTX, 'KL_LOC_V2692_1930', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1931', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1931, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2692_1930) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2692_1930, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1932', [setattr(KL_CTX, 'KL_LOC_Hyp_1933', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1928, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1933, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2692_1930, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1932][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2692_1930]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2688_1916, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1929][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2688_1916]) else False))][(-1)] if shen_eq(symdic.symdic_kl_vector, KL_CTX.KL_LOC_V2687_1915) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2687_1915, symdic.symdic_kl_vector, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1934', [setattr(KL_CTX, 'KL_LOC_V2693_1935', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2686_1914[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_A_1936', KL_CTX.KL_LOC_V2693_1935[0]), [setattr(KL_CTX, 'KL_LOC_V2694_1937', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2693_1935[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2695_1938', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1939', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1939, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2695_1938) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2695_1938, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1940', [setattr(KL_CTX, 'KL_LOC_Hyp_1941', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1941, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2695_1938, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1940][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2695_1938]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2694_1937) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2694_1937, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1942', [setattr(KL_CTX, 'KL_LOC_V2696_1943', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1944', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1944, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2696_1943) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2696_1943, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1945', [setattr(KL_CTX, 'KL_LOC_Hyp_1946', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1936, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1946, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2696_1943, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1945][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2696_1943]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2694_1937, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1942][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2694_1937]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2693_1935) else ([setattr(KL_CTX, 'KL_LOC_A_1947', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2693_1935, [KL_CTX.KL_LOC_A_1947, []], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1948', [setattr(KL_CTX, 'KL_LOC_V2697_1949', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1950', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1950, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2697_1949) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2697_1949, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1951', [setattr(KL_CTX, 'KL_LOC_Hyp_1952', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1947, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1952, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2697_1949, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1951][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2697_1949]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2693_1935, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1948][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2693_1935]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2687_1915, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1934][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2687_1915]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2686_1914) else ([setattr(KL_CTX, 'KL_LOC_A_1953', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2686_1914, [symdic.symdic_kl_vector, [KL_CTX.KL_LOC_A_1953, []]], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1954', [setattr(KL_CTX, 'KL_LOC_V2698_1955', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2685_1913[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1956', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1956, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2698_1955) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2698_1955, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1957', [setattr(KL_CTX, 'KL_LOC_Hyp_1958', KL_CTX.KL_LOC_V2676_1902[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1907, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1909, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [[symdic.symdic_kl_vector, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_1953, KL_ARG_V2884_1774]), []]], []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1958, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2698_1955, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1957][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2698_1955]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2686_1914, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1954][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2686_1914]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2685_1913) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2684_1912) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2683_1911) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2682_1910) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2681_1908) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2680_1906) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64v, KL_CTX.KL_LOC_V2679_1905) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2678_1904) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2677_1903) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2676_1902) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_1959', [setattr(KL_CTX, 'KL_LOC_V2699_1960', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2700_1961', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2699_1960[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2701_1962', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2700_1961[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2702_1963', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2701_1962[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2703_1964', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2701_1962[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1965', KL_CTX.KL_LOC_V2703_1964[0]), [setattr(KL_CTX, 'KL_LOC_V2704_1966', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2703_1964[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Y_1967', KL_CTX.KL_LOC_V2704_1966[0]), [setattr(KL_CTX, 'KL_LOC_V2705_1968', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2704_1966[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2706_1969', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2700_1961[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2707_1970', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2706_1969[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2708_1971', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2706_1969[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2709_1972', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2708_1971[0], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_V2710_1973', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2708_1971[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1974', KL_CTX.KL_LOC_V2699_1960[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1974, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2710_1973) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2710_1973, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1975', [setattr(KL_CTX, 'KL_LOC_Hyp_1976', KL_CTX.KL_LOC_V2699_1960[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1976, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2710_1973, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1975][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2710_1973]) else False))][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2709_1972) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2709_1972, symdic.symdic_kl_string, KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1977', [setattr(KL_CTX, 'KL_LOC_V2711_1978', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2708_1971[1], KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_Hyp_1979', KL_CTX.KL_LOC_V2699_1960[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1979, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2711_1978) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2711_1978, [], KL_ARG_V2884_1774]), [setattr(KL_CTX, 'KL_LOC_Result_1980', [setattr(KL_CTX, 'KL_LOC_Hyp_1981', KL_CTX.KL_LOC_V2699_1960[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_ARG_V2883_1773, [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1965, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], [[tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Y_1967, KL_ARG_V2884_1774]), [symdic.symdic_kl_x58, [symdic.symdic_kl_string, []]]], tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Hyp_1981, KL_ARG_V2884_1774])]], KL_ARG_V2884_1774, KL_ARG_V2885_1775])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2711_1978, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1980][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2711_1978]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2709_1972, KL_ARG_V2884_1774]), KL_CTX.KL_LOC_Result_1977][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2709_1972]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2708_1971) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2707_1970) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2706_1969) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2705_1968) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2704_1966) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2703_1964) else False)][(-1)] if shen_eq(symdic.symdic_kl_x64s, KL_CTX.KL_LOC_V2702_1963) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2701_1962) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2700_1961) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2699_1960) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2712_1982', tco_apply(shen_lazyderef, [KL_ARG_V2882_1772, KL_ARG_V2884_1774])), ([setattr(KL_CTX, 'KL_LOC_X_1983', KL_CTX.KL_LOC_V2712_1982[0]), [setattr(KL_CTX, 'KL_LOC_Hyp_1984', KL_CTX.KL_LOC_V2712_1982[1]), [setattr(KL_CTX, 'KL_LOC_NewHyps_1985', tco_apply(shen_newpv, [KL_ARG_V2884_1774])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V2883_1773, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_1983, KL_ARG_V2884_1774]), tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_NewHyps_1985, KL_ARG_V2884_1774])], KL_ARG_V2884_1774, (lambda : tail_call(shen_tx42x45hyps, [KL_CTX.KL_LOC_Hyp_1984, KL_CTX.KL_LOC_NewHyps_1985, KL_ARG_V2884_1774, KL_ARG_V2885_1775]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2712_1982) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1959, False) else KL_CTX.KL_LOC_Case_1959)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1901, False) else KL_CTX.KL_LOC_Case_1901)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1834, False) else KL_CTX.KL_LOC_Case_1834)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_1776, False) else KL_CTX.KL_LOC_Case_1776)][(-1)]
shen_add_fun('shen.t*-hyps', shen_tx42x45hyps)

@tail_recursion
def shen_show(KL_ARG_V2898_1986, KL_ARG_V2899_1987, KL_ARG_V2900_1988, KL_ARG_V2901_1989):
    global symdic
    return ([tco_apply(shen_line, []), [tco_apply(shen_showx45p, [tco_apply(shen_deref, [KL_ARG_V2898_1986, KL_ARG_V2900_1988])]), [tco_apply(kl_nl, [1]), [tco_apply(kl_nl, [1]), [tco_apply(shen_showx45assumptions, [tco_apply(shen_deref, [KL_ARG_V2899_1987, KL_ARG_V2900_1988]), 1]), [tco_apply(shen_prhush, ['\r\n> ', tco_apply(kl_stoutput, [])]), [tco_apply(shen_pausex45forx45user, [shen_get(symdic.symdic_kl_x42languagex42)]), tail_call(kl_thaw, [KL_ARG_V2901_1989])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_get(symdic.symdic_shen_x42spyx42) else (tail_call(kl_thaw, [KL_ARG_V2901_1989]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show', shen_show)

@tail_recursion
def shen_line():

    class KL_Context:
        KL_LOC_Infs_1990 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Infs_1990', tco_apply(kl_inferences, [])), tail_call(shen_prhush, [('____________________________________________________________ ' + tco_apply(shen_app, [KL_CTX.KL_LOC_Infs_1990, (' inference' + tco_apply(shen_app, [('' if shen_eq(1, KL_CTX.KL_LOC_Infs_1990) else 's'), ' \r\n?- ', symdic.symdic_shen_a])), symdic.symdic_shen_a])), tco_apply(kl_stoutput, [])])][(-1)]
shen_add_fun('shen.line', shen_line)

@tail_recursion
def shen_showx45p(KL_ARG_V2902_1991):
    global symdic
    return (tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2902_1991[0], (' : ' + tco_apply(shen_app, [KL_ARG_V2902_1991[1][1][0], '', symdic.symdic_shen_r])), symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])]) if ((((shen_eq([], KL_ARG_V2902_1991[1][1][1]) if shen_consp(KL_ARG_V2902_1991[1][1]) else False) if shen_eq(symdic.symdic_kl_x58, KL_ARG_V2902_1991[1][0]) else False) if shen_consp(KL_ARG_V2902_1991[1]) else False) if shen_consp(KL_ARG_V2902_1991) else False) else (tail_call(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2902_1991, '', symdic.symdic_shen_r]), tco_apply(kl_stoutput, [])]) if True else shen_simple_error('condition failure')))
shen_add_fun('shen.show-p', shen_showx45p)

@tail_recursion
def shen_showx45assumptions(KL_ARG_V2905_1992, KL_ARG_V2906_1993):
    global symdic
    return (symdic.symdic_shen_skip if shen_eq([], KL_ARG_V2905_1992) else ([tco_apply(shen_prhush, [tco_apply(shen_app, [KL_ARG_V2906_1993, '. ', symdic.symdic_shen_a]), tco_apply(kl_stoutput, [])]), [tco_apply(shen_showx45p, [KL_ARG_V2905_1992[0]]), [tco_apply(kl_nl, [1]), tail_call(shen_showx45assumptions, [KL_ARG_V2905_1992[1], (KL_ARG_V2906_1993 + 1)])][(-1)]][(-1)]][(-1)] if shen_consp(KL_ARG_V2905_1992) else (tail_call(shen_sysx45error, [symdic.symdic_shen_showx45assumptions]) if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.show-assumptions', shen_showx45assumptions)

@tail_recursion
def shen_pausex45forx45user(KL_ARG_V2911_1994):

    class KL_Context:
        KL_LOC_I_1995 = None
        KL_LOC_I_1996 = None
    KL_CTX = KL_Context()
    global symdic
    return ([setattr(KL_CTX, 'KL_LOC_I_1995', tco_apply(FORMAT, [[], '~C', tco_apply(READx45CHAR, [])])), (shen_simple_error('input aborted\r\n') if shen_eq(KL_CTX.KL_LOC_I_1995, 'a') else tail_call(kl_nl, [1]))][(-1)] if shen_eq('Common Lisp', KL_ARG_V2911_1994) else ([setattr(KL_CTX, 'KL_LOC_I_1996', tco_apply(shen_readx45char, [])), (shen_simple_error('input aborted\r\n') if shen_eq(KL_CTX.KL_LOC_I_1996, 'a') else tail_call(kl_nl, [1]))][(-1)] if True else shen_simple_error('condition failure')))
shen_add_fun('shen.pause-for-user', shen_pausex45forx45user)

@tail_recursion
def shen_readx45char():
    global symdic
    return tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0])
shen_add_fun('shen.read-char', shen_readx45char)

@tail_recursion
def shen_readx45charx45h(KL_ARG_V2914_1997, KL_ARG_V2915_1998):
    global symdic
    return (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if (shen_eq(0, KL_ARG_V2915_1998) if shen_eq((-1), KL_ARG_V2914_1997) else False) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 0]) if shen_eq(0, KL_ARG_V2915_1998) else (tail_call(shen_readx45charx45h, [shen_read_byte(tco_apply(kl_stinput, [])), 1]) if (shen_eq(1, KL_ARG_V2915_1998) if shen_eq((-1), KL_ARG_V2914_1997) else False) else (chr(KL_ARG_V2914_1997) if shen_eq(1, KL_ARG_V2915_1998) else (tail_call(shen_sysx45error, [symdic.symdic_shen_readx45charx45h]) if True else shen_simple_error('condition failure'))))))
shen_add_fun('shen.read-char-h', shen_readx45charx45h)

@tail_recursion
def shen_typedfx63(KL_ARG_V2916_1999):
    global symdic
    return shen_consp(tco_apply(kl_assoc, [KL_ARG_V2916_1999, shen_get(symdic.symdic_shen_x42signedfuncsx42)]))
shen_add_fun('shen.typedf?', shen_typedfx63)

@tail_recursion
def shen_sigf(KL_ARG_V2917_2000):
    global symdic
    return tail_call(kl_concat, [symdic.symdic_shen_typex45signaturex45ofx45, KL_ARG_V2917_2000])
shen_add_fun('shen.sigf', shen_sigf)

@tail_recursion
def shen_placeholder():
    global symdic
    return tail_call(kl_gensym, [symdic.symdic_kl_x38x38])
shen_add_fun('shen.placeholder', shen_placeholder)

@tail_recursion
def shen_base(KL_ARG_V2918_2001, KL_ARG_V2919_2002, KL_ARG_V2920_2003, KL_ARG_V2921_2004):

    class KL_Context:
        KL_LOC_Case_2005 = None
        KL_LOC_V2615_2006 = None
        KL_LOC_Result_2007 = None
        KL_LOC_Case_2008 = None
        KL_LOC_V2616_2009 = None
        KL_LOC_Result_2010 = None
        KL_LOC_Case_2011 = None
        KL_LOC_V2617_2012 = None
        KL_LOC_Result_2013 = None
        KL_LOC_Case_2014 = None
        KL_LOC_V2618_2015 = None
        KL_LOC_Result_2016 = None
        KL_LOC_V2619_2017 = None
        KL_LOC_V2620_2018 = None
        KL_LOC_V2621_2019 = None
        KL_LOC_V2622_2020 = None
        KL_LOC_A_2021 = None
        KL_LOC_V2623_2022 = None
        KL_LOC_Result_2023 = None
        KL_LOC_A_2024 = None
        KL_LOC_Result_2025 = None
        KL_LOC_Result_2026 = None
        KL_LOC_V2624_2027 = None
        KL_LOC_A_2028 = None
        KL_LOC_V2625_2029 = None
        KL_LOC_Result_2030 = None
        KL_LOC_A_2031 = None
        KL_LOC_Result_2032 = None
        KL_LOC_A_2033 = None
        KL_LOC_Result_2034 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2005', [setattr(KL_CTX, 'KL_LOC_V2615_2006', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), numbers.Number), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)] if shen_eq(symdic.symdic_kl_number, KL_CTX.KL_LOC_V2615_2006) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2615_2006, symdic.symdic_kl_number, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2007', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), numbers.Number), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2615_2006, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2007][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2615_2006]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2008', [setattr(KL_CTX, 'KL_LOC_V2616_2009', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)] if shen_eq(symdic.symdic_kl_boolean, KL_CTX.KL_LOC_V2616_2009) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2616_2009, symdic.symdic_kl_boolean, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2010', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_booleanx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2616_2009, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2010][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2616_2009]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2011', [setattr(KL_CTX, 'KL_LOC_V2617_2012', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), str), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)] if shen_eq(symdic.symdic_kl_string, KL_CTX.KL_LOC_V2617_2012) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2617_2012, symdic.symdic_kl_string, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2013', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [isinstance(tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003]), str), KL_ARG_V2920_2003, KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2617_2012, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2013][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2617_2012]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2014', [setattr(KL_CTX, 'KL_LOC_V2618_2015', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])])), KL_ARG_V2920_2003, KL_ARG_V2921_2004]))])][(-1)] if shen_eq(symdic.symdic_kl_symbol, KL_CTX.KL_LOC_V2618_2015) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2618_2015, symdic.symdic_kl_symbol, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2016', [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(kl_symbolx63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])]), KL_ARG_V2920_2003, (lambda : tail_call(kl_fwhen, [(not tco_apply(shen_uex63, [tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])])), KL_ARG_V2920_2003, KL_ARG_V2921_2004]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2618_2015, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2016][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2618_2015]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2619_2017', tco_apply(shen_lazyderef, [KL_ARG_V2918_2001, KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_V2620_2018', tco_apply(shen_lazyderef, [KL_ARG_V2919_2002, KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_V2621_2019', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2620_2018[0], KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_V2622_2020', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2620_2018[1], KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_A_2021', KL_CTX.KL_LOC_V2622_2020[0]), [setattr(KL_CTX, 'KL_LOC_V2623_2022', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2622_2020[1], KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tail_call(kl_thaw, [KL_ARG_V2921_2004])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2623_2022) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2623_2022, [], KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2023', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2623_2022, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2023][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2623_2022]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2622_2020) else ([setattr(KL_CTX, 'KL_LOC_A_2024', tco_apply(shen_newpv, [KL_ARG_V2920_2003])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2622_2020, [KL_CTX.KL_LOC_A_2024, []], KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2025', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2622_2020, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2025][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2622_2020]) else False))][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2621_2019) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2621_2019, symdic.symdic_kl_list, KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2026', [setattr(KL_CTX, 'KL_LOC_V2624_2027', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2620_2018[1], KL_ARG_V2920_2003])), ([setattr(KL_CTX, 'KL_LOC_A_2028', KL_CTX.KL_LOC_V2624_2027[0]), [setattr(KL_CTX, 'KL_LOC_V2625_2029', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2624_2027[1], KL_ARG_V2920_2003])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2625_2029) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2625_2029, [], KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2030', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2625_2029, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2030][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2625_2029]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2624_2027) else ([setattr(KL_CTX, 'KL_LOC_A_2031', tco_apply(shen_newpv, [KL_ARG_V2920_2003])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2624_2027, [KL_CTX.KL_LOC_A_2031, []], KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2032', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2624_2027, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2032][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2624_2027]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2621_2019, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2026][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2621_2019]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2620_2018) else ([setattr(KL_CTX, 'KL_LOC_A_2033', tco_apply(shen_newpv, [KL_ARG_V2920_2003])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2620_2018, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2033, []]], KL_ARG_V2920_2003]), [setattr(KL_CTX, 'KL_LOC_Result_2034', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2921_2004])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2620_2018, KL_ARG_V2920_2003]), KL_CTX.KL_LOC_Result_2034][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2620_2018]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2619_2017) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2014, False) else KL_CTX.KL_LOC_Case_2014)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2011, False) else KL_CTX.KL_LOC_Case_2011)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2008, False) else KL_CTX.KL_LOC_Case_2008)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2005, False) else KL_CTX.KL_LOC_Case_2005)][(-1)]
shen_add_fun('shen.base', shen_base)

@tail_recursion
def shen_by_hypothesis(KL_ARG_V2922_2035, KL_ARG_V2923_2036, KL_ARG_V2924_2037, KL_ARG_V2925_2038, KL_ARG_V2926_2039):

    class KL_Context:
        KL_LOC_Case_2040 = None
        KL_LOC_V2606_2041 = None
        KL_LOC_V2607_2042 = None
        KL_LOC_Y_2043 = None
        KL_LOC_V2608_2044 = None
        KL_LOC_V2609_2045 = None
        KL_LOC_V2610_2046 = None
        KL_LOC_B_2047 = None
        KL_LOC_V2611_2048 = None
        KL_LOC_V2612_2049 = None
        KL_LOC_Hyp_2050 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2040', [setattr(KL_CTX, 'KL_LOC_V2606_2041', tco_apply(shen_lazyderef, [KL_ARG_V2924_2037, KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_V2607_2042', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2606_2041[0], KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_Y_2043', KL_CTX.KL_LOC_V2607_2042[0]), [setattr(KL_CTX, 'KL_LOC_V2608_2044', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2607_2042[1], KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_V2609_2045', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2608_2044[0], KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_V2610_2046', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2608_2044[1], KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_B_2047', KL_CTX.KL_LOC_V2610_2046[0]), [setattr(KL_CTX, 'KL_LOC_V2611_2048', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2610_2046[1], KL_ARG_V2925_2038])), ([tco_apply(shen_incinfs, []), tco_apply(kl_identical, [KL_ARG_V2922_2035, KL_CTX.KL_LOC_Y_2043, KL_ARG_V2925_2038, (lambda : tail_call(kl_unifyx33, [KL_ARG_V2923_2036, KL_CTX.KL_LOC_B_2047, KL_ARG_V2925_2038, KL_ARG_V2926_2039]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2611_2048) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2610_2046) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2609_2045) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2608_2044) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2607_2042) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2606_2041) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2612_2049', tco_apply(shen_lazyderef, [KL_ARG_V2924_2037, KL_ARG_V2925_2038])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2050', KL_CTX.KL_LOC_V2612_2049[1]), [tco_apply(shen_incinfs, []), tail_call(shen_by_hypothesis, [KL_ARG_V2922_2035, KL_ARG_V2923_2036, KL_CTX.KL_LOC_Hyp_2050, KL_ARG_V2925_2038, KL_ARG_V2926_2039])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2612_2049) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2040, False) else KL_CTX.KL_LOC_Case_2040)][(-1)]
shen_add_fun('shen.by_hypothesis', shen_by_hypothesis)

@tail_recursion
def shen_tx42x45def(KL_ARG_V2927_2051, KL_ARG_V2928_2052, KL_ARG_V2929_2053, KL_ARG_V2930_2054, KL_ARG_V2931_2055):

    class KL_Context:
        KL_LOC_V2600_2056 = None
        KL_LOC_V2601_2057 = None
        KL_LOC_V2602_2058 = None
        KL_LOC_F_2059 = None
        KL_LOC_X_2060 = None
        KL_LOC_E_2061 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2600_2056', tco_apply(shen_lazyderef, [KL_ARG_V2927_2051, KL_ARG_V2930_2054])), ([setattr(KL_CTX, 'KL_LOC_V2601_2057', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2600_2056[0], KL_ARG_V2930_2054])), ([setattr(KL_CTX, 'KL_LOC_V2602_2058', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2600_2056[1], KL_ARG_V2930_2054])), ([setattr(KL_CTX, 'KL_LOC_F_2059', KL_CTX.KL_LOC_V2602_2058[0]), [setattr(KL_CTX, 'KL_LOC_X_2060', KL_CTX.KL_LOC_V2602_2058[1]), [setattr(KL_CTX, 'KL_LOC_E_2061', tco_apply(shen_newpv, [KL_ARG_V2930_2054])), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defh, [tco_apply(kl_compile, [symdic.symdic_shen_x60sigx43rulesx62, KL_CTX.KL_LOC_X_2060, (lambda KL_ARG_E_2062: (shen_simple_error(('parse error here: ' + tco_apply(shen_app, [KL_ARG_E_2062, '\r\n', symdic.symdic_shen_s]))) if shen_consp(KL_ARG_E_2062) else shen_simple_error('parse error\r\n')))]), KL_CTX.KL_LOC_F_2059, KL_ARG_V2928_2052, KL_ARG_V2929_2053, KL_ARG_V2930_2054, KL_ARG_V2931_2055])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2602_2058) else False)][(-1)] if shen_eq(symdic.symdic_kl_define, KL_CTX.KL_LOC_V2601_2057) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2600_2056) else False)][(-1)]
shen_add_fun('shen.t*-def', shen_tx42x45def)

@tail_recursion
def shen_tx42x45defh(KL_ARG_V2932_2063, KL_ARG_V2933_2064, KL_ARG_V2934_2065, KL_ARG_V2935_2066, KL_ARG_V2936_2067, KL_ARG_V2937_2068):

    class KL_Context:
        KL_LOC_V2596_2069 = None
        KL_LOC_Sig_2070 = None
        KL_LOC_Rules_2071 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_V2596_2069', tco_apply(shen_lazyderef, [KL_ARG_V2932_2063, KL_ARG_V2936_2067])), ([setattr(KL_CTX, 'KL_LOC_Sig_2070', KL_CTX.KL_LOC_V2596_2069[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2071', KL_CTX.KL_LOC_V2596_2069[1]), [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45defhh, [KL_CTX.KL_LOC_Sig_2070, tco_apply(shen_ue, [KL_CTX.KL_LOC_Sig_2070]), KL_ARG_V2933_2064, KL_ARG_V2934_2065, KL_ARG_V2935_2066, KL_CTX.KL_LOC_Rules_2071, KL_ARG_V2936_2067, KL_ARG_V2937_2068])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2596_2069) else False)][(-1)]
shen_add_fun('shen.t*-defh', shen_tx42x45defh)

@tail_recursion
def shen_tx42x45defhh(KL_ARG_V2938_2072, KL_ARG_V2939_2073, KL_ARG_V2940_2074, KL_ARG_V2941_2075, KL_ARG_V2942_2076, KL_ARG_V2943_2077, KL_ARG_V2944_2078, KL_ARG_V2945_2079):
    global symdic
    return [tco_apply(shen_incinfs, []), tail_call(shen_tx42x45rules, [KL_ARG_V2943_2077, KL_ARG_V2939_2073, 1, KL_ARG_V2940_2074, [[KL_ARG_V2940_2074, [symdic.symdic_kl_x58, [KL_ARG_V2939_2073, []]]], KL_ARG_V2942_2076], KL_ARG_V2944_2078, (lambda : tail_call(shen_memo, [KL_ARG_V2940_2074, KL_ARG_V2938_2072, KL_ARG_V2941_2075, KL_ARG_V2944_2078, KL_ARG_V2945_2079]))])][(-1)]
shen_add_fun('shen.t*-defhh', shen_tx42x45defhh)

@tail_recursion
def shen_memo(KL_ARG_V2946_2080, KL_ARG_V2947_2081, KL_ARG_V2948_2082, KL_ARG_V2949_2083, KL_ARG_V2950_2084):

    class KL_Context:
        KL_LOC_Jnk_2085 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Jnk_2085', tco_apply(shen_newpv, [KL_ARG_V2949_2083])), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_ARG_V2948_2082, KL_ARG_V2947_2081, KL_ARG_V2949_2083, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Jnk_2085, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_ARG_V2946_2080, KL_ARG_V2949_2083]), tco_apply(shen_lazyderef, [KL_ARG_V2948_2082, KL_ARG_V2949_2083])]), KL_ARG_V2949_2083, KL_ARG_V2950_2084]))])][(-1)]][(-1)]
shen_add_fun('shen.memo', shen_memo)

@tail_recursion
def shen_x60sigx43rulesx62(KL_ARG_V2955_2086):

    class KL_Context:
        KL_LOC_Result_2087 = None
        KL_LOC_Parse_shen_x60signaturex62_2088 = None
        KL_LOC_Parse_shen_x60rulesx62_2089 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Result_2087', [setattr(KL_CTX, 'KL_LOC_Parse_shen_x60signaturex62_2088', tco_apply(shen_x60signaturex62, [KL_ARG_V2955_2086])), ([setattr(KL_CTX, 'KL_LOC_Parse_shen_x60rulesx62_2089', tco_apply(shen_x60rulesx62, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2088])), (tco_apply(shen_pair, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2089[0], [tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2088]), tco_apply(shen_hdtl, [KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2089])]]) if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60rulesx62_2089)) else tco_apply(kl_fail, []))][(-1)] if (not shen_eq(tco_apply(kl_fail, []), KL_CTX.KL_LOC_Parse_shen_x60signaturex62_2088)) else tco_apply(kl_fail, []))][(-1)]), (tail_call(kl_fail, []) if shen_eq(KL_CTX.KL_LOC_Result_2087, tco_apply(kl_fail, [])) else KL_CTX.KL_LOC_Result_2087)][(-1)]
shen_add_fun('shen.<sig+rules>', shen_x60sigx43rulesx62)

@tail_recursion
def shen_ue(KL_ARG_V2956_2090):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_ue, KL_ARG_V2956_2090]) if shen_consp(KL_ARG_V2956_2090) else (tail_call(kl_concat, [symdic.symdic_kl_x38x38, KL_ARG_V2956_2090]) if tco_apply(kl_variablex63, [KL_ARG_V2956_2090]) else (KL_ARG_V2956_2090 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ue', shen_ue)

@tail_recursion
def shen_ues(KL_ARG_V2961_2091):
    global symdic
    return ([KL_ARG_V2961_2091, []] if tco_apply(shen_uex63, [KL_ARG_V2961_2091]) else (tail_call(kl_union, [tco_apply(shen_ues, [KL_ARG_V2961_2091[0]]), tco_apply(shen_ues, [KL_ARG_V2961_2091[1]])]) if shen_consp(KL_ARG_V2961_2091) else ([] if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.ues', shen_ues)

@tail_recursion
def shen_uex63(KL_ARG_V2962_2092):
    global symdic
    return (tail_call(shen_uex45hx63, [str(KL_ARG_V2962_2092)]) if tco_apply(kl_symbolx63, [KL_ARG_V2962_2092]) else False)
shen_add_fun('shen.ue?', shen_uex63)

@tail_recursion
def shen_uex45hx63(KL_ARG_V2969_2093):
    global symdic
    return (True if (((shen_eq('&', KL_ARG_V2969_2093[1:][0]) if tco_apply(shen_x43stringx63, [KL_ARG_V2969_2093[1:]]) else False) if shen_eq('&', KL_ARG_V2969_2093[0]) else False) if tco_apply(shen_x43stringx63, [KL_ARG_V2969_2093]) else False) else (False if True else shen_simple_error('condition failure')))
shen_add_fun('shen.ue-h?', shen_uex45hx63)

@tail_recursion
def shen_tx42x45rules(KL_ARG_V2970_2094, KL_ARG_V2971_2095, KL_ARG_V2972_2096, KL_ARG_V2973_2097, KL_ARG_V2974_2098, KL_ARG_V2975_2099, KL_ARG_V2976_2100):

    class KL_Context:
        KL_LOC_Throwcontrol_2101 = None
        KL_LOC_Case_2102 = None
        KL_LOC_V2571_2103 = None
        KL_LOC_Case_2104 = None
        KL_LOC_V2572_2105 = None
        KL_LOC_V2573_2106 = None
        KL_LOC_V2574_2107 = None
        KL_LOC_V2575_2108 = None
        KL_LOC_Action_2109 = None
        KL_LOC_V2576_2110 = None
        KL_LOC_Rules_2111 = None
        KL_LOC_V2577_2112 = None
        KL_LOC_V2578_2113 = None
        KL_LOC_V2579_2114 = None
        KL_LOC_A_2115 = None
        KL_LOC_V2580_2116 = None
        KL_LOC_Case_2117 = None
        KL_LOC_V2581_2118 = None
        KL_LOC_Rule_2119 = None
        KL_LOC_Rules_2120 = None
        KL_LOC_Err_2121 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2101', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2101, [setattr(KL_CTX, 'KL_LOC_Case_2102', [setattr(KL_CTX, 'KL_LOC_V2571_2103', tco_apply(shen_lazyderef, [KL_ARG_V2970_2094, KL_ARG_V2975_2099])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2976_2100])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2571_2103) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2104', [setattr(KL_CTX, 'KL_LOC_V2572_2105', tco_apply(shen_lazyderef, [KL_ARG_V2970_2094, KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2573_2106', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2572_2105[0], KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2574_2107', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2573_2106[0], KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2575_2108', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2573_2106[1], KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_Action_2109', KL_CTX.KL_LOC_V2575_2108[0]), [setattr(KL_CTX, 'KL_LOC_V2576_2110', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2575_2108[1], KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_Rules_2111', KL_CTX.KL_LOC_V2572_2105[1]), [setattr(KL_CTX, 'KL_LOC_V2577_2112', tco_apply(shen_lazyderef, [KL_ARG_V2971_2095, KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2578_2113', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2577_2112[0], KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_V2579_2114', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2577_2112[1], KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_A_2115', KL_CTX.KL_LOC_V2579_2114[0]), [setattr(KL_CTX, 'KL_LOC_V2580_2116', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2579_2114[1], KL_ARG_V2975_2099])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [[[], [tco_apply(shen_ue, [KL_CTX.KL_LOC_Action_2109]), []]], KL_CTX.KL_LOC_A_2115, KL_ARG_V2974_2098, KL_ARG_V2975_2099, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2101, KL_ARG_V2975_2099, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2111, KL_CTX.KL_LOC_A_2115, (KL_ARG_V2972_2096 + 1), KL_ARG_V2973_2097, KL_ARG_V2974_2098, KL_ARG_V2975_2099, KL_ARG_V2976_2100]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2580_2116) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2579_2114) else False)][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2578_2113) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2577_2112) else False)][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2576_2110) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2575_2108) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2574_2107) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2573_2106) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2572_2105) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2117', [setattr(KL_CTX, 'KL_LOC_V2581_2118', tco_apply(shen_lazyderef, [KL_ARG_V2970_2094, KL_ARG_V2975_2099])), ([setattr(KL_CTX, 'KL_LOC_Rule_2119', KL_CTX.KL_LOC_V2581_2118[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2120', KL_CTX.KL_LOC_V2581_2118[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45rule, [tco_apply(shen_ue, [KL_CTX.KL_LOC_Rule_2119]), KL_ARG_V2971_2095, KL_ARG_V2974_2098, KL_ARG_V2975_2099, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2101, KL_ARG_V2975_2099, (lambda : tail_call(shen_tx42x45rules, [KL_CTX.KL_LOC_Rules_2120, KL_ARG_V2971_2095, (KL_ARG_V2972_2096 + 1), KL_ARG_V2973_2097, KL_ARG_V2974_2098, KL_ARG_V2975_2099, KL_ARG_V2976_2100]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2581_2118) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2121', tco_apply(shen_newpv, [KL_ARG_V2975_2099])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Err_2121, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2972_2096, KL_ARG_V2975_2099]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V2973_2097, KL_ARG_V2975_2099]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V2975_2099, KL_ARG_V2976_2100])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2117, False) else KL_CTX.KL_LOC_Case_2117)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2104, False) else KL_CTX.KL_LOC_Case_2104)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2102, False) else KL_CTX.KL_LOC_Case_2102)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rules', shen_tx42x45rules)

@tail_recursion
def shen_tx42x45rule(KL_ARG_V2977_2122, KL_ARG_V2978_2123, KL_ARG_V2979_2124, KL_ARG_V2980_2125, KL_ARG_V2981_2126):

    class KL_Context:
        KL_LOC_Throwcontrol_2127 = None
        KL_LOC_Case_2128 = None
        KL_LOC_V2553_2129 = None
        KL_LOC_V2554_2130 = None
        KL_LOC_V2555_2131 = None
        KL_LOC_Action_2132 = None
        KL_LOC_V2556_2133 = None
        KL_LOC_V2557_2134 = None
        KL_LOC_V2558_2135 = None
        KL_LOC_Pattern_2136 = None
        KL_LOC_Patterns_2137 = None
        KL_LOC_V2559_2138 = None
        KL_LOC_Action_2139 = None
        KL_LOC_V2560_2140 = None
        KL_LOC_V2561_2141 = None
        KL_LOC_A_2142 = None
        KL_LOC_V2562_2143 = None
        KL_LOC_V2563_2144 = None
        KL_LOC_V2564_2145 = None
        KL_LOC_B_2146 = None
        KL_LOC_V2565_2147 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2127', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2127, [setattr(KL_CTX, 'KL_LOC_Case_2128', [setattr(KL_CTX, 'KL_LOC_V2553_2129', tco_apply(shen_lazyderef, [KL_ARG_V2977_2122, KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2554_2130', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2553_2129[0], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2555_2131', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2553_2129[1], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_Action_2132', KL_CTX.KL_LOC_V2555_2131[0]), [setattr(KL_CTX, 'KL_LOC_V2556_2133', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2555_2131[1], KL_ARG_V2980_2125])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2127, KL_ARG_V2980_2125, (lambda : tail_call(shen_tx42x45action, [tco_apply(shen_curry, [KL_CTX.KL_LOC_Action_2132]), KL_ARG_V2978_2123, KL_ARG_V2979_2124, KL_ARG_V2980_2125, KL_ARG_V2981_2126]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2556_2133) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2555_2131) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2554_2130) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2553_2129) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2557_2134', tco_apply(shen_lazyderef, [KL_ARG_V2977_2122, KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2558_2135', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2557_2134[0], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_Pattern_2136', KL_CTX.KL_LOC_V2558_2135[0]), [setattr(KL_CTX, 'KL_LOC_Patterns_2137', KL_CTX.KL_LOC_V2558_2135[1]), [setattr(KL_CTX, 'KL_LOC_V2559_2138', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2557_2134[1], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_Action_2139', KL_CTX.KL_LOC_V2559_2138[0]), [setattr(KL_CTX, 'KL_LOC_V2560_2140', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2559_2138[1], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2561_2141', tco_apply(shen_lazyderef, [KL_ARG_V2978_2123, KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_A_2142', KL_CTX.KL_LOC_V2561_2141[0]), [setattr(KL_CTX, 'KL_LOC_V2562_2143', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2561_2141[1], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2563_2144', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2562_2143[0], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_V2564_2145', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2562_2143[1], KL_ARG_V2980_2125])), ([setattr(KL_CTX, 'KL_LOC_B_2146', KL_CTX.KL_LOC_V2564_2145[0]), [setattr(KL_CTX, 'KL_LOC_V2565_2147', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2564_2145[1], KL_ARG_V2980_2125])), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42x45pattern, [KL_CTX.KL_LOC_Pattern_2136, KL_CTX.KL_LOC_A_2142, KL_ARG_V2980_2125, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2127, KL_ARG_V2980_2125, (lambda : tail_call(shen_tx42x45rule, [[KL_CTX.KL_LOC_Patterns_2137, [KL_CTX.KL_LOC_Action_2139, []]], KL_CTX.KL_LOC_B_2146, [[KL_CTX.KL_LOC_Pattern_2136, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2142, []]]], KL_ARG_V2979_2124], KL_ARG_V2980_2125, KL_ARG_V2981_2126]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2565_2147) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2564_2145) else False)][(-1)] if shen_eq(symdic.symdic_kl_x45x45x62, KL_CTX.KL_LOC_V2563_2144) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2562_2143) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2561_2141) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2560_2140) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2559_2138) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2558_2135) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2557_2134) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2128, False) else KL_CTX.KL_LOC_Case_2128)][(-1)]])][(-1)]
shen_add_fun('shen.t*-rule', shen_tx42x45rule)

@tail_recursion
def shen_tx42x45action(KL_ARG_V2982_2148, KL_ARG_V2983_2149, KL_ARG_V2984_2150, KL_ARG_V2985_2151, KL_ARG_V2986_2152):

    class KL_Context:
        KL_LOC_Throwcontrol_2153 = None
        KL_LOC_Case_2154 = None
        KL_LOC_V2530_2155 = None
        KL_LOC_V2531_2156 = None
        KL_LOC_V2532_2157 = None
        KL_LOC_P_2158 = None
        KL_LOC_V2533_2159 = None
        KL_LOC_Action_2160 = None
        KL_LOC_V2534_2161 = None
        KL_LOC_Case_2162 = None
        KL_LOC_V2535_2163 = None
        KL_LOC_V2536_2164 = None
        KL_LOC_V2537_2165 = None
        KL_LOC_V2538_2166 = None
        KL_LOC_V2539_2167 = None
        KL_LOC_V2540_2168 = None
        KL_LOC_V2541_2169 = None
        KL_LOC_F_2170 = None
        KL_LOC_V2542_2171 = None
        KL_LOC_V2543_2172 = None
        KL_LOC_Action_2173 = None
        KL_LOC_V2544_2174 = None
        KL_LOC_V2545_2175 = None
        KL_LOC_Case_2176 = None
        KL_LOC_V2546_2177 = None
        KL_LOC_V2547_2178 = None
        KL_LOC_V2548_2179 = None
        KL_LOC_Action_2180 = None
        KL_LOC_V2549_2181 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2153', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2153, [setattr(KL_CTX, 'KL_LOC_Case_2154', [setattr(KL_CTX, 'KL_LOC_V2530_2155', tco_apply(shen_lazyderef, [KL_ARG_V2982_2148, KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2531_2156', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2530_2155[0], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2532_2157', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2530_2155[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_P_2158', KL_CTX.KL_LOC_V2532_2157[0]), [setattr(KL_CTX, 'KL_LOC_V2533_2159', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2532_2157[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_Action_2160', KL_CTX.KL_LOC_V2533_2159[0]), [setattr(KL_CTX, 'KL_LOC_V2534_2161', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2533_2159[1], KL_ARG_V2985_2151])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_P_2158, [symdic.symdic_kl_x58, [symdic.symdic_kl_boolean, []]]], KL_ARG_V2984_2150, KL_ARG_V2985_2151, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42x45action, [KL_CTX.KL_LOC_Action_2160, KL_ARG_V2983_2149, [[KL_CTX.KL_LOC_P_2158, [symdic.symdic_kl_x58, [symdic.symdic_kl_verified, []]]], KL_ARG_V2984_2150], KL_ARG_V2985_2151, KL_ARG_V2986_2152]))]))]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2534_2161) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2533_2159) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2532_2157) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2531_2156) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2530_2155) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2162', [setattr(KL_CTX, 'KL_LOC_V2535_2163', tco_apply(shen_lazyderef, [KL_ARG_V2982_2148, KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2536_2164', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2535_2163[0], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2537_2165', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2535_2163[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2538_2166', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2537_2165[0], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2539_2167', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2538_2166[0], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2540_2168', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2539_2167[0], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2541_2169', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2539_2167[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_F_2170', KL_CTX.KL_LOC_V2541_2169[0]), [setattr(KL_CTX, 'KL_LOC_V2542_2171', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2541_2169[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2543_2172', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2538_2166[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_Action_2173', KL_CTX.KL_LOC_V2543_2172[0]), [setattr(KL_CTX, 'KL_LOC_V2544_2174', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2543_2172[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2545_2175', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2537_2165[1], KL_ARG_V2985_2151])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42x45action, [[symdic.symdic_kl_where, [[symdic.symdic_kl_not, [[KL_CTX.KL_LOC_F_2170, [KL_CTX.KL_LOC_Action_2173, []]], []]], [KL_CTX.KL_LOC_Action_2173, []]]], KL_ARG_V2983_2149, KL_ARG_V2984_2150, KL_ARG_V2985_2151, KL_ARG_V2986_2152]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2545_2175) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2544_2174) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2543_2172) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2542_2171) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2541_2169) else False)][(-1)] if shen_eq(symdic.symdic_kl_failx45if, KL_CTX.KL_LOC_V2540_2168) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2539_2167) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2538_2166) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2537_2165) else False)][(-1)] if shen_eq(symdic.symdic_shen_choicepointx33, KL_CTX.KL_LOC_V2536_2164) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2535_2163) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2176', [setattr(KL_CTX, 'KL_LOC_V2546_2177', tco_apply(shen_lazyderef, [KL_ARG_V2982_2148, KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2547_2178', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2546_2177[0], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_V2548_2179', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2546_2177[1], KL_ARG_V2985_2151])), ([setattr(KL_CTX, 'KL_LOC_Action_2180', KL_CTX.KL_LOC_V2548_2179[0]), [setattr(KL_CTX, 'KL_LOC_V2549_2181', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2548_2179[1], KL_ARG_V2985_2151])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2153, KL_ARG_V2985_2151, (lambda : tail_call(shen_tx42x45action, [[symdic.symdic_kl_where, [[symdic.symdic_kl_not, [[[symdic.symdic_kl_x61, [KL_CTX.KL_LOC_Action_2180, []]], [[symdic.symdic_kl_fail, []], []]], []]], [KL_CTX.KL_LOC_Action_2180, []]]], KL_ARG_V2983_2149, KL_ARG_V2984_2150, KL_ARG_V2985_2151, KL_ARG_V2986_2152]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2549_2181) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2548_2179) else False)][(-1)] if shen_eq(symdic.symdic_shen_choicepointx33, KL_CTX.KL_LOC_V2547_2178) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2546_2177) else False)][(-1)]), ([tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [[KL_ARG_V2982_2148, [symdic.symdic_kl_x58, [KL_ARG_V2983_2149, []]]], KL_ARG_V2984_2150, KL_ARG_V2985_2151, KL_ARG_V2986_2152])][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2176, False) else KL_CTX.KL_LOC_Case_2176)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2162, False) else KL_CTX.KL_LOC_Case_2162)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2154, False) else KL_CTX.KL_LOC_Case_2154)][(-1)]])][(-1)]
shen_add_fun('shen.t*-action', shen_tx42x45action)

@tail_recursion
def shen_tx42x45pattern(KL_ARG_V2987_2182, KL_ARG_V2988_2183, KL_ARG_V2989_2184, KL_ARG_V2990_2185):

    class KL_Context:
        KL_LOC_Throwcontrol_2186 = None
        KL_LOC_Hyp_2187 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2186', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2186, [setattr(KL_CTX, 'KL_LOC_Hyp_2187', tco_apply(shen_newpv, [KL_ARG_V2989_2184])), [tco_apply(shen_incinfs, []), tco_apply(shen_tmsx45x62hyp, [tco_apply(shen_ues, [KL_ARG_V2987_2182]), KL_CTX.KL_LOC_Hyp_2187, KL_ARG_V2989_2184, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2186, KL_ARG_V2989_2184, (lambda : tail_call(shen_tx42, [[KL_ARG_V2987_2182, [symdic.symdic_kl_x58, [KL_ARG_V2988_2183, []]]], KL_CTX.KL_LOC_Hyp_2187, KL_ARG_V2989_2184, KL_ARG_V2990_2185]))]))])][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.t*-pattern', shen_tx42x45pattern)

@tail_recursion
def shen_tmsx45x62hyp(KL_ARG_V2991_2188, KL_ARG_V2992_2189, KL_ARG_V2993_2190, KL_ARG_V2994_2191):

    class KL_Context:
        KL_LOC_Case_2192 = None
        KL_LOC_V2514_2193 = None
        KL_LOC_V2515_2194 = None
        KL_LOC_Result_2195 = None
        KL_LOC_V2516_2196 = None
        KL_LOC_Tm2511_2197 = None
        KL_LOC_Tms_2198 = None
        KL_LOC_V2517_2199 = None
        KL_LOC_V2518_2200 = None
        KL_LOC_Tm_2201 = None
        KL_LOC_V2519_2202 = None
        KL_LOC_V2520_2203 = None
        KL_LOC_V2521_2204 = None
        KL_LOC_A_2205 = None
        KL_LOC_V2522_2206 = None
        KL_LOC_Hyp_2207 = None
        KL_LOC_Result_2208 = None
        KL_LOC_Hyp_2209 = None
        KL_LOC_A_2210 = None
        KL_LOC_Result_2211 = None
        KL_LOC_Hyp_2212 = None
        KL_LOC_Result_2213 = None
        KL_LOC_V2523_2214 = None
        KL_LOC_A_2215 = None
        KL_LOC_V2524_2216 = None
        KL_LOC_Hyp_2217 = None
        KL_LOC_Result_2218 = None
        KL_LOC_Hyp_2219 = None
        KL_LOC_A_2220 = None
        KL_LOC_Result_2221 = None
        KL_LOC_Hyp_2222 = None
        KL_LOC_A_2223 = None
        KL_LOC_Result_2224 = None
        KL_LOC_Hyp_2225 = None
        KL_LOC_Tm_2226 = None
        KL_LOC_A_2227 = None
        KL_LOC_Result_2228 = None
        KL_LOC_Hyp_2229 = None
        KL_LOC_Tm_2230 = None
        KL_LOC_A_2231 = None
        KL_LOC_Hyp_2232 = None
        KL_LOC_Result_2233 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2192', [setattr(KL_CTX, 'KL_LOC_V2514_2193', tco_apply(shen_lazyderef, [KL_ARG_V2991_2188, KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2515_2194', tco_apply(shen_lazyderef, [KL_ARG_V2992_2189, KL_ARG_V2993_2190])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2994_2191])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2515_2194) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2515_2194, [], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2195', [tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V2994_2191])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2515_2194, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2195][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2515_2194]) else False))][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2514_2193) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2516_2196', tco_apply(shen_lazyderef, [KL_ARG_V2991_2188, KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Tm2511_2197', KL_CTX.KL_LOC_V2516_2196[0]), [setattr(KL_CTX, 'KL_LOC_Tms_2198', KL_CTX.KL_LOC_V2516_2196[1]), [setattr(KL_CTX, 'KL_LOC_V2517_2199', tco_apply(shen_lazyderef, [KL_ARG_V2992_2189, KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2518_2200', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2517_2199[0], KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Tm_2201', KL_CTX.KL_LOC_V2518_2200[0]), [setattr(KL_CTX, 'KL_LOC_V2519_2202', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2518_2200[1], KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2520_2203', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2519_2202[0], KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_V2521_2204', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2519_2202[1], KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_A_2205', KL_CTX.KL_LOC_V2521_2204[0]), [setattr(KL_CTX, 'KL_LOC_V2522_2206', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2521_2204[1], KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2207', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tail_call(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2207, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2522_2206) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2522_2206, [], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2208', [setattr(KL_CTX, 'KL_LOC_Hyp_2209', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2209, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2522_2206, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2208][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2522_2206]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2521_2204) else ([setattr(KL_CTX, 'KL_LOC_A_2210', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2521_2204, [KL_CTX.KL_LOC_A_2210, []], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2211', [setattr(KL_CTX, 'KL_LOC_Hyp_2212', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2212, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2521_2204, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2211][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2521_2204]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2520_2203) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2520_2203, symdic.symdic_kl_x58, KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2213', [setattr(KL_CTX, 'KL_LOC_V2523_2214', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2519_2202[1], KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_A_2215', KL_CTX.KL_LOC_V2523_2214[0]), [setattr(KL_CTX, 'KL_LOC_V2524_2216', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2523_2214[1], KL_ARG_V2993_2190])), ([setattr(KL_CTX, 'KL_LOC_Hyp_2217', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2217, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2524_2216) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2524_2216, [], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2218', [setattr(KL_CTX, 'KL_LOC_Hyp_2219', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2219, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2524_2216, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2218][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2524_2216]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2523_2214) else ([setattr(KL_CTX, 'KL_LOC_A_2220', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2523_2214, [KL_CTX.KL_LOC_A_2220, []], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2221', [setattr(KL_CTX, 'KL_LOC_Hyp_2222', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2222, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2523_2214, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2221][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2523_2214]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2520_2203, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2213][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2520_2203]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2519_2202) else ([setattr(KL_CTX, 'KL_LOC_A_2223', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2519_2202, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2223, []]], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2224', [setattr(KL_CTX, 'KL_LOC_Hyp_2225', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2201, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2225, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2519_2202, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2224][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2519_2202]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2518_2200) else ([setattr(KL_CTX, 'KL_LOC_Tm_2226', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [setattr(KL_CTX, 'KL_LOC_A_2227', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2518_2200, [KL_CTX.KL_LOC_Tm_2226, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2227, []]]], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2228', [setattr(KL_CTX, 'KL_LOC_Hyp_2229', KL_CTX.KL_LOC_V2517_2199[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2226, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2229, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2518_2200, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2228][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2518_2200]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2517_2199) else ([setattr(KL_CTX, 'KL_LOC_Tm_2230', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [setattr(KL_CTX, 'KL_LOC_A_2231', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [setattr(KL_CTX, 'KL_LOC_Hyp_2232', tco_apply(shen_newpv, [KL_ARG_V2993_2190])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2517_2199, [[KL_CTX.KL_LOC_Tm_2230, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A_2231, []]]], KL_CTX.KL_LOC_Hyp_2232], KL_ARG_V2993_2190]), [setattr(KL_CTX, 'KL_LOC_Result_2233', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_Tm_2230, KL_CTX.KL_LOC_Tm2511_2197, KL_ARG_V2993_2190, (lambda : tail_call(shen_tmsx45x62hyp, [KL_CTX.KL_LOC_Tms_2198, KL_CTX.KL_LOC_Hyp_2232, KL_ARG_V2993_2190, KL_ARG_V2994_2191]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2517_2199, KL_ARG_V2993_2190]), KL_CTX.KL_LOC_Result_2233][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2517_2199]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2516_2196) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2192, False) else KL_CTX.KL_LOC_Case_2192)][(-1)]
shen_add_fun('shen.tms->hyp', shen_tmsx45x62hyp)

@tail_recursion
def kl_findall(KL_ARG_V2995_2234, KL_ARG_V2996_2235, KL_ARG_V2997_2236, KL_ARG_V2998_2237, KL_ARG_V2999_2238):

    class KL_Context:
        KL_LOC_B_2239 = None
        KL_LOC_A_2240 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2239', tco_apply(shen_newpv, [KL_ARG_V2998_2237])), [setattr(KL_CTX, 'KL_LOC_A_2240', tco_apply(shen_newpv, [KL_ARG_V2998_2237])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_A_2240, tco_apply(kl_gensym, [symdic.symdic_shen_a]), KL_ARG_V2998_2237, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_B_2239, shen_set(tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2240, KL_ARG_V2998_2237]), []), KL_ARG_V2998_2237, (lambda : tail_call(shen_findallhelp, [KL_ARG_V2995_2234, KL_ARG_V2996_2235, KL_ARG_V2997_2236, KL_CTX.KL_LOC_A_2240, KL_ARG_V2998_2237, KL_ARG_V2999_2238]))]))])][(-1)]][(-1)]][(-1)]
shen_add_fun('findall', kl_findall)

@tail_recursion
def shen_findallhelp(KL_ARG_V3000_2241, KL_ARG_V3001_2242, KL_ARG_V3002_2243, KL_ARG_V3003_2244, KL_ARG_V3004_2245, KL_ARG_V3005_2246):

    class KL_Context:
        KL_LOC_Case_2247 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2247', [tco_apply(shen_incinfs, []), tco_apply(kl_call, [KL_ARG_V3001_2242, KL_ARG_V3004_2245, (lambda : tail_call(shen_remember, [KL_ARG_V3003_2244, KL_ARG_V3000_2241, KL_ARG_V3004_2245, (lambda : tail_call(kl_fwhen, [False, KL_ARG_V3004_2245, KL_ARG_V3005_2246]))]))])][(-1)]), ([tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_ARG_V3002_2243, shen_get(tco_apply(shen_lazyderef, [KL_ARG_V3003_2244, KL_ARG_V3004_2245])), KL_ARG_V3004_2245, KL_ARG_V3005_2246])][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2247, False) else KL_CTX.KL_LOC_Case_2247)][(-1)]
shen_add_fun('shen.findallhelp', shen_findallhelp)

@tail_recursion
def shen_remember(KL_ARG_V3006_2248, KL_ARG_V3007_2249, KL_ARG_V3008_2250, KL_ARG_V3009_2251):

    class KL_Context:
        KL_LOC_B_2252 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_B_2252', tco_apply(shen_newpv, [KL_ARG_V3008_2250])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_B_2252, shen_set(tco_apply(shen_deref, [KL_ARG_V3006_2248, KL_ARG_V3008_2250]), [tco_apply(shen_deref, [KL_ARG_V3007_2249, KL_ARG_V3008_2250]), shen_get(tco_apply(shen_deref, [KL_ARG_V3006_2248, KL_ARG_V3008_2250]))]), KL_ARG_V3008_2250, KL_ARG_V3009_2251])][(-1)]][(-1)]
shen_add_fun('shen.remember', shen_remember)

@tail_recursion
def shen_tx42x45defcc(KL_ARG_V3010_2253, KL_ARG_V3011_2254, KL_ARG_V3012_2255, KL_ARG_V3013_2256, KL_ARG_V3014_2257):

    class KL_Context:
        KL_LOC_Throwcontrol_2258 = None
        KL_LOC_V2487_2259 = None
        KL_LOC_V2488_2260 = None
        KL_LOC_V2489_2261 = None
        KL_LOC_F_2262 = None
        KL_LOC_V2490_2263 = None
        KL_LOC_V2491_2264 = None
        KL_LOC_V2492_2265 = None
        KL_LOC_V2493_2266 = None
        KL_LOC_V2494_2267 = None
        KL_LOC_V2495_2268 = None
        KL_LOC_A_2269 = None
        KL_LOC_V2496_2270 = None
        KL_LOC_V2497_2271 = None
        KL_LOC_V2498_2272 = None
        KL_LOC_V2499_2273 = None
        KL_LOC_B_2274 = None
        KL_LOC_V2500_2275 = None
        KL_LOC_V2501_2276 = None
        KL_LOC_Rest_2277 = None
        KL_LOC_Restx38_2278 = None
        KL_LOC_Restx38x38_2279 = None
        KL_LOC_Rules_2280 = None
        KL_LOC_ListAx38x38_2281 = None
        KL_LOC_Bx38x38_2282 = None
        KL_LOC_Sig_2283 = None
        KL_LOC_Declare_2284 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2258', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2258, [setattr(KL_CTX, 'KL_LOC_V2487_2259', tco_apply(shen_lazyderef, [KL_ARG_V3010_2253, KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2488_2260', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2487_2259[0], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2489_2261', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2487_2259[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_F_2262', KL_CTX.KL_LOC_V2489_2261[0]), [setattr(KL_CTX, 'KL_LOC_V2490_2263', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2489_2261[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2491_2264', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2490_2263[0], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2492_2265', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2490_2263[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2493_2266', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2492_2265[0], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2494_2267', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2493_2266[0], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2495_2268', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2493_2266[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_A_2269', KL_CTX.KL_LOC_V2495_2268[0]), [setattr(KL_CTX, 'KL_LOC_V2496_2270', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2495_2268[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2497_2271', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2492_2265[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2498_2272', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2497_2271[0], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2499_2273', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2497_2271[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_B_2274', KL_CTX.KL_LOC_V2499_2273[0]), [setattr(KL_CTX, 'KL_LOC_V2500_2275', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2499_2273[1], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_V2501_2276', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2500_2275[0], KL_ARG_V3013_2256])), ([setattr(KL_CTX, 'KL_LOC_Rest_2277', KL_CTX.KL_LOC_V2500_2275[1]), [setattr(KL_CTX, 'KL_LOC_Restx38_2278', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Restx38x38_2279', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Rules_2280', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_ListAx38x38_2281', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Bx38x38_2282', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Sig_2283', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [setattr(KL_CTX, 'KL_LOC_Declare_2284', tco_apply(shen_newpv, [KL_ARG_V3013_2256])), [tco_apply(shen_incinfs, []), tco_apply(kl_bind, [KL_CTX.KL_LOC_Sig_2283, tco_apply(shen_ue, [[[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2269, KL_ARG_V3013_2256]), []]], [symdic.symdic_kl_x61x61x62, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2274, KL_ARG_V3013_2256]), []]]]]), KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_ListAx38x38_2281, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2283, KL_ARG_V3013_2256])[0], KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Bx38x38_2282, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Sig_2283, KL_ARG_V3013_2256])[1][1][0], KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38_2278, tco_apply(shen_plugx45wildcards, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Rest_2277, KL_ARG_V3013_2256])]), KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Restx38x38_2279, tco_apply(shen_ue, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Restx38_2278, KL_ARG_V3013_2256])]), KL_ARG_V3013_2256, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2280, KL_CTX.KL_LOC_Restx38x38_2279, KL_ARG_V3013_2256, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2258, KL_ARG_V3013_2256, (lambda : tail_call(shen_tcx45rules, [KL_CTX.KL_LOC_F_2262, KL_CTX.KL_LOC_Rules_2280, KL_CTX.KL_LOC_ListAx38x38_2281, KL_CTX.KL_LOC_Bx38x38_2282, [[KL_CTX.KL_LOC_F_2262, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_Sig_2283, []]]], KL_ARG_V3012_2255], 1, KL_ARG_V3013_2256, (lambda : tail_call(kl_unify, [KL_ARG_V3011_2254, [[symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2269, []]], [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_B_2274, []]]], KL_ARG_V3013_2256, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Declare_2284, apply(kl_declare, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_F_2262, KL_ARG_V3013_2256]), [[symdic.symdic_kl_list, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_A_2269, KL_ARG_V3013_2256]), []]], [symdic.symdic_kl_x61x61x62, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_B_2274, KL_ARG_V3013_2256]), []]]]]), KL_ARG_V3013_2256, KL_ARG_V3014_2257]))]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_eq(symdic.symdic_kl_x125, KL_CTX.KL_LOC_V2501_2276) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2500_2275) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2499_2273) else False)][(-1)] if shen_eq(symdic.symdic_kl_x61x61x62, KL_CTX.KL_LOC_V2498_2272) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2497_2271) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2496_2270) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2495_2268) else False)][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2494_2267) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2493_2266) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2492_2265) else False)][(-1)] if shen_eq(symdic.symdic_kl_x123, KL_CTX.KL_LOC_V2491_2264) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2490_2263) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2489_2261) else False)][(-1)] if shen_eq(symdic.symdic_kl_defcc, KL_CTX.KL_LOC_V2488_2260) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2487_2259) else False)][(-1)]])][(-1)]
shen_add_fun('shen.t*-defcc', shen_tx42x45defcc)

@tail_recursion
def shen_plugx45wildcards(KL_ARG_V3015_2285):
    global symdic
    return (tail_call(kl_map, [symdic.symdic_shen_plugx45wildcards, KL_ARG_V3015_2285]) if shen_consp(KL_ARG_V3015_2285) else (tail_call(kl_gensym, [shen_intern('X')]) if shen_eq(KL_ARG_V3015_2285, symdic.symdic_kl__) else (KL_ARG_V3015_2285 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.plug-wildcards', shen_plugx45wildcards)

@tail_recursion
def shen_getx45rules(KL_ARG_V3016_2286, KL_ARG_V3017_2287, KL_ARG_V3018_2288, KL_ARG_V3019_2289):

    class KL_Context:
        KL_LOC_Throwcontrol_2290 = None
        KL_LOC_Case_2291 = None
        KL_LOC_V2480_2292 = None
        KL_LOC_V2481_2293 = None
        KL_LOC_Result_2294 = None
        KL_LOC_V2482_2295 = None
        KL_LOC_V2483_2296 = None
        KL_LOC_Rule_2297 = None
        KL_LOC_Rules_2298 = None
        KL_LOC_Other_2299 = None
        KL_LOC_Rule_2300 = None
        KL_LOC_Rules_2301 = None
        KL_LOC_Result_2302 = None
        KL_LOC_Other_2303 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2290', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2290, [setattr(KL_CTX, 'KL_LOC_Case_2291', [setattr(KL_CTX, 'KL_LOC_V2480_2292', tco_apply(shen_lazyderef, [KL_ARG_V3016_2286, KL_ARG_V3018_2288])), ([setattr(KL_CTX, 'KL_LOC_V2481_2293', tco_apply(shen_lazyderef, [KL_ARG_V3017_2287, KL_ARG_V3018_2288])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, KL_ARG_V3019_2289])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2481_2293) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2480_2292) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2480_2292, [], KL_ARG_V3018_2288]), [setattr(KL_CTX, 'KL_LOC_Result_2294', [setattr(KL_CTX, 'KL_LOC_V2482_2295', tco_apply(shen_lazyderef, [KL_ARG_V3017_2287, KL_ARG_V3018_2288])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, KL_ARG_V3019_2289])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2482_2295) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2480_2292, KL_ARG_V3018_2288]), KL_CTX.KL_LOC_Result_2294][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2480_2292]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2483_2296', tco_apply(shen_lazyderef, [KL_ARG_V3016_2286, KL_ARG_V3018_2288])), ([setattr(KL_CTX, 'KL_LOC_Rule_2297', KL_CTX.KL_LOC_V2483_2296[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2298', KL_CTX.KL_LOC_V2483_2296[1]), [setattr(KL_CTX, 'KL_LOC_Other_2299', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V3017_2287, KL_CTX.KL_LOC_Rule_2297, KL_CTX.KL_LOC_Other_2299, KL_ARG_V3018_2288, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2298, KL_CTX.KL_LOC_Other_2299, KL_ARG_V3018_2288, KL_ARG_V3019_2289]))]))])][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2483_2296) else ([setattr(KL_CTX, 'KL_LOC_Rule_2300', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [setattr(KL_CTX, 'KL_LOC_Rules_2301', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2483_2296, [KL_CTX.KL_LOC_Rule_2300, KL_CTX.KL_LOC_Rules_2301], KL_ARG_V3018_2288]), [setattr(KL_CTX, 'KL_LOC_Result_2302', [setattr(KL_CTX, 'KL_LOC_Other_2303', tco_apply(shen_newpv, [KL_ARG_V3018_2288])), [tco_apply(shen_incinfs, []), tco_apply(shen_firstx45rule, [KL_ARG_V3017_2287, KL_CTX.KL_LOC_Rule_2300, KL_CTX.KL_LOC_Other_2303, KL_ARG_V3018_2288, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2290, KL_ARG_V3018_2288, (lambda : tail_call(shen_getx45rules, [KL_CTX.KL_LOC_Rules_2301, KL_CTX.KL_LOC_Other_2303, KL_ARG_V3018_2288, KL_ARG_V3019_2289]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2483_2296, KL_ARG_V3018_2288]), KL_CTX.KL_LOC_Result_2302][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2483_2296]) else False))][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2291, False) else KL_CTX.KL_LOC_Case_2291)][(-1)]])][(-1)]
shen_add_fun('shen.get-rules', shen_getx45rules)

@tail_recursion
def shen_firstx45rule(KL_ARG_V3020_2304, KL_ARG_V3021_2305, KL_ARG_V3022_2306, KL_ARG_V3023_2307, KL_ARG_V3024_2308):

    class KL_Context:
        KL_LOC_Throwcontrol_2309 = None
        KL_LOC_Case_2310 = None
        KL_LOC_V2473_2311 = None
        KL_LOC_V2474_2312 = None
        KL_LOC_Other2468_2313 = None
        KL_LOC_V2475_2314 = None
        KL_LOC_Result_2315 = None
        KL_LOC_V2476_2316 = None
        KL_LOC_X2469_2317 = None
        KL_LOC_Rest_2318 = None
        KL_LOC_V2477_2319 = None
        KL_LOC_X_2320 = None
        KL_LOC_Rule_2321 = None
        KL_LOC_X_2322 = None
        KL_LOC_Rule_2323 = None
        KL_LOC_Result_2324 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2309', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2309, [setattr(KL_CTX, 'KL_LOC_Case_2310', [setattr(KL_CTX, 'KL_LOC_V2473_2311', tco_apply(shen_lazyderef, [KL_ARG_V3020_2304, KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_V2474_2312', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2473_2311[0], KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_Other2468_2313', KL_CTX.KL_LOC_V2473_2311[1]), [setattr(KL_CTX, 'KL_LOC_V2475_2314', tco_apply(shen_lazyderef, [KL_ARG_V3021_2305, KL_ARG_V3023_2307])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3022_2306, KL_CTX.KL_LOC_Other2468_2313, KL_ARG_V3023_2307, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2309, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2475_2314) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2475_2314, [], KL_ARG_V3023_2307]), [setattr(KL_CTX, 'KL_LOC_Result_2315', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3022_2306, KL_CTX.KL_LOC_Other2468_2313, KL_ARG_V3023_2307, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2309, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2475_2314, KL_ARG_V3023_2307]), KL_CTX.KL_LOC_Result_2315][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2475_2314]) else False))][(-1)]][(-1)] if shen_eq(symdic.symdic_kl_x59, KL_CTX.KL_LOC_V2474_2312) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2473_2311) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2476_2316', tco_apply(shen_lazyderef, [KL_ARG_V3020_2304, KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_X2469_2317', KL_CTX.KL_LOC_V2476_2316[0]), [setattr(KL_CTX, 'KL_LOC_Rest_2318', KL_CTX.KL_LOC_V2476_2316[1]), [setattr(KL_CTX, 'KL_LOC_V2477_2319', tco_apply(shen_lazyderef, [KL_ARG_V3021_2305, KL_ARG_V3023_2307])), ([setattr(KL_CTX, 'KL_LOC_X_2320', KL_CTX.KL_LOC_V2477_2319[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2321', KL_CTX.KL_LOC_V2477_2319[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2320, KL_CTX.KL_LOC_X2469_2317, KL_ARG_V3023_2307, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2318, KL_CTX.KL_LOC_Rule_2321, KL_ARG_V3022_2306, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2477_2319) else ([setattr(KL_CTX, 'KL_LOC_X_2322', tco_apply(shen_newpv, [KL_ARG_V3023_2307])), [setattr(KL_CTX, 'KL_LOC_Rule_2323', tco_apply(shen_newpv, [KL_ARG_V3023_2307])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2477_2319, [KL_CTX.KL_LOC_X_2322, KL_CTX.KL_LOC_Rule_2323], KL_ARG_V3023_2307]), [setattr(KL_CTX, 'KL_LOC_Result_2324', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2322, KL_CTX.KL_LOC_X2469_2317, KL_ARG_V3023_2307, (lambda : tail_call(shen_firstx45rule, [KL_CTX.KL_LOC_Rest_2318, KL_CTX.KL_LOC_Rule_2323, KL_ARG_V3022_2306, KL_ARG_V3023_2307, KL_ARG_V3024_2308]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2477_2319, KL_ARG_V3023_2307]), KL_CTX.KL_LOC_Result_2324][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2477_2319]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2476_2316) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2310, False) else KL_CTX.KL_LOC_Case_2310)][(-1)]])][(-1)]
shen_add_fun('shen.first-rule', shen_firstx45rule)

@tail_recursion
def shen_tcx45rules(KL_ARG_V3025_2325, KL_ARG_V3026_2326, KL_ARG_V3027_2327, KL_ARG_V3028_2328, KL_ARG_V3029_2329, KL_ARG_V3030_2330, KL_ARG_V3031_2331, KL_ARG_V3032_2332):

    class KL_Context:
        KL_LOC_Throwcontrol_2333 = None
        KL_LOC_Case_2334 = None
        KL_LOC_V2462_2335 = None
        KL_LOC_V2463_2336 = None
        KL_LOC_Rule_2337 = None
        KL_LOC_Rules_2338 = None
        KL_LOC_V2464_2339 = None
        KL_LOC_V2465_2340 = None
        KL_LOC_V2466_2341 = None
        KL_LOC_A_2342 = None
        KL_LOC_V2467_2343 = None
        KL_LOC_M_2344 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2333', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2333, [setattr(KL_CTX, 'KL_LOC_Case_2334', [setattr(KL_CTX, 'KL_LOC_V2462_2335', tco_apply(shen_lazyderef, [KL_ARG_V3026_2326, KL_ARG_V3031_2331])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V3032_2332])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2462_2335) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2463_2336', tco_apply(shen_lazyderef, [KL_ARG_V3026_2326, KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_Rule_2337', KL_CTX.KL_LOC_V2463_2336[0]), [setattr(KL_CTX, 'KL_LOC_Rules_2338', KL_CTX.KL_LOC_V2463_2336[1]), [setattr(KL_CTX, 'KL_LOC_V2464_2339', tco_apply(shen_lazyderef, [KL_ARG_V3027_2327, KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_V2465_2340', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2464_2339[0], KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_V2466_2341', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2464_2339[1], KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_A_2342', KL_CTX.KL_LOC_V2466_2341[0]), [setattr(KL_CTX, 'KL_LOC_V2467_2343', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2466_2341[1], KL_ARG_V3031_2331])), ([setattr(KL_CTX, 'KL_LOC_M_2344', tco_apply(shen_newpv, [KL_ARG_V3031_2331])), [tco_apply(shen_incinfs, []), tco_apply(shen_tcx45rule, [KL_ARG_V3025_2325, KL_CTX.KL_LOC_Rule_2337, KL_CTX.KL_LOC_A_2342, KL_ARG_V3028_2328, KL_ARG_V3029_2329, KL_ARG_V3030_2330, KL_ARG_V3031_2331, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_M_2344, (tco_apply(shen_deref, [KL_ARG_V3030_2330, KL_ARG_V3031_2331]) + 1), KL_ARG_V3031_2331, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2333, KL_ARG_V3031_2331, (lambda : tail_call(shen_tcx45rules, [KL_ARG_V3025_2325, KL_CTX.KL_LOC_Rules_2338, [symdic.symdic_kl_list, [KL_CTX.KL_LOC_A_2342, []]], KL_ARG_V3028_2328, KL_ARG_V3029_2329, KL_CTX.KL_LOC_M_2344, KL_ARG_V3031_2331, KL_ARG_V3032_2332]))]))]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2467_2343) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2466_2341) else False)][(-1)] if shen_eq(symdic.symdic_kl_list, KL_CTX.KL_LOC_V2465_2340) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2464_2339) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2463_2336) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2334, False) else KL_CTX.KL_LOC_Case_2334)][(-1)]])][(-1)]
shen_add_fun('shen.tc-rules', shen_tcx45rules)

@tail_recursion
def shen_tcx45rule(KL_ARG_V3033_2345, KL_ARG_V3034_2346, KL_ARG_V3035_2347, KL_ARG_V3036_2348, KL_ARG_V3037_2349, KL_ARG_V3038_2350, KL_ARG_V3039_2351, KL_ARG_V3040_2352):

    class KL_Context:
        KL_LOC_Case_2353 = None
        KL_LOC_Err_2354 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Case_2353', [tco_apply(shen_incinfs, []), tco_apply(shen_checkx45defccx45rule, [KL_ARG_V3034_2346, KL_ARG_V3035_2347, KL_ARG_V3036_2348, KL_ARG_V3037_2349, KL_ARG_V3039_2351, KL_ARG_V3040_2352])][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Err_2354', tco_apply(shen_newpv, [KL_ARG_V3039_2351])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Err_2354, shen_simple_error(('type error in rule ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V3038_2350, KL_ARG_V3039_2351]), (' of ' + tco_apply(shen_app, [tco_apply(shen_lazyderef, [KL_ARG_V3033_2345, KL_ARG_V3039_2351]), '', symdic.symdic_shen_a])), symdic.symdic_shen_a]))), KL_ARG_V3039_2351, KL_ARG_V3040_2352])][(-1)]][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2353, False) else KL_CTX.KL_LOC_Case_2353)][(-1)]
shen_add_fun('shen.tc-rule', shen_tcx45rule)

@tail_recursion
def shen_checkx45defccx45rule(KL_ARG_V3041_2355, KL_ARG_V3042_2356, KL_ARG_V3043_2357, KL_ARG_V3044_2358, KL_ARG_V3045_2359, KL_ARG_V3046_2360):

    class KL_Context:
        KL_LOC_Throwcontrol_2361 = None
        KL_LOC_Syntax_2362 = None
        KL_LOC_Semantics_2363 = None
        KL_LOC_SynHyps_2364 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2361', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2361, [setattr(KL_CTX, 'KL_LOC_Syntax_2362', tco_apply(shen_newpv, [KL_ARG_V3045_2359])), [setattr(KL_CTX, 'KL_LOC_Semantics_2363', tco_apply(shen_newpv, [KL_ARG_V3045_2359])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2364', tco_apply(shen_newpv, [KL_ARG_V3045_2359])), [tco_apply(shen_incinfs, []), tco_apply(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2362, KL_CTX.KL_LOC_Semantics_2363, KL_ARG_V3041_2355, KL_ARG_V3045_2359, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2361, KL_ARG_V3045_2359, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Syntax_2362, KL_ARG_V3044_2358, KL_CTX.KL_LOC_SynHyps_2364, KL_ARG_V3042_2356, KL_ARG_V3045_2359, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2361, KL_ARG_V3045_2359, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2362, KL_ARG_V3042_2356, KL_CTX.KL_LOC_SynHyps_2364, KL_ARG_V3045_2359, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2361, KL_ARG_V3045_2359, (lambda : tail_call(shen_semanticsx45check, [KL_CTX.KL_LOC_Semantics_2363, KL_ARG_V3043_2357, KL_CTX.KL_LOC_SynHyps_2364, KL_ARG_V3045_2359, KL_ARG_V3046_2360]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]])][(-1)]
shen_add_fun('shen.check-defcc-rule', shen_checkx45defccx45rule)

@tail_recursion
def shen_syntaxx45hyps(KL_ARG_V3047_2365, KL_ARG_V3048_2366, KL_ARG_V3049_2367, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370):

    class KL_Context:
        KL_LOC_Throwcontrol_2371 = None
        KL_LOC_Case_2372 = None
        KL_LOC_V2435_2373 = None
        KL_LOC_Case_2374 = None
        KL_LOC_V2436_2375 = None
        KL_LOC_X2429_2376 = None
        KL_LOC_Y_2377 = None
        KL_LOC_V2437_2378 = None
        KL_LOC_V2438_2379 = None
        KL_LOC_X_2380 = None
        KL_LOC_V2439_2381 = None
        KL_LOC_V2440_2382 = None
        KL_LOC_V2441_2383 = None
        KL_LOC_A2430_2384 = None
        KL_LOC_V2442_2385 = None
        KL_LOC_SynHyps_2386 = None
        KL_LOC_Result_2387 = None
        KL_LOC_SynHyps_2388 = None
        KL_LOC_A2430_2389 = None
        KL_LOC_Result_2390 = None
        KL_LOC_SynHyps_2391 = None
        KL_LOC_Result_2392 = None
        KL_LOC_V2443_2393 = None
        KL_LOC_A2430_2394 = None
        KL_LOC_V2444_2395 = None
        KL_LOC_SynHyps_2396 = None
        KL_LOC_Result_2397 = None
        KL_LOC_SynHyps_2398 = None
        KL_LOC_A2430_2399 = None
        KL_LOC_Result_2400 = None
        KL_LOC_SynHyps_2401 = None
        KL_LOC_A2430_2402 = None
        KL_LOC_Result_2403 = None
        KL_LOC_SynHyps_2404 = None
        KL_LOC_X_2405 = None
        KL_LOC_A2430_2406 = None
        KL_LOC_Result_2407 = None
        KL_LOC_SynHyps_2408 = None
        KL_LOC_X_2409 = None
        KL_LOC_A2430_2410 = None
        KL_LOC_SynHyps_2411 = None
        KL_LOC_Result_2412 = None
        KL_LOC_V2445_2413 = None
        KL_LOC_Y_2414 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2371', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2371, [setattr(KL_CTX, 'KL_LOC_Case_2372', [setattr(KL_CTX, 'KL_LOC_V2435_2373', tco_apply(shen_lazyderef, [KL_ARG_V3047_2365, KL_ARG_V3051_2369])), ([tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3049_2367, KL_ARG_V3048_2366, KL_ARG_V3051_2369, KL_ARG_V3052_2370])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2435_2373) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2374', [setattr(KL_CTX, 'KL_LOC_V2436_2375', tco_apply(shen_lazyderef, [KL_ARG_V3047_2365, KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_X2429_2376', KL_CTX.KL_LOC_V2436_2375[0]), [setattr(KL_CTX, 'KL_LOC_Y_2377', KL_CTX.KL_LOC_V2436_2375[1]), [setattr(KL_CTX, 'KL_LOC_V2437_2378', tco_apply(shen_lazyderef, [KL_ARG_V3049_2367, KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_V2438_2379', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2437_2378[0], KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_X_2380', KL_CTX.KL_LOC_V2438_2379[0]), [setattr(KL_CTX, 'KL_LOC_V2439_2381', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2438_2379[1], KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_V2440_2382', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2439_2381[0], KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_V2441_2383', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2439_2381[1], KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_A2430_2384', KL_CTX.KL_LOC_V2441_2383[0]), [setattr(KL_CTX, 'KL_LOC_V2442_2385', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2441_2383[1], KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2386', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2384, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2386, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2442_2385) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2442_2385, [], KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2387', [setattr(KL_CTX, 'KL_LOC_SynHyps_2388', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2384, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2388, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2442_2385, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2387][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2442_2385]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2441_2383) else ([setattr(KL_CTX, 'KL_LOC_A2430_2389', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2441_2383, [KL_CTX.KL_LOC_A2430_2389, []], KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2390', [setattr(KL_CTX, 'KL_LOC_SynHyps_2391', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2389, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2391, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2441_2383, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2390][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2441_2383]) else False))][(-1)] if shen_eq(symdic.symdic_kl_x58, KL_CTX.KL_LOC_V2440_2382) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2440_2382, symdic.symdic_kl_x58, KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2392', [setattr(KL_CTX, 'KL_LOC_V2443_2393', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2439_2381[1], KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_A2430_2394', KL_CTX.KL_LOC_V2443_2393[0]), [setattr(KL_CTX, 'KL_LOC_V2444_2395', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2443_2393[1], KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_SynHyps_2396', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2394, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2396, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2444_2395) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2444_2395, [], KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2397', [setattr(KL_CTX, 'KL_LOC_SynHyps_2398', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2394, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2398, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2444_2395, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2397][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2444_2395]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2443_2393) else ([setattr(KL_CTX, 'KL_LOC_A2430_2399', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2443_2393, [KL_CTX.KL_LOC_A2430_2399, []], KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2400', [setattr(KL_CTX, 'KL_LOC_SynHyps_2401', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2399, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2401, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2443_2393, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2400][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2443_2393]) else False))][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2440_2382, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2392][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2440_2382]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2439_2381) else ([setattr(KL_CTX, 'KL_LOC_A2430_2402', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2439_2381, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2430_2402, []]], KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2403', [setattr(KL_CTX, 'KL_LOC_SynHyps_2404', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2402, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2380, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2380, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2404, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2439_2381, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2403][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2439_2381]) else False))][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2438_2379) else ([setattr(KL_CTX, 'KL_LOC_X_2405', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [setattr(KL_CTX, 'KL_LOC_A2430_2406', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2438_2379, [KL_CTX.KL_LOC_X_2405, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2430_2406, []]]], KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2407', [setattr(KL_CTX, 'KL_LOC_SynHyps_2408', KL_CTX.KL_LOC_V2437_2378[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2406, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2405, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2405, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2408, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2438_2379, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2407][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2438_2379]) else False))][(-1)] if shen_consp(KL_CTX.KL_LOC_V2437_2378) else ([setattr(KL_CTX, 'KL_LOC_X_2409', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [setattr(KL_CTX, 'KL_LOC_A2430_2410', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [setattr(KL_CTX, 'KL_LOC_SynHyps_2411', tco_apply(shen_newpv, [KL_ARG_V3051_2369])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2437_2378, [[KL_CTX.KL_LOC_X_2409, [symdic.symdic_kl_x58, [KL_CTX.KL_LOC_A2430_2410, []]]], KL_CTX.KL_LOC_SynHyps_2411], KL_ARG_V3051_2369]), [setattr(KL_CTX, 'KL_LOC_Result_2412', [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_ARG_V3050_2368, KL_CTX.KL_LOC_A2430_2410, KL_ARG_V3051_2369, (lambda : tail_call(kl_unifyx33, [KL_CTX.KL_LOC_X_2409, KL_CTX.KL_LOC_X2429_2376, KL_ARG_V3051_2369, (lambda : tail_call(kl_fwhen, [tco_apply(shen_uex63, [tco_apply(shen_deref, [KL_CTX.KL_LOC_X_2409, KL_ARG_V3051_2369])]), KL_ARG_V3051_2369, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2371, KL_ARG_V3051_2369, (lambda : tail_call(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2377, KL_ARG_V3048_2366, KL_CTX.KL_LOC_SynHyps_2411, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370]))]))]))]))])][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2437_2378, KL_ARG_V3051_2369]), KL_CTX.KL_LOC_Result_2412][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2437_2378]) else False))][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2436_2375) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2445_2413', tco_apply(shen_lazyderef, [KL_ARG_V3047_2365, KL_ARG_V3051_2369])), ([setattr(KL_CTX, 'KL_LOC_Y_2414', KL_CTX.KL_LOC_V2445_2413[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_syntaxx45hyps, [KL_CTX.KL_LOC_Y_2414, KL_ARG_V3048_2366, KL_ARG_V3049_2367, KL_ARG_V3050_2368, KL_ARG_V3051_2369, KL_ARG_V3052_2370])][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2445_2413) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2374, False) else KL_CTX.KL_LOC_Case_2374)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2372, False) else KL_CTX.KL_LOC_Case_2372)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-hyps', shen_syntaxx45hyps)

@tail_recursion
def shen_getx45syntaxx43semantics(KL_ARG_V3053_2415, KL_ARG_V3054_2416, KL_ARG_V3055_2417, KL_ARG_V3056_2418, KL_ARG_V3057_2419):

    class KL_Context:
        KL_LOC_Throwcontrol_2420 = None
        KL_LOC_Case_2421 = None
        KL_LOC_V2401_2422 = None
        KL_LOC_V2402_2423 = None
        KL_LOC_V2403_2424 = None
        KL_LOC_V2404_2425 = None
        KL_LOC_Semantics_2426 = None
        KL_LOC_V2405_2427 = None
        KL_LOC_Result_2428 = None
        KL_LOC_V2406_2429 = None
        KL_LOC_V2407_2430 = None
        KL_LOC_V2408_2431 = None
        KL_LOC_Semantics_2432 = None
        KL_LOC_V2409_2433 = None
        KL_LOC_Case_2434 = None
        KL_LOC_V2410_2435 = None
        KL_LOC_V2411_2436 = None
        KL_LOC_V2412_2437 = None
        KL_LOC_V2413_2438 = None
        KL_LOC_Semantics_2439 = None
        KL_LOC_V2414_2440 = None
        KL_LOC_V2415_2441 = None
        KL_LOC_V2416_2442 = None
        KL_LOC_G_2443 = None
        KL_LOC_V2417_2444 = None
        KL_LOC_Result_2445 = None
        KL_LOC_V2418_2446 = None
        KL_LOC_V2419_2447 = None
        KL_LOC_V2420_2448 = None
        KL_LOC_Semantics_2449 = None
        KL_LOC_V2421_2450 = None
        KL_LOC_V2422_2451 = None
        KL_LOC_V2423_2452 = None
        KL_LOC_G_2453 = None
        KL_LOC_V2424_2454 = None
        KL_LOC_V2425_2455 = None
        KL_LOC_X2397_2456 = None
        KL_LOC_Syntax_2457 = None
        KL_LOC_V2426_2458 = None
        KL_LOC_X_2459 = None
        KL_LOC_Rule_2460 = None
        KL_LOC_X2397_2461 = None
        KL_LOC_Syntax_2462 = None
        KL_LOC_Result_2463 = None
        KL_LOC_V2427_2464 = None
        KL_LOC_X_2465 = None
        KL_LOC_Rule_2466 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2420', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2420, [setattr(KL_CTX, 'KL_LOC_Case_2421', [setattr(KL_CTX, 'KL_LOC_V2401_2422', tco_apply(shen_lazyderef, [KL_ARG_V3053_2415, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2402_2423', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2403_2424', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2402_2423[0], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2404_2425', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2402_2423[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2426', KL_CTX.KL_LOC_V2404_2425[0]), [setattr(KL_CTX, 'KL_LOC_V2405_2427', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2404_2425[1], KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2426, KL_ARG_V3056_2418]), KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2405_2427) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2404_2425) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2403_2424) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2402_2423) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2401_2422) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2401_2422, [], KL_ARG_V3056_2418]), [setattr(KL_CTX, 'KL_LOC_Result_2428', [setattr(KL_CTX, 'KL_LOC_V2406_2429', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2407_2430', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2406_2429[0], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2408_2431', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2406_2429[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2432', KL_CTX.KL_LOC_V2408_2431[0]), [setattr(KL_CTX, 'KL_LOC_V2409_2433', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2408_2431[1], KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2432, KL_ARG_V3056_2418]), KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2409_2433) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2408_2431) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2407_2430) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2406_2429) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2401_2422, KL_ARG_V3056_2418]), KL_CTX.KL_LOC_Result_2428][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2401_2422]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2434', [setattr(KL_CTX, 'KL_LOC_V2410_2435', tco_apply(shen_lazyderef, [KL_ARG_V3053_2415, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2411_2436', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2412_2437', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2411_2436[0], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2413_2438', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2411_2436[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2439', KL_CTX.KL_LOC_V2413_2438[0]), [setattr(KL_CTX, 'KL_LOC_V2414_2440', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2413_2438[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2415_2441', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2414_2440[0], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2416_2442', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2414_2440[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_G_2443', KL_CTX.KL_LOC_V2416_2442[0]), [setattr(KL_CTX, 'KL_LOC_V2417_2444', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2416_2442[1], KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, [symdic.symdic_kl_where, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2443, KL_ARG_V3056_2418]), [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2439, KL_ARG_V3056_2418]), []]]], KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2417_2444) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2416_2442) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2415_2441) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2414_2440) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2413_2438) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2412_2437) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2411_2436) else False)][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2410_2435) else ([tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2410_2435, [], KL_ARG_V3056_2418]), [setattr(KL_CTX, 'KL_LOC_Result_2445', [setattr(KL_CTX, 'KL_LOC_V2418_2446', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2419_2447', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2418_2446[0], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2420_2448', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2418_2446[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_Semantics_2449', KL_CTX.KL_LOC_V2420_2448[0]), [setattr(KL_CTX, 'KL_LOC_V2421_2450', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2420_2448[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2422_2451', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2421_2450[0], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_V2423_2452', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2421_2450[1], KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_G_2453', KL_CTX.KL_LOC_V2423_2452[0]), [setattr(KL_CTX, 'KL_LOC_V2424_2454', tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_V2423_2452[1], KL_ARG_V3056_2418])), ([tco_apply(shen_incinfs, []), tco_apply(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2420, KL_ARG_V3056_2418, (lambda : tail_call(kl_bind, [KL_ARG_V3054_2416, [symdic.symdic_kl_where, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_G_2453, KL_ARG_V3056_2418]), [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_Semantics_2449, KL_ARG_V3056_2418]), []]]], KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2424_2454) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2423_2452) else False)][(-1)] if shen_eq(symdic.symdic_kl_where, KL_CTX.KL_LOC_V2422_2451) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2421_2450) else False)][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2420_2448) else False)][(-1)] if shen_eq(symdic.symdic_kl_x58x61, KL_CTX.KL_LOC_V2419_2447) else False)][(-1)] if shen_consp(KL_CTX.KL_LOC_V2418_2446) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2410_2435, KL_ARG_V3056_2418]), KL_CTX.KL_LOC_Result_2445][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2410_2435]) else False))][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2425_2455', tco_apply(shen_lazyderef, [KL_ARG_V3053_2415, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_X2397_2456', KL_CTX.KL_LOC_V2425_2455[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2457', KL_CTX.KL_LOC_V2425_2455[1]), [setattr(KL_CTX, 'KL_LOC_V2426_2458', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_X_2459', KL_CTX.KL_LOC_V2426_2458[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2460', KL_CTX.KL_LOC_V2426_2458[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2459, KL_CTX.KL_LOC_X2397_2456, KL_ARG_V3056_2418, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2457, KL_ARG_V3054_2416, KL_CTX.KL_LOC_Rule_2460, KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2426_2458) else False)][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2425_2455) else ([setattr(KL_CTX, 'KL_LOC_X2397_2461', tco_apply(shen_newpv, [KL_ARG_V3056_2418])), [setattr(KL_CTX, 'KL_LOC_Syntax_2462', tco_apply(shen_newpv, [KL_ARG_V3056_2418])), [tco_apply(shen_bindv, [KL_CTX.KL_LOC_V2425_2455, [KL_CTX.KL_LOC_X2397_2461, KL_CTX.KL_LOC_Syntax_2462], KL_ARG_V3056_2418]), [setattr(KL_CTX, 'KL_LOC_Result_2463', [setattr(KL_CTX, 'KL_LOC_V2427_2464', tco_apply(shen_lazyderef, [KL_ARG_V3055_2417, KL_ARG_V3056_2418])), ([setattr(KL_CTX, 'KL_LOC_X_2465', KL_CTX.KL_LOC_V2427_2464[0]), [setattr(KL_CTX, 'KL_LOC_Rule_2466', KL_CTX.KL_LOC_V2427_2464[1]), [tco_apply(shen_incinfs, []), tco_apply(kl_unifyx33, [KL_CTX.KL_LOC_X_2465, KL_CTX.KL_LOC_X2397_2461, KL_ARG_V3056_2418, (lambda : tail_call(shen_getx45syntaxx43semantics, [KL_CTX.KL_LOC_Syntax_2462, KL_ARG_V3054_2416, KL_CTX.KL_LOC_Rule_2466, KL_ARG_V3056_2418, KL_ARG_V3057_2419]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2427_2464) else False)][(-1)]), [tco_apply(shen_unbindv, [KL_CTX.KL_LOC_V2425_2455, KL_ARG_V3056_2418]), KL_CTX.KL_LOC_Result_2463][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if tco_apply(shen_pvarx63, [KL_CTX.KL_LOC_V2425_2455]) else False))][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2434, False) else KL_CTX.KL_LOC_Case_2434)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2421, False) else KL_CTX.KL_LOC_Case_2421)][(-1)]])][(-1)]
shen_add_fun('shen.get-syntax+semantics', shen_getx45syntaxx43semantics)

@tail_recursion
def shen_syntaxx45check(KL_ARG_V3058_2467, KL_ARG_V3059_2468, KL_ARG_V3060_2469, KL_ARG_V3061_2470, KL_ARG_V3062_2471):

    class KL_Context:
        KL_LOC_Throwcontrol_2472 = None
        KL_LOC_Case_2473 = None
        KL_LOC_V2394_2474 = None
        KL_LOC_Case_2475 = None
        KL_LOC_V2395_2476 = None
        KL_LOC_X_2477 = None
        KL_LOC_Syntax_2478 = None
        KL_LOC_C_2479 = None
        KL_LOC_Xx38x38_2480 = None
        KL_LOC_B_2481 = None
        KL_LOC_V2396_2482 = None
        KL_LOC_X_2483 = None
        KL_LOC_Syntax_2484 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Throwcontrol_2472', tco_apply(shen_catchpoint, [])), tail_call(shen_cutpoint, [KL_CTX.KL_LOC_Throwcontrol_2472, [setattr(KL_CTX, 'KL_LOC_Case_2473', [setattr(KL_CTX, 'KL_LOC_V2394_2474', tco_apply(shen_lazyderef, [KL_ARG_V3058_2467, KL_ARG_V3061_2470])), ([tco_apply(shen_incinfs, []), tco_apply(kl_thaw, [KL_ARG_V3062_2471])][(-1)] if shen_eq([], KL_CTX.KL_LOC_V2394_2474) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_Case_2475', [setattr(KL_CTX, 'KL_LOC_V2395_2476', tco_apply(shen_lazyderef, [KL_ARG_V3058_2467, KL_ARG_V3061_2470])), ([setattr(KL_CTX, 'KL_LOC_X_2477', KL_CTX.KL_LOC_V2395_2476[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2478', KL_CTX.KL_LOC_V2395_2476[1]), [setattr(KL_CTX, 'KL_LOC_C_2479', tco_apply(shen_newpv, [KL_ARG_V3061_2470])), [setattr(KL_CTX, 'KL_LOC_Xx38x38_2480', tco_apply(shen_newpv, [KL_ARG_V3061_2470])), [setattr(KL_CTX, 'KL_LOC_B_2481', tco_apply(shen_newpv, [KL_ARG_V3061_2470])), [tco_apply(shen_incinfs, []), tco_apply(kl_fwhen, [tco_apply(shen_grammar_symbolx63, [tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2477, KL_ARG_V3061_2470])]), KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_X_2477, [symdic.symdic_kl_x58, [[[symdic.symdic_kl_list, [KL_CTX.KL_LOC_B_2481, []]], [symdic.symdic_kl_x61x61x62, [KL_CTX.KL_LOC_C_2479, []]]], []]]], KL_ARG_V3060_2469, KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(kl_bind, [KL_CTX.KL_LOC_Xx38x38_2480, tco_apply(kl_concat, [symdic.symdic_kl_x38x38, tco_apply(shen_lazyderef, [KL_CTX.KL_LOC_X_2477, KL_ARG_V3061_2470])]), KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_Xx38x38_2480, [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [KL_ARG_V3059_2468, []]], []]]], [[KL_CTX.KL_LOC_Xx38x38_2480, [symdic.symdic_kl_x58, [[symdic.symdic_kl_list, [KL_CTX.KL_LOC_B_2481, []]], []]]], KL_ARG_V3060_2469], KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2478, KL_ARG_V3059_2468, KL_ARG_V3060_2469, KL_ARG_V3061_2470, KL_ARG_V3062_2471]))]))]))]))]))]))]))]))])][(-1)]][(-1)]][(-1)]][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2395_2476) else False)][(-1)]), ([setattr(KL_CTX, 'KL_LOC_V2396_2482', tco_apply(shen_lazyderef, [KL_ARG_V3058_2467, KL_ARG_V3061_2470])), ([setattr(KL_CTX, 'KL_LOC_X_2483', KL_CTX.KL_LOC_V2396_2482[0]), [setattr(KL_CTX, 'KL_LOC_Syntax_2484', KL_CTX.KL_LOC_V2396_2482[1]), [tco_apply(shen_incinfs, []), tco_apply(shen_tx42, [[KL_CTX.KL_LOC_X_2483, [symdic.symdic_kl_x58, [KL_ARG_V3059_2468, []]]], KL_ARG_V3060_2469, KL_ARG_V3061_2470, (lambda : tail_call(kl_cut, [KL_CTX.KL_LOC_Throwcontrol_2472, KL_ARG_V3061_2470, (lambda : tail_call(shen_syntaxx45check, [KL_CTX.KL_LOC_Syntax_2484, KL_ARG_V3059_2468, KL_ARG_V3060_2469, KL_ARG_V3061_2470, KL_ARG_V3062_2471]))]))])][(-1)]][(-1)]][(-1)] if shen_consp(KL_CTX.KL_LOC_V2396_2482) else False)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2475, False) else KL_CTX.KL_LOC_Case_2475)][(-1)] if shen_eq(KL_CTX.KL_LOC_Case_2473, False) else KL_CTX.KL_LOC_Case_2473)][(-1)]])][(-1)]
shen_add_fun('shen.syntax-check', shen_syntaxx45check)

@tail_recursion
def shen_semanticsx45check(KL_ARG_V3063_2485, KL_ARG_V3064_2486, KL_ARG_V3065_2487, KL_ARG_V3066_2488, KL_ARG_V3067_2489):

    class KL_Context:
        KL_LOC_Semanticsx42_2490 = None
    KL_CTX = KL_Context()
    global symdic
    return [setattr(KL_CTX, 'KL_LOC_Semanticsx42_2490', tco_apply(shen_newpv, [KL_ARG_V3066_2488])), [tco_apply(shen_incinfs, []), tail_call(kl_bind, [KL_CTX.KL_LOC_Semanticsx42_2490, tco_apply(shen_curry, [tco_apply(shen_renamex45semantics, [tco_apply(shen_deref, [KL_ARG_V3063_2485, KL_ARG_V3066_2488])])]), KL_ARG_V3066_2488, (lambda : tail_call(shen_tx42, [[KL_CTX.KL_LOC_Semanticsx42_2490, [symdic.symdic_kl_x58, [KL_ARG_V3064_2486, []]]], KL_ARG_V3065_2487, KL_ARG_V3066_2488, KL_ARG_V3067_2489]))])][(-1)]][(-1)]
shen_add_fun('shen.semantics-check', shen_semanticsx45check)

@tail_recursion
def shen_renamex45semantics(KL_ARG_V3068_2491):
    global symdic
    return ([tco_apply(shen_renamex45semantics, [KL_ARG_V3068_2491[0]]), tco_apply(shen_renamex45semantics, [KL_ARG_V3068_2491[1]])] if shen_consp(KL_ARG_V3068_2491) else ([symdic.symdic_shen_x60x45sem, [KL_ARG_V3068_2491, []]] if tco_apply(shen_grammar_symbolx63, [KL_ARG_V3068_2491]) else (KL_ARG_V3068_2491 if True else shen_simple_error('condition failure'))))
shen_add_fun('shen.rename-semantics', shen_renamex45semantics)
shen_initialise_arity_table(shen_to_cons([Sym('absvector'), 1, Sym('adjoin'), 2, Sym('and'), 2, Sym('append'), 2, Sym('arity'), 1, Sym('assoc'), 2, Sym('boolean?'), 1, Sym('cd'), 1, Sym('compile'), 3, Sym('concat'), 2, Sym('cons'), 2, Sym('cons?'), 1, Sym('cn'), 2, Sym('declare'), 2, Sym('destroy'), 1, Sym('difference'), 2, Sym('do'), 2, Sym('element?'), 2, Sym('empty?'), 1, Sym('enable-type-theory'), 1, Sym('interror'), 2, Sym('eval'), 1, Sym('eval-kl'), 1, Sym('explode'), 1, Sym('external'), 1, Sym('fail-if'), 2, Sym('fail'), 0, Sym('fix'), 2, Sym('findall'), 5, Sym('freeze'), 1, Sym('fst'), 1, Sym('gensym'), 1, Sym('get'), 3, Sym('get-time'), 1, Sym('address->'), 3, Sym('<-address'), 2, Sym('<-vector'), 2, Sym('>'), 2, Sym('>='), 2, Sym('='), 2, Sym('hd'), 1, Sym('hdv'), 1, Sym('hdstr'), 1, Sym('head'), 1, Sym('if'), 3, Sym('integer?'), 1, Sym('identical'), 4, Sym('inferences'), 0, Sym('intersection'), 2, Sym('length'), 1, Sym('lineread'), 0, Sym('load'), 1, Sym('<'), 2, Sym('<='), 2, Sym('vector'), 1, Sym('macroexpand'), 1, Sym('map'), 2, Sym('mapcan'), 2, Sym('maxinferences'), 1, Sym('not'), 1, Sym('nth'), 2, Sym('n->string'), 1, Sym('number?'), 1, Sym('occurs-check'), 1, Sym('occurrences'), 2, Sym('occurs-check'), 1, Sym('or'), 2, Sym('package'), 3, Sym('pos'), 2, Sym('print'), 1, Sym('profile'), 1, Sym('profile-results'), 0, Sym('pr'), 2, Sym('ps'), 1, Sym('preclude'), 1, Sym('preclude-all-but'), 1, Sym('protect'), 1, Sym('address->'), 3, Sym('put'), 4, Sym('shen.reassemble'), 2, Sym('read-file-as-string'), 1, Sym('read-file'), 1, Sym('read-byte'), 1, Sym('read-from-string'), 1, Sym('remove'), 2, Sym('reverse'), 1, Sym('set'), 2, Sym('simple-error'), 1, Sym('snd'), 1, Sym('specialise'), 1, Sym('spy'), 1, Sym('step'), 1, Sym('stinput'), 0, Sym('stoutput'), 0, Sym('string->n'), 1, Sym('string->symbol'), 1, Sym('string?'), 1, Sym('shen.strong-warning'), 1, Sym('subst'), 3, Sym('shen.sum'), 1, Sym('symbol?'), 1, Sym('tail'), 1, Sym('tl'), 1, Sym('tc'), 1, Sym('tc?'), 1, Sym('thaw'), 1, Sym('track'), 1, Sym('trap-error'), 2, Sym('tuple?'), 1, Sym('type'), 1, Sym('return'), 3, Sym('undefmacro'), 1, Sym('unprofile'), 1, Sym('unify'), 4, Sym('unify!'), 4, Sym('union'), 2, Sym('untrack'), 1, Sym('unspecialise'), 1, Sym('undefmacro'), 1, Sym('vector'), 1, Sym('vector->'), 3, Sym('value'), 1, Sym('variable?'), 1, Sym('version'), 1, Sym('warn'), 1, Sym('write-to-file'), 2, Sym('y-or-n?'), 1, Sym('+'), 2, Sym('*'), 2, Sym('/'), 2, Sym('-'), 2, Sym('=='), 2, Sym('shen.<1>'), 1, Sym('<e>'), 1, Sym('@p'), 2, Sym('@v'), 2, Sym('@s'), 2, Sym('preclude'), 1, Sym('include'), 1, Sym('preclude-all-but'), 1, Sym('include-all-but'), 1, Sym('where'), 2]))
kl_put(shen_intern('shen'), Sym('shen.external-symbols'), shen_to_cons([Sym('!'), Sym('}'), Sym('{'), Sym('-->'), Sym('<--'), Sym('&&'), Sym(':'), Sym(';'), Sym(':-'), Sym(':='), Sym('_'), Sym('*language*'), Sym('*implementation*'), Sym('*stinput*'), Sym('*home-directory*'), Sym('*version*'), Sym('*maximum-print-sequence-size*'), Sym('*macros*'), Sym('*os*'), Sym('*release*'), Sym('*property-vector*'), Sym('@v'), Sym('@p'), Sym('@s'), Sym('*port*'), Sym('*porters*'), Sym('<-'), Sym('->'), Sym('<e>'), Sym('=='), Sym('='), Sym('>='), Sym('>'), Sym('/.'), Sym('=!'), Sym('$'), Sym('-'), Sym('/'), Sym('*'), Sym('+'), Sym('<='), Sym('<'), Sym('>>'), tco_apply(kl_vector, [0]), Sym('==>'), Sym('y-or-n?'), Sym('write-to-file'), Sym('where'), Sym('when'), Sym('warn'), Sym('version'), Sym('verified'), Sym('variable?'), Sym('value'), Sym('vector->'), Sym('<-vector'), Sym('vector'), Sym('vector?'), Sym('unspecialise'), Sym('untrack'), Sym('unit'), Sym('shen.unix'), Sym('union'), Sym('unify'), Sym('unify!'), Sym('unprofile'), Sym('undefmacro'), Sym('return'), Sym('type'), Sym('tuple?'), Sym('true'), Sym('trap-error'), Sym('track'), Sym('time'), Sym('thaw'), Sym('tc?'), Sym('tc'), Sym('tl'), Sym('tlstr'), Sym('tlv'), Sym('tail'), Sym('systemf'), Sym('synonyms'), Sym('symbol'), Sym('symbol?'), Sym('string->symbol'), Sym('subst'), Sym('string?'), Sym('string->n'), Sym('stream'), Sym('string'), Sym('stinput'), Sym('stoutput'), Sym('step'), Sym('spy'), Sym('specialise'), Sym('snd'), Sym('simple-error'), Sym('set'), Sym('save'), Sym('str'), Sym('run'), Sym('reverse'), Sym('remove'), Sym('read'), Sym('read-file'), Sym('read-file-as-bytelist'), Sym('read-file-as-string'), Sym('read-byte'), Sym('read-from-string'), Sym('quit'), Sym('put'), Sym('preclude'), Sym('preclude-all-but'), Sym('ps'), Sym('prolog?'), Sym('protect'), Sym('profile-results'), Sym('profile'), Sym('print'), Sym('pr'), Sym('pos'), Sym('package'), Sym('output'), Sym('out'), Sym('or'), Sym('open'), Sym('occurrences'), Sym('occurs-check'), Sym('n->string'), Sym('number?'), Sym('number'), Sym('null'), Sym('nth'), Sym('not'), Sym('nl'), Sym('mode'), Sym('macro'), Sym('macroexpand'), Sym('maxinferences'), Sym('mapcan'), Sym('map'), Sym('make-string'), Sym('load'), Sym('loaded'), Sym('list'), Sym('lineread'), Sym('limit'), Sym('length'), Sym('let'), Sym('lazy'), Sym('lambda'), Sym('is'), Sym('intersection'), Sym('inferences'), Sym('intern'), Sym('integer?'), Sym('input'), Sym('input+'), Sym('include'), Sym('include-all-but'), Sym('in'), Sym('if'), Sym('identical'), Sym('head'), Sym('hd'), Sym('hdv'), Sym('hdstr'), Sym('hash'), Sym('get'), Sym('get-time'), Sym('gensym'), Sym('function'), Sym('fst'), Sym('freeze'), Sym('fix'), Sym('file'), Sym('fail'), Sym('fail-if'), Sym('fwhen'), Sym('findall'), Sym('false'), Sym('enable-type-theory'), Sym('explode'), Sym('external'), Sym('exception'), Sym('eval-kl'), Sym('eval'), Sym('error-to-string'), Sym('error'), Sym('empty?'), Sym('element?'), Sym('do'), Sym('difference'), Sym('destroy'), Sym('defun'), Sym('define'), Sym('defmacro'), Sym('defcc'), Sym('defprolog'), Sym('declare'), Sym('datatype'), Sym('cut'), Sym('cn'), Sym('cons?'), Sym('cons'), Sym('cond'), Sym('concat'), Sym('compile'), Sym('cd'), Sym('cases'), Sym('call'), Sym('close'), Sym('bind'), Sym('bound?'), Sym('boolean?'), Sym('boolean'), Sym('bar!'), Sym('assoc'), Sym('arity'), Sym('append'), Sym('and'), Sym('adjoin'), Sym('<-address'), Sym('address->'), Sym('absvector?'), Sym('absvector'), Sym('abort')]), shen_get(Sym('*property-vector*')))
apply(kl_declare, [symdic.symdic_kl_absvectorx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_adjoin, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_and, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_shen_app, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_append, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_arity, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_assoc, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_booleanx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_boundx63, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_cd, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_close, [[symdic.symdic_kl_stream, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_cn, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_compile, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x61x61x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_consx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_destroy, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_difference, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_do, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_B, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x60ex62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x61x61x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]]])
apply(kl_declare, [symdic.symdic_x60x33x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x61x61x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_elementx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_emptyx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_enablex45typex45theory, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_external, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_errorx45tox45string, [symdic.symdic_kl_exception, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_explode, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_string, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_failx45if, [[symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_fix, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_format, [[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_freeze, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_lazy, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_fst, [[symdic.symdic_A, [symdic.symdic_kl_x42, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_gensym, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_x60x45vector, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_vectorx45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_vector, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_getx45time, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_hash, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_head, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_hdv, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_hdstr, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_if, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_include, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_includex45allx45but, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_inferences, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]])
apply(kl_declare, [symdic.symdic_shen_insert, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_integerx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_intersection, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_length, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_limit, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_load, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_map, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_mapcan, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_B, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_maxinferences, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_nx45x62string, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_nl, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_not, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_nth, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_numberx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_occurrences, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_B, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_occursx45check, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_optimise, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_or, [symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_boolean, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_pos, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_pr, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_print, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_profile, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_preclude, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_shen_procx45nl, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_profilex45results, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_protect, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_precludex45allx45but, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_shen_prhush, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_ps, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_unit, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45byte, [[symdic.symdic_kl_stream, [symdic.symdic_kl_in, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45filex45asx45bytelist, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_number, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45filex45asx45string, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45file, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_unit, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_readx45fromx45string, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_unit, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_remove, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_reverse, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_simplex45error, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_snd, [[symdic.symdic_A, [symdic.symdic_kl_x42, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]]])
apply(kl_declare, [symdic.symdic_kl_specialise, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_spy, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_step, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_stinput, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_stream, [symdic.symdic_kl_in, []]], []]]])
apply(kl_declare, [symdic.symdic_kl_stoutput, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_stream, [symdic.symdic_kl_out, []]], []]]])
apply(kl_declare, [symdic.symdic_kl_stringx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_str, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_stringx45x62n, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_stringx45x62symbol, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_shen_sum, [[symdic.symdic_kl_list, [symdic.symdic_kl_number, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]]])
apply(kl_declare, [symdic.symdic_kl_symbolx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_systemf, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_kl_symbol, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_tail, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_tlstr, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_tlv, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_vector, [symdic.symdic_A, []]], []]]]])
apply(kl_declare, [symdic.symdic_kl_tc, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_tcx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_thaw, [[symdic.symdic_kl_lazy, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]]])
apply(kl_declare, [symdic.symdic_kl_track, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_trapx45error, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_exception, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_shen_truncate, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_tuplex63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_undefmacro, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_union, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[[symdic.symdic_kl_list, [symdic.symdic_A, []]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_list, [symdic.symdic_A, []]], []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_unprofile, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_B, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_untrack, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_unspecialise, [symdic.symdic_kl_symbol, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_symbol, []]]]])
apply(kl_declare, [symdic.symdic_kl_variablex63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_vectorx63, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_version, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_string, []]]]])
apply(kl_declare, [symdic.symdic_kl_writex45tox45file, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_A, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_yx45orx45nx63, [symdic.symdic_kl_string, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]]])
apply(kl_declare, [symdic.symdic_kl_x62, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x60, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x62x61, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x60x61, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x61, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x43, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x47, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x45, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x42, [symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_kl_number, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_number, []]]], []]]]])
apply(kl_declare, [symdic.symdic_kl_x61x61, [symdic.symdic_A, [symdic.symdic_kl_x45x45x62, [[symdic.symdic_B, [symdic.symdic_kl_x45x45x62, [symdic.symdic_kl_boolean, []]]], []]]]])
# included at the end of shen.py

def shen_expt(KL_ARG_V1518_757, KL_ARG_V1519_758):
    KL_ARG_V1518_757, KL_ARG_V1519_758 = float(KL_ARG_V1518_757), float(KL_ARG_V1519_758)
    return (1 if (0 == KL_ARG_V1519_758) else ((KL_ARG_V1518_757 * tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 - 1)])) if (KL_ARG_V1519_758 > 0) else ((1 * (tco_apply(shen_expt, [KL_ARG_V1518_757, (KL_ARG_V1519_758 + 1)]) / KL_ARG_V1518_757)) if True else shen_simple_error('condition failure'))))

def kl_booleanx63(KL_ARG_V1857_1068):
    if isinstance(KL_ARG_V1857_1068, Sym) and (KL_ARG_V1857_1068.sym == "true" or KL_ARG_V1857_1068.sym == "false"):
        return True
    else:
        return (True if (True == KL_ARG_V1857_1068) else (True if (False == KL_ARG_V1857_1068) else (False if True else shen_simple_error('condition failure'))))
