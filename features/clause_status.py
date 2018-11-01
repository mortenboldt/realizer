"""
license info
"""


from enum import Enum, unique


@unique
class ClauseStatus(Enum):
    """
    This is an enumeration of the two different types of clauses used in the
    SimplNLG package. Clauses can be either matrix or subordinate. Matrix clauses
    are not contained within any other clause and frequently span an entire
    sentence, whereas a subordinate clauses is contained within another clause.
    </p>

    <p>
    As an example, take the phrase, <em><b>whoever said it</b> is wrong</em>.
    This phrase has two clauses, one being the main clause and the other being a
    subordinate clause. The section in <b>bold</b> type highlights the
    subordinate clause. It is entirely contained within another clause. The
    matrix clause is of the form <em>he is wrong</em> or to be more general
    <em>X is wrong</em>. <em>X</em> can be replaced with a single subject or, as
    is the case here, by a subordinate clause.
    </p>

    <p>
    The clause status is recorded under the {@code Feature.CLAUSE_STATUS} feature
    and applies only to clauses.
    """

    # This enumeration represents a matrix clause. A matrix clause is not
    # subordinate to any other clause and therefore sits at the top-level of
    # the clause hierarchy, typically spanning the whole sentence.
    MATRIX = 1

    # The subordinate clauses are contained within a higher clause
    SUBORDINATE = 2
