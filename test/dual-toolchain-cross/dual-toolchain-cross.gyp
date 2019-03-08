
{
  'target_defaults': {
    'cflags': [],
    'default_configuration': 'Release',
    'defines': [],
    'include_dirs': [],
    'libraries': [],
  },
  'variables': {
    'intermediate_file': '<(SHARED_INTERMEDIATE_DIR)/hi.c',
    'host_arch': 'x64',
    'target_arch': 'x64',
  },
  'targets': [
    {
      'target_name': 'print_source#host',
      'type': 'executable',
      'sources': [
        'print_source.c',
      ],
      'toolsets': ['host'],
    },
#    {
#      'target_name': 'run_print_source',
#      'dependencies': 'print_source#host',
#      'actions': [
#        {
#          'action_name': '
#        },
#      ],
#    },
    {
      'target_name': 'hi',
      'type': 'executable',
      'toolsets': ['target'],
      'sources': [
        '$(intermediate_file)',
      ],
    },
  ],
}
