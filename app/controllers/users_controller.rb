class UsersController < ApplicationController
    before_action :authenticate_user!

    def set_id
        if !current_user.is_set_id
            @kerbero = Kerbero.find(current_user.kerbero_id)
            case current_user.position
            when "left"
                @kerbero.left_user_id = current_user.id
            when "center"
                @kerbero.center_user_id = current_user.id            
            when "right"
                @kerbero.right_user_id = current_user.id
            end
            if @kerbero.left_user_id * @kerbero.center_user_id * @kerbero.right_user_id != 0
                @kerbero.is_confirmed = true
            end
            if @kerbero.save 
                current_user.is_set_id = true
                current_user.save
            end
        end
        redirect_to head_path
    end
end
