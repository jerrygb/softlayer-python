"""
    SoftLayer.CLI.routes
    ~~~~~~~~~~~~~~~~~~~~~
    This is how all commands are registered with the CLI.

    :license: MIT, see LICENSE for more details.
"""

ALL_ROUTES = [
    ('call-api', 'SoftLayer.CLI.call_api:cli'),

    ('vs', 'SoftLayer.CLI.virt'),
    ('vs:cancel', 'SoftLayer.CLI.virt.cancel:cli'),
    ('vs:capture', 'SoftLayer.CLI.virt.capture:cli'),
    ('vs:create', 'SoftLayer.CLI.virt.create:cli'),
    ('vs:create-options', 'SoftLayer.CLI.virt.create_options:cli'),
    ('vs:detail', 'SoftLayer.CLI.virt.detail:cli'),
    ('vs:dns-sync', 'SoftLayer.CLI.virt.dns:cli'),
    ('vs:edit', 'SoftLayer.CLI.virt.edit:cli'),
    ('vs:list', 'SoftLayer.CLI.virt.list:cli'),
    ('vs:network', 'SoftLayer.CLI.virt.network:cli'),
    ('vs:pause', 'SoftLayer.CLI.virt.power:pause'),
    ('vs:power_off', 'SoftLayer.CLI.virt.power:power_off'),
    ('vs:power_on', 'SoftLayer.CLI.virt.power:power_on'),
    ('vs:rescue', 'SoftLayer.CLI.virt.power:rescue'),
    ('vs:resume', 'SoftLayer.CLI.virt.power:resume'),
    ('vs:ready', 'SoftLayer.CLI.virt.ready:cli'),
    ('vs:reboot', 'SoftLayer.CLI.virt.power:reboot'),
    ('vs:reload', 'SoftLayer.CLI.virt.reload:cli'),
    ('vs:upgrade', 'SoftLayer.CLI.virt.upgrade:cli'),

    ('cdn', 'SoftLayer.CLI.cdn'),
    ('cdn:detail', 'SoftLayer.CLI.cdn.detail:cli'),
    ('cdn:list', 'SoftLayer.CLI.cdn.list:cli'),
    ('cdn:load', 'SoftLayer.CLI.cdn.load:cli'),
    ('cdn:origin-add', 'SoftLayer.CLI.cdn.origin_add:cli'),
    ('cdn:origin-list', 'SoftLayer.CLI.cdn.origin_list:cli'),
    ('cdn:origin-remove', 'SoftLayer.CLI.cdn.origin_remove:cli'),
    ('cdn:purge', 'SoftLayer.CLI.cdn.purge:cli'),

    ('config', 'SoftLayer.CLI.config'),
    ('config:setup', 'SoftLayer.CLI.config.setup:cli'),
    ('config:show', 'SoftLayer.CLI.config.show:cli'),

    ('dns', 'SoftLayer.CLI.dns'),
    ('dns:import', 'SoftLayer.CLI.dns.zone_import:cli'),
    ('dns:record-add', 'SoftLayer.CLI.dns.record_add:cli'),
    ('dns:record-edit', 'SoftLayer.CLI.dns.record_edit:cli'),
    ('dns:record-list', 'SoftLayer.CLI.dns.record_list:cli'),
    ('dns:record-remove', 'SoftLayer.CLI.dns.record_remove:cli'),
    ('dns:zone-create', 'SoftLayer.CLI.dns.zone_create:cli'),
    ('dns:zone-delete', 'SoftLayer.CLI.dns.zone_delete:cli'),
    ('dns:zone-list', 'SoftLayer.CLI.dns.zone_list:cli'),
    ('dns:zone-print', 'SoftLayer.CLI.dns.zone_print:cli'),

    ('firewall', 'SoftLayer.CLI.firewall'),
    ('firewall:add', 'SoftLayer.CLI.firewall.add:cli'),
    ('firewall:cancel', 'SoftLayer.CLI.firewall.cancel:cli'),
    ('firewall:detail', 'SoftLayer.CLI.firewall.detail:cli'),
    ('firewall:edit', 'SoftLayer.CLI.firewall.edit:cli'),
    ('firewall:list', 'SoftLayer.CLI.firewall.list:cli'),

    ('globalip', 'SoftLayer.CLI.globalip'),
    ('globalip:assign', 'SoftLayer.CLI.globalip.assign:cli'),
    ('globalip:cancel', 'SoftLayer.CLI.globalip.cancel:cli'),
    ('globalip:create', 'SoftLayer.CLI.globalip.create:cli'),
    ('globalip:list', 'SoftLayer.CLI.globalip.list:cli'),
    ('globalip:unassign', 'SoftLayer.CLI.globalip.unassign:cli'),

    ('image', 'SoftLayer.CLI.image'),
    ('image:delete', 'SoftLayer.CLI.image.delete:cli'),
    ('image:detail', 'SoftLayer.CLI.image.detail:cli'),
    ('image:edit', 'SoftLayer.CLI.image.edit:cli'),
    ('image:list', 'SoftLayer.CLI.image.list:cli'),

    ('iscsi', 'SoftLayer.CLI.iscsi'),
    ('iscsi:cancel', 'SoftLayer.CLI.iscsi.cancel:cli'),
    ('iscsi:create', 'SoftLayer.CLI.iscsi.create:cli'),
    ('iscsi:detail', 'SoftLayer.CLI.iscsi.detail:cli'),
    ('iscsi:list', 'SoftLayer.CLI.iscsi.list:cli'),

    ('loadbal', 'SoftLayer.CLI.loadbal'),
    ('loadbal:cancel', 'SoftLayer.CLI.loadbal.cancel:cli'),
    ('loadbal:create', 'SoftLayer.CLI.loadbal.create:cli'),
    ('loadbal:create-options', 'SoftLayer.CLI.loadbal.create_options:cli'),
    ('loadbal:detail', 'SoftLayer.CLI.loadbal.detail:cli'),
    ('loadbal:group-add', 'SoftLayer.CLI.loadbal.group_add:cli'),
    ('loadbal:group-delete', 'SoftLayer.CLI.loadbal.group_delete:cli'),
    ('loadbal:group-edit', 'SoftLayer.CLI.loadbal.group_edit:cli'),
    ('loadbal:group-reset', 'SoftLayer.CLI.loadbal.group_reset:cli'),
    ('loadbal:health-checks', 'SoftLayer.CLI.loadbal.health_checks:cli'),
    ('loadbal:list', 'SoftLayer.CLI.loadbal.list:cli'),
    ('loadbal:routing-methods', 'SoftLayer.CLI.loadbal.routing_methods:cli'),
    ('loadbal:routing-types', 'SoftLayer.CLI.loadbal.routing_types:cli'),
    ('loadbal:service-add', 'SoftLayer.CLI.loadbal.service_add:cli'),
    ('loadbal:service-delete', 'SoftLayer.CLI.loadbal.service_delete:cli'),
    ('loadbal:service-edit', 'SoftLayer.CLI.loadbal.service_edit:cli'),
    ('loadbal:service-toggle', 'SoftLayer.CLI.loadbal.service_toggle:cli'),

    ('messaging', 'SoftLayer.CLI.mq'),
    ('messaging:accounts-list', 'SoftLayer.CLI.mq.accounts_list:cli'),
    ('messaging:endpoints-list', 'SoftLayer.CLI.mq.endpoints_list:cli'),
    ('messaging:ping', 'SoftLayer.CLI.mq.ping:cli'),
    ('messaging:queue-add', 'SoftLayer.CLI.mq.queue_add:cli'),
    ('messaging:queue-detail', 'SoftLayer.CLI.mq.queue_detail:cli'),
    ('messaging:queue-edit', 'SoftLayer.CLI.mq.queue_edit:cli'),
    ('messaging:queue-list', 'SoftLayer.CLI.mq.queue_list:cli'),
    ('messaging:queue-pop', 'SoftLayer.CLI.mq.queue_pop:cli'),
    ('messaging:queue-push', 'SoftLayer.CLI.mq.queue_push:cli'),
    ('messaging:queue-remove', 'SoftLayer.CLI.mq.queue_remove:cli'),
    ('messaging:topic-add', 'SoftLayer.CLI.mq.topic_add:cli'),
    ('messaging:topic-detail', 'SoftLayer.CLI.mq.topic_detail:cli'),
    ('messaging:topic-list', 'SoftLayer.CLI.mq.topic_list:cli'),
    ('messaging:topic-push', 'SoftLayer.CLI.mq.topic_push:cli'),
    ('messaging:topic-remove', 'SoftLayer.CLI.mq.topic_remove:cli'),
    ('messaging:topic-subscribe', 'SoftLayer.CLI.mq.topic_subscribe:cli'),
    ('messaging:topic-unsubscribe', 'SoftLayer.CLI.mq.topic_unsubscribe:cli'),

    ('metadata', 'SoftLayer.CLI.metadata:cli'),

    ('nas', 'SoftLayer.CLI.nas'),
    ('nas:list', 'SoftLayer.CLI.nas.list:cli'),

    ('rwhois', 'SoftLayer.CLI.rwhois'),
    ('rwhois:edit', 'SoftLayer.CLI.rwhois.edit:cli'),
    ('rwhois:show', 'SoftLayer.CLI.rwhois.show:cli'),

    ('server', 'SoftLayer.CLI.server'),
    ('server:cancel', 'SoftLayer.CLI.server.cancel:cli'),
    ('server:cancel-reasons', 'SoftLayer.CLI.server.cancel_reasons:cli'),
    ('server:create', 'SoftLayer.CLI.server.create:cli'),
    ('server:create-options', 'SoftLayer.CLI.server.create_options:cli'),
    ('server:detail', 'SoftLayer.CLI.server.detail:cli'),
    ('server:edit', 'SoftLayer.CLI.server.edit:cli'),
    ('server:list', 'SoftLayer.CLI.server.list:cli'),
    ('server:list-chassis', 'SoftLayer.CLI.server.list_chassis:cli'),
    ('server:nic-edit', 'SoftLayer.CLI.server.nic_edit:cli'),
    ('server:power-cycle', 'SoftLayer.CLI.server.power:power_cycle'),
    ('server:power-off', 'SoftLayer.CLI.server.power:power_off'),
    ('server:power-on', 'SoftLayer.CLI.server.power:power_on'),
    ('server:reboot', 'SoftLayer.CLI.server.power:reboot'),
    ('server:reload', 'SoftLayer.CLI.server.reload:cli'),

    ('snapshot', 'SoftLayer.CLI.snapshot'),
    ('snapshot:cancel', 'SoftLayer.CLI.snapshot.cancel:cli'),
    ('snapshot:create', 'SoftLayer.CLI.snapshot.create:cli'),
    ('snapshot:create-space', 'SoftLayer.CLI.snapshot.create_space:cli'),
    ('snapshot:list', 'SoftLayer.CLI.snapshot.list:cli'),
    ('snapshot:restore-volume', 'SoftLayer.CLI.snapshot.restore_volume:cli'),

    ('sshkey', 'SoftLayer.CLI.sshkey'),
    ('sshkey:add', 'SoftLayer.CLI.sshkey.add:cli'),
    ('sshkey:remove', 'SoftLayer.CLI.sshkey.remove:cli'),
    ('sshkey:edit', 'SoftLayer.CLI.sshkey.edit:cli'),
    ('sshkey:list', 'SoftLayer.CLI.sshkey.list:cli'),
    ('sshkey:print', 'SoftLayer.CLI.sshkey.print:cli'),

    ('ssl', 'SoftLayer.CLI.ssl'),
    ('ssl:add', 'SoftLayer.CLI.ssl.add:cli'),
    ('ssl:download', 'SoftLayer.CLI.ssl.download:cli'),
    ('ssl:edit', 'SoftLayer.CLI.ssl.edit:cli'),
    ('ssl:list', 'SoftLayer.CLI.ssl.list:cli'),
    ('ssl:remove', 'SoftLayer.CLI.ssl.remove:cli'),

    ('subnet', 'SoftLayer.CLI.subnet'),
    ('subnet:cancel', 'SoftLayer.CLI.subnet.cancel:cli'),
    ('subnet:create', 'SoftLayer.CLI.subnet.create:cli'),
    ('subnet:detail', 'SoftLayer.CLI.subnet.detail:cli'),
    ('subnet:list', 'SoftLayer.CLI.subnet.list:cli'),
    ('subnet:lookup', 'SoftLayer.CLI.subnet.lookup:cli'),

    ('ticket', 'SoftLayer.CLI.ticket'),
    ('ticket:create', 'SoftLayer.CLI.ticket.create:cli'),
    ('ticket:detail', 'SoftLayer.CLI.ticket.detail:cli'),
    ('ticket:list', 'SoftLayer.CLI.ticket.list:cli'),
    ('ticket:update', 'SoftLayer.CLI.ticket.update:cli'),
    ('ticket:subjects', 'SoftLayer.CLI.ticket.subjects:cli'),
    ('ticket:summary', 'SoftLayer.CLI.ticket.summary:cli'),

    ('vlan', 'SoftLayer.CLI.vlan'),
    ('vlan:detail', 'SoftLayer.CLI.vlan.detail:cli'),
    ('vlan:list', 'SoftLayer.CLI.vlan.list:cli'),

    ('summary', 'SoftLayer.CLI.summary:cli'),
]
