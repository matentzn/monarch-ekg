# Auto generated from monarch-ekg.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-03-16 17:47
# Schema: monarch-ekg
#
# id: https://w3id.org/monarch-ekg
# description: This is the Schema for the Organisational Monarch Initiative Knowledge Graph (Monarch EKG). The EKG
#              is usually used for Enterprise Knowledge Graph, but the abbreviation is pretty ubiquitous now.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
MONARCH_EKG = CurieNamespace('monarch-ekg', 'https://w3id.org/mixs/monarch-ekg/')
DEFAULT_ = MONARCH-EKG


# Types

# Class references



@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH-EKG.NamedThing
    class_class_curie: ClassVar[str] = "monarch-ekg:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = MONARCH-EKG.NamedThing

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


class ProfessionalIndividual(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH-EKG.ProfessionalIndividual
    class_class_curie: ClassVar[str] = "monarch-ekg:ProfessionalIndividual"
    class_name: ClassVar[str] = "professional individual"
    class_model_uri: ClassVar[URIRef] = MONARCH-EKG.ProfessionalIndividual


class Grant(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH-EKG.Grant
    class_class_curie: ClassVar[str] = "monarch-ekg:Grant"
    class_name: ClassVar[str] = "grant"
    class_model_uri: ClassVar[URIRef] = MONARCH-EKG.Grant


class Project(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH-EKG.Project
    class_class_curie: ClassVar[str] = "monarch-ekg:Project"
    class_name: ClassVar[str] = "project"
    class_model_uri: ClassVar[URIRef] = MONARCH-EKG.Project


class ProjectGoal(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH-EKG.ProjectGoal
    class_class_curie: ClassVar[str] = "monarch-ekg:ProjectGoal"
    class_name: ClassVar[str] = "project goal"
    class_model_uri: ClassVar[URIRef] = MONARCH-EKG.ProjectGoal


class Organisation(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH-EKG.Organisation
    class_class_curie: ClassVar[str] = "monarch-ekg:Organisation"
    class_name: ClassVar[str] = "organisation"
    class_model_uri: ClassVar[URIRef] = MONARCH-EKG.Organisation


class Software(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH-EKG.Software
    class_class_curie: ClassVar[str] = "monarch-ekg:Software"
    class_name: ClassVar[str] = "software"
    class_model_uri: ClassVar[URIRef] = MONARCH-EKG.Software


# Enumerations


# Slots
class slots:
    pass

slots.name = Slot(uri=MONARCH-EKG.name, name="name", curie=MONARCH-EKG.curie('name'),
                   model_uri=MONARCH-EKG.name, domain=None, range=Optional[str])
