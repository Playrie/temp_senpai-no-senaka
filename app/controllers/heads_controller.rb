class HeadsController < ApplicationController
    before_action :authenticate_user!, :set_kerberos

    def index
        redirect_to kerberos_path
    end

    def set_kerberos
        @kerbero = Kerbero.find(current_user.kerbero_id)
    end
end
