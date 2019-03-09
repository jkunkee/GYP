
{
  'target_defaults': {
    'cflags': [],
#    'default_configuration': 'Release',
    'defines': [],
    'include_dirs': [],
    'libraries': [],
  },
  'variables': {
    'intermediate_file': '<(SHARED_INTERMEDIATE_DIR)/hi.c',
    'host_arch': 'x64',
    'target_arch': 'arm64',
  },
  'targets': [
    {
      'target_name': 'print_source',
      'type': 'executable',
      'sources': [
        'print_source.c',
      ],
      'toolsets': ['host'],
    },
    {
      'target_name': 'run_print_source',
      'type': 'none',
      'dependencies': [ 'print_source#host' ],
      'actions': [
        {
          'action_name': 'run_print_source',
          'inputs': [ '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)print_source<(EXECUTABLE_SUFFIX)' ],
          'outputs': [ '<(intermediate_file)' ],
          'action': ['<@(_inputs)', '<@(_outputs)'],
        },
      ],
      'toolsets': ['host'],
    },
    {
      'target_name': 'hi',
      'type': 'executable',
      'dependencies': [ 'run_print_source#host' ],
      'toolsets': ['target'],
      'sources': [
        '<(intermediate_file)',
      ],
    },
  ],
}
