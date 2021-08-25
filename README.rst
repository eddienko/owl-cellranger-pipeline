Owl Cellranger Pipeline
=======================

This is an `Owl Pipeline <https://eddienko.github.io/owl-pipeline>`__ that runs
`Cell Ranger <https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger>`__
to process single-cell data.


Pipeline Definition
-------------------

An example pipeline definition file is:

  .. code-block:: yaml

    # Version of the configuration file
    version: 1

    name: cellranger

    # Location of the cellranger software
    # soft: /soft/cellranger
    # command to run, currently only count
    command: count
    # Arguments for the command above
    id: SITTF9
    sample: SITTF9
    transcriptome: /storage/shared/cellranger_refs/refdata-gex-mm10-2020-A
    fastqs: /storage/user/cellranger/SLX-20946
    output_dir: /storage/user/cellranger/runs

    # extra
    # useful to add localcores and localmem in case cellranger fails to detect them
    extra: ["--localcores", "20", "--localmem", "64"]

    requirements:
    workers: 1
    threads: 25
    memory: 64
