const editButtons = document.getElementsByClassName('editButton');
const reviewText = document.getElementById('id_body');
const reviewForm = document.getElementById('reviewForm');
const submitButton = document.getElementById('submitButton');

// Grabbing Id's for delete confirmation
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("deleteButton");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
  button.addEventListener('click', (e) => {
    let reviewId = e.target.getAttribute('review_id');
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewContent;
    submitButton.innerText = 'Update';
    reviewForm.setAttribute('action', `edit_review/${reviewId}`);
  });
}

// Function to delete reviews
for (let button of deleteButtons) {
  button.addEventListener('click', (e) => {
    let reviewId = e.target.getAttribute('review_id');
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}