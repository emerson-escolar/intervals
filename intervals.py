import math

def check_interval(pair, n=math.inf):
    b,d = pair
    return (0 <= b <= d < n)


def get_presence_at(pair, i):
    b,d = pair
    return (b <= i <= d)

def get_dimension_at(pair, i):
    return int(get_presence_at(pair, i))


def as_dimension_vector(pair, n):
    return [get_dimension_at(pair, i) for i in range(n)]


def intervals_iter(n):
    for b in range(n):
        for d in range(b,n):
            yield (b,d)


def intersect_intervals(I,J):
    source_b, source_d = I
    target_b, target_d = J
    intersection = ( max(source_b, target_b), min(source_d, target_d) )

    if intersection[0] > intersection[1]:
        return None
    return intersection


def has_nonzero_morphism(domain, codomain):
    n = math.inf
    if not check_interval(domain,n) or not check_interval(codomain,n):
        raise RuntimeError("Invalid input")

    intersection = intersect_intervals(domain, codomain)
    if intersection == None:
        return False

    source_b, source_d = domain
    target_b, target_d = codomain
    return not (source_b < target_b or source_d < target_d)


def box_has_nonzero_morphism(domain_pattern, codomain_pattern, direction):
    if len(domain_pattern) != 2 or len(codomain_pattern) != 2:
        raise RuntimeError("improper data")

    if direction not in ("f", "b"):
        raise RuntimeError("Orientation direction improperly specified!")

    if direction == "b":
        domain_pattern = list(reversed(domain_pattern))
        codomain_pattern = list(reversed(codomain_pattern))

    if not any(domain_pattern) or not any(codomain_pattern):
        return False

    pattern = (domain_pattern[0], domain_pattern[1],
               codomain_pattern[0], codomain_pattern[1])
    if pattern in ((1,0,1,1), (1,1,0,1)):
        return False

    return True


def get_box_pattern(domain, codomain, i):
    domain_pattern = [get_presence_at(domain, j) for j in (i,i+1)]
    codomain_pattern = [get_presence_at(codomain, j) for j in (i,i+1)]
    return (domain_pattern, codomain_pattern)


def has_nonzero_zigzag_morphism(domain, codomain, orientation=None):
    if orientation == None:
        return has_nonzero_morphism(domain, codomain)
    n = len(orientation) + 1
    if not check_interval(domain,n) or not check_interval(codomain,n):
        raise RuntimeError("Invalid input interval")


    intersection = intersect_intervals(domain, codomain)
    if intersection == None:
        return False
    span = (min(min(domain),min(codomain)), max(max(domain),max(codomain)))

    left, right = intersection
    critical_pts = []
    if get_presence_at(domain, left - 1) or get_presence_at(codomain, left - 1):
        critical_pts.append(left - 1)
    if (get_presence_at(domain, right) or get_presence_at(codomain, right)) and right + 1 < n:
        critical_pts.append(right)

    for i in critical_pts:
        domain_pattern, codomain_pattern = get_box_pattern(domain, codomain, i)

        if not box_has_nonzero_morphism(domain_pattern, codomain_pattern, orientation[i]):
            return False
    return True


