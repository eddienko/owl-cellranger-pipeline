from pathlib import Path

import voluptuous as vo

schema_count = vo.Schema(
    {
        vo.Optional("soft", default="/soft/cellranger"): vo.Coerce(Path),
        vo.Required("command"): vo.In(["count"]),
        vo.Required("id"): str,
        vo.Optional("fastqs"): vo.Coerce(Path),
        vo.Optional("libraries"): vo.Coerce(Path),
        vo.Optional("sample"): str,
        vo.Optional("transcriptome"): vo.Coerce(Path),
        vo.Optional("feature-ref"): vo.Coerce(Path),
        vo.Optional("target-panel"): vo.Coerce(Path),
        vo.Optional("expected-cells"): int,
        vo.Optional("force-cells"): int,
        vo.Optional("chemistry"): str,
        vo.Optional("r1-length"): int,
        vo.Optional("r2-length"): int,
        vo.Optional("lanes"): str,
        vo.Optional("extra"): vo.Schema([str]),
        vo.Required("output_dir"): vo.Coerce(Path),
    },
    extra=vo.REMOVE_EXTRA,
)

schema_mkfastq = vo.Schema(
    {
        vo.Optional("soft", default="/soft/cellranger"): vo.Coerce(Path),
        vo.Required("command"): vo.In(["mkfastq"]),
        vo.Required("run"): vo.Coerce(Path),
        vo.Optional("id"): str,
        vo.Optional("samplesheet"): vo.Coerce(Path),
        vo.Optional("csv"): vo.Coerce(Path),
        vo.Optional("simple-csv"): vo.Coerce(Path),
        vo.Optional("lanes"): str,
        vo.Required("output_dir"): vo.Coerce(Path),
        vo.Optional("project"): str,
    },
    extra=vo.REMOVE_EXTRA,
)

schema = vo.Any(schema_count, schema_mkfastq)
