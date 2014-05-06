# -*- coding: utf-8 -*-

#    This file is part of RDF-PATCH
#    Copyright (C) 2013 Pierre-Antoine Champin <pchampin@liris.cnrs.fr> /
#    Universite de Lyon <http://www.universite-lyon.fr>
#
#    RDF-PATCH is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RDF-PATCH is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with RDF-PATCH.  If not, see <http://www.gnu.org/licenses/>.

def apply(patch, graph, init_ns=None, init_var=None, syntax="simple"):
    """
    I parse `patch` (either a file-like or a string), and apply it to `graph`.

    Other parameters:
    * `init_ns`: initial namespace binding
    * `init_var`: initial variables binding
    * `syntax`: concrete syntax used in `patch`
    """
    if syntax == "simple":
        from .simple import Parser
    else:
        raise ValueError("Unknown LD-Patch syntax {}".format())

    if hasattr(patch, "read"):
        patch = patch.read()

    from .engine import PatchEngine
    Parser(PatchEngine(graph, init_ns, init_var)).parseString(patch)