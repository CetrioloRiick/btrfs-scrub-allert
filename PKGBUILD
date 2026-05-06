# Mantainer: Diego Quarantani <diego.q@ik.me>
pkgname=btrfs-telegram-notifier
pkgver=0.1
pkgrel=1
pkgdesc="Telegram alerts for btrfs scrub failures (btrfsmaintenance integration)"
arch=('any')
url="https://github.com/CetrioloRiick/btrfs-scrub-allert"
license=('GPL')

depends=('python-requests' 'python-dotenv' 'btrfsmaintenance')
source=('btrfs-telegram-alert.py'
        'telegram-alert.conf')
sha256sums=('SKIP' 'SKIP') # Sostituisci con i veri hash usando 'updpkgsums'

package() {
  # 1. Installa lo script Python in /usr/bin
  install -Dm755 "${srcdir}/btrfs-telegram-alert.py" "${pkgdir}/usr/bin/btrfs-telegram-alert"

  # 2. Installa il drop-in di systemd per il servizio btrfs-scrub
  # Il percorso deve essere /usr/lib/systemd/system/<nome-servizio>.service.d/
  install -Dm644 "${srcdir}/telegram-alert.conf" \
    "${pkgdir}/usr/lib/systemd/system/btrfs-scrub.service.d/telegram-alert.conf"
}