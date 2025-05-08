/**
 * Adds fade-out animation to notifications after 4 seconds.
 * Replaces `animate__fadeInRight` with `animate__fadeOutRight` class.
 */
const activateNotificationFadeOut = () => {
  const notifications = document.querySelectorAll(".notification");

  notifications.forEach((notification) => {
    setTimeout(() => {
      notification.classList.remove("animate__fadeInRight");
      notification.classList.add("animate__fadeOutRight");
    }, 4 * 1000);
  });
};

document.addEventListener("DOMContentLoaded", () => {
  activateNotificationFadeOut();
});
