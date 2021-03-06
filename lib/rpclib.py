from slickrpc import Proxy
import http


# RPC connection
def rpc_connect(rpc_user, rpc_password, server, port):
    try:
        rpc_connection = Proxy("http://%s:%s@%s:%d"%(rpc_user, rpc_password, server, port))
    except Exception as e:
        print(e)
        raise Exception("Connection error! Probably no daemon on selected port.")
    return rpc_connection


# Non CC calls
def getinfo(rpc_connection):
    info = rpc_connection.getinfo()
    return info


def getbalance(rpc_connection):
    balance = rpc_connection.getbalance()
    return balance


def sendrawtransaction(rpc_connection, hex):
    tx_id = rpc_connection.sendrawtransaction(hex)
    return tx_id


def getaccountaddress(rpc_connection, account):
    account_address = rpc_connection.getaccountaddress(account)
    return account_address


def validateaddress(rpc_connection, address):
    validation_result = rpc_connection.validateaddress(address)
    return validation_result


def signmessage(rpc_connection, address, message):
    signature = rpc_connection.signmessage(address, message)
    return signature


def verifymessage(rpc_connection, address, signature, message):
    verifymessage_result = rpc_connection.verifymessage(address, signature, message)
    return verifymessage_result


def kvupdate(rpc_connection, key, value, days, password):
    update_result = rpc_connection.kvupdate(key, value, str(days), password)
    return update_result


def kvsearch(rpc_connection, key):
    kvsearch_result = rpc_connection.kvsearch(key)
    return kvsearch_result


# Dice CC calls

def dice_list(rpc_connection):
    dice_list = rpc_connection.dicelist()
    return dice_list


def dice_info(rpc_connection, dice_txid):
    dice_info = rpc_connection.diceinfo(dice_txid)
    return dice_info


def dice_fund(rpc_connection, name, funds, minbet, maxbet, maxodds, timeoutblocks):
    new_fund = rpc_connection.dicefund(name, funds, minbet, maxbet, maxodds, timeoutblocks)
    return new_fund


def dice_bet(rpc_connection, name, fundingtxid, amount, odds):
    new_bet = rpc_connection.dicebet(name, fundingtxid, amount, odds)
    return new_bet

# Token CC calls
def token_create(rpc_connection, name, supply, description):
    token_hex = rpc_connection.tokencreate(name, supply, description)
    return token_hex


def token_info(rpc_connection, token_id):
    token_info = rpc_connection.tokeninfo(token_id)
    return token_info


# TODO: have to add option with pubkey input
def token_balance(rpc_connection, token_id):
    token_balance = rpc_connection.tokenbalance(token_id)
    return token_balance


def token_list(rpc_connection):
    token_list = rpc_connection.tokenlist()
    return token_list


def token_convert(rpc_connection, evalcode, token_id, pubkey, supply):
    token_convert_hex = rpc_connection.tokenconvert(evalcode, token_id, pubkey, supply)
    return token_convert_hex


# Oracle CC calls
def oracles_create(rpc_connection, name, description, data_type):
    oracles_hex = rpc_connection.oraclescreate(name, description, data_type)
    return oracles_hex


def oracles_register(rpc_connection, oracle_id, data_fee):
    oracles_register_hex = rpc_connection.oraclesregister(oracle_id, data_fee)
    return oracles_register_hex


def oracles_subscribe(rpc_connection, oracle_id, publisher_id, data_fee):
    oracles_subscribe_hex = rpc_connection.oraclessubscribe(oracle_id, publisher_id, data_fee)
    return oracles_subscribe_hex


def oracles_info(rpc_connection, oracle_id):
    oracles_info = rpc_connection.oraclesinfo(oracle_id)
    return oracles_info


def oracles_list(rpc_connection):
    oracles_list = rpc_connection.oracleslist()
    return oracles_list


def oracles_samples(rpc_connection, oracletxid, batonutxo, num):
    oracles_sample = rpc_connection.oraclessamples(oracletxid, batonutxo, num)
    return oracles_sample


def oracles_data(rpc_connection, oracletxid, hexstr):
    oracles_data_hex = rpc_connection.oraclesdata(oracletxid, hexstr)
    return oracles_data_hex


# Gateways CC calls
# Arguments changing dynamically depends of M N, so supposed to wrap it this way
# token_id, oracle_id, coin_name, token_supply, M, N + pubkeys for each N
def gateways_bind(rpc_connection, *args):
    gateways_bind_hex = rpc_connection.gatewaysbind(*args)
    return gateways_bind_hex


def gateways_deposit(rpc_connection, gateway_id, height, coin_name,\
                     coin_txid, claim_vout, deposit_hex, proof, dest_pub, amount):
    gateways_deposit_hex = rpc_connection.gatewaysdeposit(gateway_id, height, coin_name,\
                     coin_txid, claim_vout, deposit_hex, proof, dest_pub, amount)
    return gateways_deposit_hex


def gateways_claim(rpc_connection, gateway_id, coin_name, deposit_txid, dest_pub, amount):
    gateways_claim_hex = rpc_connection.gatewaysclaim(gateway_id, coin_name, deposit_txid, dest_pub, amount)
    return gateways_claim_hex


def gateways_withdraw(rpc_connection, gateway_id, coin_name, withdraw_pub, amount):
    gateways_withdraw_hex = rpc_connection(gateway_id, coin_name, withdraw_pub, amount)
    return gateways_withdraw_hex


# Channels CC calls
def channels_info(rpc_connection, channel_id=None):
    info = rpc_connection.channelsinfo(channel_id)
    return info


def channels_open(rpc_connection, destpubkey, paymentsnum, denomination):
    new_channel = rpc_connection.channelsopen(destpubkey, paymentsnum, denomination)
    return new_channel


def channels_list(rpc_connection):
    channels_list = rpc_connection.channelslist()
    return channels_list


def channels_payment(rpc_connection, channel_txid, sum):
    payment = rpc_connection.channelspayment(channel_txid, sum)
    return payment
