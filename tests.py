from strtest import str_test


class Node:
    def __init__(self, v=None, n=None):
        self.value = v
        self.next = n


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1

    def _make_list(self, l):
        nodes = []
        for v in l:
            n = Node(v)
            if nodes:
                nodes[-1].next = n
            nodes.append(n)
        return nodes

    def _strlist(self, l):
        s = []
        while l:
            s.append(f'{l.value}')
            l = l.next
        return '->'.join(s) or 'Empty'

    def _check(self, values, k):
        head = None
        expected = None
        if values:
            l = self._make_list(values)
            head = l[0]
            if k <= len(l):
                expected = l[-k]
        ret = self.function(head, k)
        e = f'Não funcionou para a lista "{self._strlist(head)}" e k={k}'
        self.assertEqual(expected, ret, msg=e)

    def test_1(self):
        self._check(None, 10)

    def test_2(self):
        self._check([1, 1, 1, 1, 1, 1], 3)

    def test_3(self):
        self._check(range(1, 11), 1)

    def test_4(self):
        self._check(range(1, 11), 10)

    def test_5(self):
        self._check(range(1, 11), 20)

    def test_6(self):
        self._check(range(1, 11), 2)

    def test_7(self):
        self._check(range(1, 11), 3)

    def test_8(self):
        self._check(range(1, 11), 4)

    def test_9(self):
        self._check(range(1, 11), 5)

    def test_10(self):
        self._check(range(1, 11), 6)
