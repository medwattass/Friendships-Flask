const userSelect = document.getElementById('user_selection');
const friendSelect = document.getElementById('friend_selection');

friendSelect.style.display = 'none';

userSelect.addEventListener('change', () => {
    if (userSelect.value !== '0') {
        friendSelect.style.display = 'block';
    } else {
        friendSelect.style.display = 'none';
    }
});