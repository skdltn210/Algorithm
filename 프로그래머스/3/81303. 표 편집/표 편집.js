class Node {
    constructor(value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

function solution(n, k, cmd) {
    let head = new Node(0);
    let current = head;
    for (let i = 1; i < n; i++) {
        const newNode = new Node(i);
        current.next = newNode;
        newNode.prev = current;
        current = newNode;
    }

    current = head;
    for (let i = 0; i < k; i++) {
        current = current.next;
    }

    const stack = [];
    const deleted = new Set();

    for (const command of cmd) {
        const [action, amount] = command.split(' ');

        switch (action) {
            case 'U':
                for (let i = 0; i < Number(amount); i++) {
                    current = current.prev;
                }
                break;
            case 'D':
                for (let i = 0; i < Number(amount); i++) {
                    current = current.next;
                }
                break;
            case 'C':
                deleted.add(current.value);
                stack.push(current);

                const prev = current.prev;
                const next = current.next;

                if (prev) prev.next = next;
                if (next) next.prev = prev;

                current = next ? next : prev;
                break;
            case 'Z':
                const restored = stack.pop();
                deleted.delete(restored.value);

                const prevNode = restored.prev;
                const nextNode = restored.next;

                if (prevNode) prevNode.next = restored;
                if (nextNode) nextNode.prev = restored;
                break;
        }
    }

    let result = '';
    for (let i = 0; i < n; i++) {
        result += deleted.has(i) ? 'X' : 'O';
    }

    return result;
}